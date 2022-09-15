from fastapi import FastAPI, HTTPException, status
from sqlmodel import Session, select
from app.database import create_db_and_tables, engine
from app.models import BaseTasks, TasksTable, AddTask, UpdateTask, Status, ReadTask
from typing import List
from datetime import datetime


description = """
<br />
<br />
## About this App
<br />
You are able to store all your tasks in this awesome app,
<br />
so you won't **forget** any...
<br />
<br />
**You can:**
* Add tasks
* Get all your tasks
* Update tasks
* Delete tasks
* And a few extra features...

"""

tags_metadata = [
    {
        "name": "AllTasks",
        "description": "Returns all your tasks stored in the list"
    },
    {
        "name": "AddTask",
        "description": "Add task to the list, please use the proper request body"
    },
    {
        "name": "GetTask",
        "description": "Returns a task from the list by its ID"
    },
    {
        "name": "DeleteTask",
        "description": "Deletes a task from the list by its ID"
    },
        {
        "name": "UpdateTask",
        "description": "Updates a task from the list by its ID, please use the proper request body"
    },
        {
        "name": "GetStatus",
        "description": "Returns tasks with selected status"
    },
    {
        "name": "DeleteDone",
        "description": 'Deletes all tasks with status: "done"'
    }
]



app = FastAPI(title="My ToDoList",
            description=description,
            version="1.2.1",
            contact={
                "name": "Peter Babos",
                "email": "peterbabos@hotmail.com"
            },
            openapi_tags=tags_metadata)


# Creates the database
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Get all the items from the database
@app.get("/todolist", response_model=List[ReadTask], status_code=status.HTTP_200_OK, tags=["AllTasks"])
async def get_all_tasks():
    with Session(engine) as session:
        tasks = session.exec(select(TasksTable)).all()
        return tasks


# Add new item to the database
@app.post("/todolist/", response_model=ReadTask, status_code=status.HTTP_201_CREATED, tags=["AddTask"])
async def add_task(addtask: AddTask):
        with Session(engine) as session:
            new_task=TasksTable.from_orm(addtask)
            session.add(new_task)
            session.commit()
            session.refresh(new_task)
            return new_task


# Get a single item from the database by id
@app.get("/todolist/{id}", response_model=ReadTask, status_code=status.HTTP_200_OK, tags=["GetTask"])
async def get_task(id:int):
    with Session(engine) as session:
        task_by_id = session.get(TasksTable, id)
        if not task_by_id:
            raise HTTPException(status_code=404, detail="Task not found")
        return task_by_id


# Delete a single item from the database by id
@app.delete("/todolist/{id}", tags=['DeleteTask'])
async def delete_task(id:int):
    with Session(engine) as session:
        task = session.get(TasksTable, id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        session.delete(task)
        session.commit()
        return {"Task deleted": True}


# Update a single item
@app.patch("/todolist/{id}", response_model=ReadTask, tags=["UpdateTask"])
def update_task(id: int, task: UpdateTask):
    with Session(engine) as session:
        db_task = session.get(TasksTable, id)
        if not db_task:
            raise HTTPException(status_code=404, detail="Task not found")
        task_data = task.dict(exclude_unset=True)
        for key, value in task_data.items():
            setattr(db_task, key, value)
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task


# Get items by status
@app.get("/todolist/taskstatus/{status}", response_model=List[ReadTask], status_code=status.HTTP_200_OK, tags=["GetStatus"])
async def tasks_by_status(status: Status):
    with Session(engine) as session:
        task_by_status = select(TasksTable)
        results = session.exec(task_by_status.where(TasksTable.status == status)).all()
        return results


# Delete items are done
@app.delete("/todolist/done/", tags=["DeleteDone"])
async def remove_done():
    with Session(engine) as session:
        statement = select(TasksTable).where(TasksTable.status == "done")
        result = session.exec(statement).all()
        num_of_done = len(result)
        for task in result:
            session.delete(task)
        session.commit()
        if num_of_done == 1:
            return {"{} task deleted".format(num_of_done): True}
        else:
            return {"{} tasks deleted".format(num_of_done): True}

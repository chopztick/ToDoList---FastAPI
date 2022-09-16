from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import date
from enum import Enum
from pydantic import validator

# Class to create a set for status 
class Status(str, Enum):
    not_started = "not_started"
    in_prog = "in_progress"
    done = "done"

# Base class to inherit from, custom date validation added
class BaseTasks(SQLModel):
    task: str = Field(index=True, default="add_task")
    status: Status = Field(default="not_started/in_progress/done")
    due_date: date = Field(default=date.today())



# To create the database, id added
class TasksTable(BaseTasks, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


# Same as TaskTable, just to avoid misunderstanding in app.py
class ReadTask(TasksTable):
    pass

# Same as TaskTable, just to avoid misunderstanding in app.py
class AddTask(BaseTasks):

     # Validation to check if input date is not past date
    @validator('due_date')
    def check_date(cls, v):
        if v < date.today():
            raise ValueError("past values not allowed")
        return v


# Inherited from BaseTask, changed all attribute to optional to be capable for partial update
class UpdateTask(AddTask):
    task: Optional[str] = Field(index=True, default="add_task")
    status: Optional[Status] = Field(default="not_started/in_progress/done")
    due_date: Optional[date] = Field(default=date.today())


# ToDoList App
A simple ToDo List with FastAPI and SQLmodel
<br/>

## About the App

With this application you can create your own ToDo List:
* add tasks (task name, status, due date)
* view all your tasks
* view a single task
* update
* delete
* delete all done tasks
* filter by status
<br/>

## Get started

### Prerequisites

* Python 3.7+
* FastAPI
* Uvicorn
* SQLModel

<br/>

### Steps to get going

  1. Clone repository via command line: `git clone https://github.com/chopztick/ToDoList-FastAPI`
  3. Create virtual environment via conda: `conda create --name <env_name>`
  4. Activate the created environment: `conda activate <env_name>`
  5. Install packages from requirements.txt: `pip install -r requirements.txt`
<br/>

## Run the App
<br/>

1. Via command line: `python main.py`
2. Head to: `http://127.0.0.1:8000`
3. Also check out the docs: `http://127.0.0.1:8000/docs`
<br/>
<br/>

# Features
<br/>
<br/>

## Add task to your list via POST request
<br/>

**Execute the POST request from the docs page or via:**
<br/> **DELETE** `http://127.0.0.1:8000/todolist/`
<br/>

**Please use the following body in your request:**
<br/>
```JSON

{
  "task": "add task here",
  "status": "status",
  "due_date": "date"
}

```

*Task, status and date are all mandatory for successful POST request*
<br/>
 * "task": accepts string
 * "status": following statues allowed: not_started / in_progress / done
 * "due_date": date, use format YYYY-MM-DD, past dates not allowed

<br/>
<br/>

## Get all your tasks from the list via GET request
<br/>

**Execute the GET request from the docs page or via:**
<br/> **GET** `http://127.0.0.1:8000/todolist`

<br/>
Returns your tasks in a list:

```JSON
[
{
  "task": "your task",
  "status": "status",
  "due_date": "date"
}
]
```
<br/>

## Get a task from the list by ID via GET request:
<br/>

**Enter ID and execute the GET request from the docs page or via:**
<br/> **GET** `http://127.0.0.1:8000/todolist/{id}`

<br/>
Returns your requested task:

```JSON
{
  "task": "your task",
  "status": "status",
  "due_date": "date"
}
```
<br/>

## Update a task in your list by ID via PATCH request
<br/>

**Enter ID and execute the PATCH request from the docs page or via:*
<br/> **PATCH** `http://127.0.0.1:8000/todolist/{id}`
<br/>

**Please use the following body in your request:**
<br/>
```JSON

{
  "task": "add task here",
  "status": "status",
  "due_date": "date"
}

```

*Task, status and date are all OPTIONAL*
<br/>
 * "task": accepts string
 * "status": following statues allowed: not_started / in_progress / done
 * "due_date": date, use format YYYY-MM-DD, past dates not allowed

<br/>

## Delete a task from the list by ID via DELETE request
<br/>

**Enter ID and execute the DELETE request from the docs page or via:**
<br/> **DELETE** `http://127.0.0.1:8000/todolist/{id}`
<br/>

*On success returns:*
```JSON

{"Task deleted": true}

```

<br/>

## Delete all tasks from the with *"done"* status via DELETE request
<br/>

**Execute the DELETE request from the docs page or via:**
<br/> **DELETE** `http://127.0.0.1:8000/todolist/done/`
<br/>

*On success returns:*
```JSON

{"<num_of_tasks> tasks deleted": true}

```
<br/>

## Get all your tasks from the list with the selected status via GET request
<br/>

**Select the status and execute the GET request from the docs page or via:** 
<br/> **GET** `http://127.0.0.1:8000/todolist/{status}`

<br/>
Returns your tasks in a list with the selected status

```JSON
[
{
  "task": "your task",
  "status": "your selected status",
  "due_date": "date"
}
]
```
<br/>

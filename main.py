from fastapi import FastAPI, status, Response
from models import Todo

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World"}

todos = []

#Get all todos
@app.get("/todos")
def get_todos():
    return {"todos": todos}

#Get single todo
@app.get("/todos/{id}")
def get_todo(id: int):
    for todo in todos:
        if todo.id == id:
            return {"todo": todo}
    return {"message": "No todos found"}

#Create a todo
@app.post("/todos",status_code= status.HTTP_201_CREATED)
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been added"}

# Update a todo
@app.get("/todos/{id}")
def update_todo(id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == id:
            todo.id = id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": "No todos found to update"}

#Delete a todo
@app.delete("/todos/{id}")
def delete_todo(id: int):
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
            return {"message": "Todo has been deleted"}
    return {"message": "No todos found"}

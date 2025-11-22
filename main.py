from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
def create_item(item: dict):
    return {"item": item}

@app.add_route("/custom", methods=["GET"])
def custom_route():
    return {"message": "This is a custom route!"}
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}

@app.put("/Dung/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item}

@app.put("/dat/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item}
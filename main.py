from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/item/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/create_item/")
def create_item(item: dict):
    return {"item": item}

@app.put("/update_item/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item}

@app.delete("/delete_item/{item_id}")
def delete_item(item_id: int):
    return {"item_id": item_id}

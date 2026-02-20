from fastapi import FastAPI, status, HTTPException

users = {1: "Alice", 2: "Bob", 3: "Charlie"}
items = {
    1: {"name": "Laptop", "price": 1000},
    2: {"name": "Mouse", "price": 20}
}
warehouse = {
    1: {"name": "Apple", "stock": 10},
    2: {"name": "Banana", "stock": 5}
}
app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"name": users[user_id]}


@app.get("/divide")
async def divide(a: int, b: int):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    return {"result": a/b}

@app.get("/admin_only")
async def admin_only(token: str):
    if token != "admin_token":
        raise HTTPException(status_code=403, detail="Access denied")
    return {"message": "Welcome, Admin!"}

@app.put("/items/{item_id}")
async def update_item(item_id: int, price: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id]["price"] = price
    return items[item_id]

@app.post("/buy/{product_id}")
async def buy_product(product_id: int, count: int):
    if not warehouse.get(product_id):
        raise HTTPException(status_code=404, detail="Product not found")
    if warehouse[product_id]["stock"] <= count:
        raise HTTPException(status_code=400, detail="Not enough stock")
    warehouse[product_id]["stock"] -= count
    return {"msg": "Bought!"}
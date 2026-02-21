from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/items")
async def test(skip: int | None = 0, limit: int | None = 10):
    try:
        return {"skip": skip, "limit": limit}
    except:
        raise HTTPException(status_code=422, detail="Internal Server Error")


from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/login")
async def test(username: str, password: str):
    return {"user": username, "password": password}

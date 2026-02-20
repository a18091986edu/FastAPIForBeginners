**uvicorn**

--port
--reload
--host 0.0.0.0
--workers 4

if __name__ == "__main__":
    # Обратите внимание: имя файла передается как строка
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
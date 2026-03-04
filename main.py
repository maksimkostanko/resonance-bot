# filename: main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

# Этот маршрут будет вашей "Interactions Endpoint"
@app.post("/")
async def interactions(req: Request):
    # Discord шлёт JSON, его можно обработать здесь если нужно
    data = await req.json()
    print("Получен запрос от Discord:", data)

    # Возвращаем тип 1 - Pong
    return JSONResponse(content={"type": 1})

# Запуск локально
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

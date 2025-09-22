from fastapi import FastAPI, Body
import os

app = FastAPI(title="Order API")

@app.get("/health")
def health():
    return {"status": "ok", "color": os.getenv("APP_COLOR", "unknown")}

@app.post("/orders")
def create_order(order: dict = Body(...)):
    # echo back with color so we can see which instance served the request
    return {"received": order, "served_by_color": os.getenv("APP_COLOR", "unknown")}

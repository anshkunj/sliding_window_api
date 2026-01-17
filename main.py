
# main.py
from fastapi import FastAPI, HTTPException
from models import Array_input, array_input
import logic

app = FastAPI(
    title="Sliding Window API",
    description="Optimized Sliding Window API (O(n) solutions)",
    version="1.0.0"
)


# Health Check
@app.get("/health")
def health_check():
    return {"status": "OK", "message": "API is running smoothly"}


# -------------------- Next Greater --------------------
@app.get("/next_greater")
def next_greater_get(arr: str):
    if not arr:
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty")
    nums = list(map(int, arr.split(',')))
    return {"result": logic.next_greater(nums)}


@app.post("/next_greater")
def next_greater_post(data: array_input):
    if not data.arr:
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty")
    return {"result": logic.next_greater(data.arr)}


# -------------------- Daily Temperatures --------------------
@app.get("/daily_temperatures")
def daily_temperatures_get(arr: str):
    if not arr:
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty")
    nums = list(map(int, arr.split(',')))
    return {"result": logic.daily_temperatures(nums)}


@app.post("/daily_temperatures")
def daily_temperatures_post(data: array_input):
    if not data.arr:
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty")
    return {"result": logic.daily_temperatures(data.arr)}


# -------------------- Largest Rectangle --------------------
@app.get("/largest_rectangle")
def largest_rectangle_get(arr: str):
    if not arr:
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty")
    nums = list(map(int, arr.split(',')))
    return {"max_area": logic.largest_rectangle(nums)}


@app.post("/largest_rectangle")
def largest_rectangle_post(data: array_input):
    if not data.arr:
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty")
    return {"max_area": logic.largest_rectangle(data.arr)}


# -------------------- Max Sliding Window --------------------
@app.get("/max_sliding_window")
def max_sliding_window_get(arr: str, k: int):
    if not arr or k <= 0:
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty and k must be > 0")
    nums = list(map(int, arr.split(',')))
    return {"result": logic.max_sliding_window(nums, k)}


@app.post("/max_sliding_window")
def max_sliding_window_post(data: Array_input):
    if not data.arr or data.k <= 0:
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty and k must be > 0")
    return {"result": logic.max_sliding_window(data.arr, data.k)}
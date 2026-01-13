# main.py
from fastapi import FastAPI,HTTPException
from models import Array_input,array_input
import logic

app = FastAPI(
	title="sliding_window_api",
	description="Optimized Sliding window API (O(n))",
	version="1.0.0"
)


# health check
@app.get("/health")
def health_check():
    return {"status": "OK", "message": "API is running smoothly"}


# /next_greater
@app.get("/next_greater")
def next_greater_get(arr:str) :
	if not arr :
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty")
	return {
		"result" : logic.next_greater(list(map(int,arr.split(','))))
	}

@app.post("/next_greater")
def next_greater_post(data:array_input) :
	if not data.arr :
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty")
	return {
		"result" : logic.next_greater(data.arr)
	}


# /daily_temperatures
@app.get("/daily_temperatures")
def daily_temperatures_get(arr:str) :
	if not arr :
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty")
	return {
		"result" : logic.daily_temperatures(list(map(int,arr.split(','))))
	}

@app.post("/daily_temperatures")
def daily_temperatures_post(data:array_input) :
	if not data.arr :
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty")
	return {
		"result" : logic.daily_temperatures(data.arr)
	}


# /largest_rectangle
@app.get("/largest_rectangle")
def largest_rectangle_get(arr:str) :
	if not arr :
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty")
	return {
		"max area" : logic.largest_rectangle(list(map(int,arr.split(','))))
	}

@app.post("/largest_rectangle")
def largest_rectangle(data:array_input) :
	if not data.arr :
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty")
	return {
		"max area" : logic.largest_rectangle(data.arr)
	}


# /max_sliding_window
@app.get("/max_sliding_window")
def max_sliding_window_get(arr:str,k:int) :
	if not arr or k <= 0:
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty and k must be > 0")
	return {
		"result" : logic.max_sliding_window(list(map(int,arr.split(','))),k)
	}

@app.post("/max_sliding_window")
def max_sliding_window_post(data:Array_input) :
	if not data.arr or data.k <= 0:
        raise HTTPException(status_code=400, detail="Invalid input: array cannot be empty and k must be > 0")
	return {
		"result" : logic.max_sliding_window(data.arr,data.k)
	}
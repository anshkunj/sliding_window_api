# 🚀 Array Algorithms API (FastAPI)

A production-ready FastAPI-based REST API implementing high-performance array and stack/deque algorithms such as Sliding Window, Monotonic Stack, and Histogram problems.

This project focuses on clean architecture, O(n) optimized solutions, and real-world backend deployment.

---

## 📌 Features

- Optimized algorithms with O(n) time complexity
- FastAPI with automatic Swagger documentation
- Core DSA concepts: Stack, Deque, HashMap
- Fully deployable on Render
- Clean and modular code structure

---

## 🌐 Live Web Service (Render)

🔗 **Base URL:**  
https://sliding-window-api.onrender.com  

📘 **Interactive API Docs (Swagger):**  
https://sliding-window-api.onrender.com/docs  

You can test **GET and POST endpoints directly from the browser**.

---


## 🗂 Project Structure

array-algorithms-api/
├── main.py          # FastAPI app & routes
├── logic.py         # Core algorithm implementations
├── models.py        # Pydantic request models
├── requirements.txt
├── README.md
└── LICENSE

---

## 🧠 Algorithms Implemented

### 1️⃣ Next Greater Element
Find the next greater element to the right of each element.

Example:
Input:  [4, 2, 1, 5]  
Output: [5, 5, 5, -1]

---

### 2️⃣ Daily Temperatures
Return the number of days until a warmer temperature.

Example:
Input:  [73, 74, 75, 71, 69, 72, 76, 73]  
Output: [1, 1, 4, 2, 1, 1, 0, 0]

---

### 3️⃣ Largest Rectangle in Histogram
Find the maximum rectangular area in a histogram.

Example:
Input:  [2, 1, 5, 6, 2, 3]  
Output: 10

---

### 4️⃣ Maximum Sliding Window
Find the maximum element in each sliding window of size k.

Example:
Input:  [2, 1, 3, 4, 6, 3, 8, 9, 10, 12, 56], k = 4  
Output: [4, 6, 6, 8, 9, 10, 12, 56]

---

## 🔌 API Endpoints

POST /next_greater  
POST /daily_temperatures  
POST /largest_rectangle  
POST /max_sliding_window  

GET /next_greater  
GET /daily_temperatures  
GET /largest_rectangle  
GET /max_sliding_window  

---

## 🧾 Request Format (JSON)

{
  "arr": [1, 3, 2, 4],
  "k": 2
}

---

## 📤 Sample Response

{
  "result": [3, 4, 4, -1]
}

---

## ▶️ Run Locally

pip install -r requirements.txt  
uvicorn main:app --reload  

Open in browser:  
http://127.0.0.1:8000/docs

---

## ☁️ Deployment (Render)

Build Command:  
pip install -r requirements.txt  

Start Command:  
uvicorn main:app --host 0.0.0.0 --port 10000

---

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn

---

## 🎯 Learning Outcomes

- Mastery of Monotonic Stack
- Sliding Window optimization
- DSA + Backend integration
- Real-world API deployment experience

---

## 📄 License

MIT License

---

## ⭐ Author

Built with ❤️ by anshkunj

***1***\
**2**\
*3*
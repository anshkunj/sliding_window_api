<p align="center">
  <img src="https://github.com/anshkunj/sliding_window_api/blob/ca7ca07b1302781adca1baa558a385ce55cca86e/1768556862714.jpg" alt="Sliding Window API" width="1200">
</p>

<h1 align="center">Sliding Window API</h1>
<p align="center">
Efficient window-based processing for APIs 🚀
</p>

# 🚀 Sliding Window API 

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

## ⚙️ Installation & Run

1) Clone the repository  
git clone https://github.com/anshkunj/sliding-window-api  
cd sliding-window-api 

2) Install dependencies  
pip install -r requirements.txt  

3) Run the server  
uvicorn main:app --reload  

---

## 🌐 API Documentation

Swagger UI: http://127.0.0.1:8000/docs  

ReDoc: http://127.0.0.1:8000/redoc  

---

## 🌐 Live API

Base URL:  
https://sliding-window-api.onrender.com  
Docs:  
https://sliding-window-api.onrender.com/docs

---


## 🗂 repo Structure
```
sliding-window-api/  
├── main.py          # FastAPI app & routes
├── logic.py         # Core algorithm implementations  
├── models.py        # Pydantic request models  
├── .gitignore  
├── requirements.txt  
├── render.yaml  
├── README.md         # Project Overview  
└── LICENSE           # Licence file (MIT)  
```
---

## 🧠 Algorithms Implemented

### 0️⃣ Home  
Check status of service whether it is live or not.

---

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

GET /health  
GET /next_greater  
POST /next_greater  
GET /daily_temperatures  
POST /daily_temperatures  
GET /largest_rectangle  
POST /largest_rectangle  
GET /max_sliding_window  
POST /max_sliding_window  

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

## 🤝 Contributing
Contributors are welcome!  
• Add new sliding window problems  
• Improve explanations  
• Optimise exists code  

---

## 👤 Author
**anshkunj**  
### 📫 Let’s connect
- **GitHub:** https://github.com/anshkunj
- **LinkedIn:** https://linkedin.com/in/anshkunj
- **Portfolio:** https://anshkunj.github.io/Portfolio
- **LeetCode:** https://leetcode.com/u/anshkunj
- **Devpost:** https://devpost.com/anshkunj
- **HackerRank:** https://www.hackerrank.com/profile/anshkunj
- **AtCoder:** https://atcoder.jp/users/anshkunj
- **Codeforces:** https://codeforces.com/profile/anshkunj
- **Fiverr:** https://www.fiverr.com/anshkunj
- **Freelancer:** https://www.freelancer.com/u/anshkunj

---

## ⭐ Support
If you found this project helpful, give it a star ⭐  
It motivates me to build more real-world APIs 🚀

---

## 🔹 Note
This repository is regularly updated with new scripts and improvements.

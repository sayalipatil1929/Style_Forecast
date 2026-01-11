# 🌤️ STYLE_FORCAST-Weather to Outfit Recommender API
* "Learning how to bridge the gap between external data and user logic."
- This project marks my transition into backend development with FastAPI.<br>
-I built this to demonstrate how a server can "talk" to the outside world, process complex data, and return something useful to a user.
---
## 🎯 The Implementation Goal
* The goal was to create a "middleman" service. My FastAPI server:
1.Listens for a user's city choice.
2.Communicates with the OpenWeatherMap API using asynchronous requests.
3.Translates raw temperature numbers into human-friendly clothing advice.
---
## 🛠️ Skills I Put Into Practice
* Asynchronous Programming: Used async and await with HTTPX so the server doesn't "freeze" while waiting for weather data.
* API Integration: Learned how to read documentation from a third-party provider (OpenWeather) and extract specific data from their JSON.
* Security Best Practices: Used .env files to hide my API keys, ensuring they never get pushed to GitHub.
* Auto-Documentation: Leveraged FastAPI's automatic Swagger UI to make testing easy.
---
## 📁 Project Structure
.
├── .env                # Secret API keys (not uploaded to GitHub)<br>
├── .gitignore          # Tells Git what to ignore (venv, .env)<br>
├── main.py             # My FastAPI implementation logic<br>
├── requirements.txt    # The "ingredients" list for this project<br>
└── README.md           # This file!

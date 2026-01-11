import os
from fastapi import FastAPI, HTTPException
import httpx
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

app = FastAPI(
    title="StyleForecast API",
    description="Bridging the gap between weather data and style logic.",
    version="1.0.0"
)

@app.get("/recommend/{city}")
async def get_outfit(city: str):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        
   
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="City not found")
    
    data = response.json()
    temp = data["main"]["temp"]
    
    
    if temp > 25:
        advice = "It's hot! Wear a T-shirt and shorts."
    elif temp > 15:
        advice = "Pleasant weather. A light hoodie or long-sleeve shirt is fine."
    else:
        advice = "It's cold! You definitely need a heavy jacket."

    
    return {
        "city": city.capitalize(),
        "current_temp": f"{temp}°C",
        "recommendation": advice
    }
import os
import requests
from langchain.tools import tool
from dotenv import load_dotenv

# Load .env from project root
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


@tool
def get_weather(destination: str) -> str:
    """Fetch 3-day weather forecast for a destination city."""
    if not WEATHER_API_KEY:
        return "Weather data unavailable (API key not set)."

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={destination}&appid={WEATHER_API_KEY}&units=metric&cnt=9"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return f"Weather data unavailable for {destination}."

        data = response.json()
        forecasts = []
        seen_dates = set()
        for item in data.get("list", []):
            day = item.get("dt_txt", "").split(" ")[0]
            if day in seen_dates:
                continue
            seen_dates.add(day)
            temp = item.get("main", {}).get("temp", 0)
            temp_min = item.get("main", {}).get("temp_min", 0)
            condition = item.get("weather", [{}])[0].get("description", "")
            icon = item.get("weather", [{}])[0].get("icon", "01d")
            forecasts.append(f"{day}: High {temp}C, Low {temp_min}C, {condition}, icon:{icon}")

        return "Weather Forecast:\n" + "\n".join(forecasts)
    except Exception as e:
        return f"Weather lookup failed: {str(e)}"


@tool
def search_attractions(destination: str, trip_type: str) -> str:
    """Search for top tourist attractions using Tavily API."""
    if not TAVILY_API_KEY:
        return f"Top attractions in {destination}: Visit local landmarks, museums, and popular viewpoints."

    query = f"top tourist attractions in {destination} for {trip_type} travel"
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "basic",
        "max_results": 5
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code != 200:
            return f"Top attractions in {destination}: Visit local landmarks and popular spots."

        results = response.json().get("results", [])
        formatted = []
        for i, res in enumerate(results):
            formatted.append(f"{i+1}. {res.get('title', 'Unknown')} - {res.get('content', '')[:200]}")

        return f"Top Attractions in {destination}:\n" + "\n".join(formatted)
    except Exception as e:
        return f"Attraction search failed: {str(e)}"


@tool
def search_hotels(destination: str, budget: str) -> str:
    """Search for hotels using Tavily API."""
    if not TAVILY_API_KEY:
        return f"Hotels in {destination}: Check popular booking sites for options under {budget} INR."

    query = f"best budget hotels in {destination} under {budget} rupees per night with ratings"
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "basic",
        "max_results": 3
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code != 200:
            return f"Hotels in {destination}: Check booking sites for budget options."

        results = response.json().get("results", [])
        formatted = []
        for i, res in enumerate(results):
            formatted.append(f"{i+1}. {res.get('title', 'Unknown')} - {res.get('content', '')[:200]}")

        return f"Hotels in {destination} under {budget} INR:\n" + "\n".join(formatted)
    except Exception as e:
        return f"Hotel search failed: {str(e)}"


@tool
def get_travel_tips(destination: str) -> str:
    """Get general travel tips for a destination."""
    return (
        f"Travel tips for {destination}:\n"
        f"1. Check visa requirements before booking\n"
        f"2. Carry local currency and a backup card\n"
        f"3. Download offline maps for navigation\n"
        f"4. Book accommodations in advance during peak season\n"
        f"5. Try local street food but pick busy stalls\n"
        f"6. Keep digital copies of all important documents"
    )

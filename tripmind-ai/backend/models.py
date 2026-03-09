# Orbit AI -- Data Models

from pydantic import BaseModel
from typing import List, Optional, Dict


class TripRequest(BaseModel):
    destination: str
    start_date: str
    end_date: str
    budget: int
    travelers: int
    trip_type: str


class WeatherData(BaseModel):
    day: str
    temp_high: float
    temp_low: float
    condition: str
    icon: str = "01d"


class Attraction(BaseModel):
    name: str
    rating: float = 4.0
    distance: str = ""
    category: str = "sightseeing"
    description: str = ""


class Hotel(BaseModel):
    name: str
    price_per_night: int = 0
    rating: float = 4.0
    amenities: List[str] = []


class Activity(BaseModel):
    time: str
    name: str
    description: str = ""
    duration: str = "1 hour"
    pro_tip: str = ""
    category: str = "sightseeing"


class DayPlan(BaseModel):
    day_number: int
    date: str = ""
    weather: Optional[WeatherData] = None
    activities: List[Activity] = []
    daily_budget: int = 0


class TripResponse(BaseModel):
    destination: str
    total_days: int
    total_budget: int
    budget_breakdown: Dict[str, int] = {}
    weather: List[WeatherData] = []
    attractions: List[Attraction] = []
    hotels: List[Hotel] = []
    itinerary: List[DayPlan] = []


class ChatRequest(BaseModel):
    message: str
    trip_id: str = ""
    trip_context: Optional[dict] = None
    context: Optional[dict] = None  # frontend sends 'context'


class ChatResponse(BaseModel):
    response: str = ""
    reply: str = ""  # frontend reads 'reply'
    updated_itinerary: Optional[dict] = None

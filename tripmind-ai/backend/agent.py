import json
import re
from models import TripRequest, TripResponse, ChatRequest, ChatResponse
from demo_data import get_demo_trip, get_demo_chat_response


class TripAgent:
    def __init__(self):
        pass

    def plan_trip(self, req: TripRequest) -> TripResponse:
        """Return demo data for known destinations, fallback for others."""

        # Check if we have demo data for this destination
        demo = get_demo_trip(req.destination)
        if demo:
            print(f"[Agent] Using demo data for '{req.destination}'")
            return TripResponse(**demo)

        # Fallback: return a minimal response
        print(f"[Agent] No demo data for '{req.destination}', returning minimal response")
        from datetime import datetime
        try:
            start = datetime.strptime(req.start_date, "%Y-%m-%d")
            end = datetime.strptime(req.end_date, "%Y-%m-%d")
            num_days = max((end - start).days, 1)
        except Exception:
            num_days = 3

        return TripResponse(
            destination=req.destination,
            total_days=num_days,
            total_budget=req.budget,
            budget_breakdown={
                "accommodation": int(req.budget * 0.4),
                "food": int(req.budget * 0.25),
                "transport": int(req.budget * 0.2),
                "activities": int(req.budget * 0.15)
            },
            weather=[],
            attractions=[],
            hotels=[],
            itinerary=[]
        )

    def chat(self, req: ChatRequest) -> ChatResponse:
        """Return demo chat responses for known destinations."""

        # Get destination from trip context
        context = req.trip_context or req.context or {}
        destination = context.get("destination", "")

        # Get demo response
        reply = get_demo_chat_response(destination, req.message)
        print(f"[Chat] dest='{destination}', msg='{req.message[:50]}', reply='{reply[:50]}'")

        return ChatResponse(response=reply, reply=reply)

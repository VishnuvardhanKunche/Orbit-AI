# ✈️ TripMind AI

AI-powered travel planner that creates personalized itineraries with real-time weather, smart route mapping, and conversational AI assistance.

## 🚀 Features

- **AI Itinerary Planning** — Hour-by-hour schedules with PRO TIPS
- **Interactive Route Maps** — Leaflet-powered maps with numbered stops
- **AI Chat Assistant** — Ask questions, get weather-aware suggestions
- **Budget Tracking** — Daily expense summaries and trip budget breakdown
- **Export Options** — Google Calendar, Email, PDF, Share with friends
- **Live Weather** — Real-time forecasts integrated into planning

## 📁 Project Structure

```
tripmind-ai/
├── frontend/
│   ├── index.html          # Landing page
│   ├── loading.html         # AI processing screen
│   ├── dashboard.html       # Trip dashboard
│   ├── itinerary.html       # Daily itinerary
│   ├── map.html             # Route map
│   ├── chat.html            # AI chat assistant
│   ├── export.html          # Export options
│   ├── css/style.css        # Shared styles
│   └── js/
│       ├── config.js        # API keys & config
│       ├── main.js          # Shared utilities
│       ├── agent.js         # Backend API calls
│       ├── map.js           # Leaflet map module
│       ├── chat.js          # Chat module
│       ├── email.js         # EmailJS integration
│       └── pdf.js           # jsPDF integration
├── backend/
│   ├── main.py              # FastAPI server
│   ├── agent.py             # AI agent (Gemini)
│   ├── tools.py             # API tools (weather, places)
│   ├── rag.py               # RAG for travel docs
│   ├── models.py            # Data models
│   └── data/travel_docs/    # Upload travel PDFs here
├── .env                     # API keys (create from template)
├── requirements.txt         # Python dependencies
└── README.md
```

## ⚡ Quick Start

### Backend
```bash
cd backend
pip install -r ../requirements.txt
python main.py
```

### Frontend
Open `frontend/index.html` in your browser, or serve with:
```bash
cd frontend
python -m http.server 5500
```

## 🔑 API Keys Needed

| Service | Key | Used For |
|---------|-----|----------|
| Google Gemini | `GOOGLE_API_KEY` | AI trip planning & chat |
| OpenWeatherMap | `WEATHER_API_KEY` | Live weather forecasts |
| EmailJS | `EMAILJS_*` | Email itinerary export |

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Vanilla JS
- **Backend:** Python, FastAPI
- **AI:** Google Gemini, LangChain
- **Maps:** Leaflet.js + OpenStreetMap
- **PDF:** jsPDF
- **Email:** EmailJS

---
© 2024 TripMind AI. All rights reserved.

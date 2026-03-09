# Orbit AI -- Static Demo Data for 4 Destinations
# Used for demo video submission. Returns instant, detailed responses.

DEMO_DESTINATIONS = {

    "goa": {
        "destination": "Goa, India",
        "total_days": 3,
        "total_budget": 50000,
        "budget_breakdown": {"accommodation": 18000, "food": 12000, "transport": 8000, "activities": 12000},
        "weather": [
            {"day": "2026-03-15", "temp_high": 33, "temp_low": 25, "condition": "Sunny", "icon": "01d"},
            {"day": "2026-03-16", "temp_high": 32, "temp_low": 24, "condition": "Partly Cloudy", "icon": "02d"},
            {"day": "2026-03-17", "temp_high": 34, "temp_low": 26, "condition": "Clear Sky", "icon": "01d"}
        ],
        "attractions": [
            {"name": "Baga Beach", "rating": 4.5, "distance": "12 km", "category": "beach", "description": "Famous for water sports, nightlife, and shacks along the shore."},
            {"name": "Fort Aguada", "rating": 4.3, "distance": "15 km", "category": "heritage", "description": "17th-century Portuguese fort with a lighthouse offering panoramic sea views."},
            {"name": "Dudhsagar Falls", "rating": 4.7, "distance": "60 km", "category": "nature", "description": "One of India's tallest waterfalls surrounded by lush green forest."},
            {"name": "Basilica of Bom Jesus", "rating": 4.6, "distance": "10 km", "category": "heritage", "description": "UNESCO World Heritage Site housing the remains of St. Francis Xavier."},
            {"name": "Anjuna Flea Market", "rating": 4.1, "distance": "18 km", "category": "shopping", "description": "Vibrant Wednesday market with handicrafts, clothes, and street food."}
        ],
        "hotels": [
            {"name": "Goa Marriott Resort & Spa", "price_per_night": 8000, "rating": 4.5, "amenities": ["wifi", "pool", "spa", "restaurant"]},
            {"name": "Treebo Trend Morjim", "price_per_night": 3500, "rating": 4.0, "amenities": ["wifi", "ac", "breakfast"]},
            {"name": "OYO Calangute Beach", "price_per_night": 2000, "rating": 3.8, "amenities": ["wifi", "ac", "parking"]}
        ],
        "itinerary": [
            {
                "day_number": 1, "date": "2026-03-15",
                "weather": {"day": "2026-03-15", "temp_high": 33, "temp_low": 25, "condition": "Sunny", "icon": "01d"},
                "activities": [
                    {"time": "09:00", "name": "Arrive in Goa", "description": "Check in to your hotel and freshen up.", "duration": "2 hours", "pro_tip": "Book a pre-paid taxi from the airport to avoid overcharging.", "category": "travel"},
                    {"time": "11:00", "name": "Baga Beach", "description": "Relax on the beach, try parasailing and jet skiing.", "duration": "3 hours", "pro_tip": "Negotiate prices for water sports - you can get 30% off the quoted price.", "category": "beach"},
                    {"time": "14:00", "name": "Lunch at Britto's", "description": "Seafood lunch at this iconic Baga Beach shack.", "duration": "1.5 hours", "pro_tip": "Try the Goan Fish Curry Rice - their signature dish.", "category": "food"},
                    {"time": "16:00", "name": "Fort Aguada", "description": "Explore the 17th-century Portuguese fort and lighthouse.", "duration": "2 hours", "pro_tip": "Visit before sunset for stunning views of the Arabian Sea.", "category": "sightseeing"},
                    {"time": "19:00", "name": "Tito's Lane Nightlife", "description": "Experience Goa's famous nightlife strip with clubs and bars.", "duration": "3 hours", "pro_tip": "Couples get free entry at most clubs before 10 PM.", "category": "nightlife"}
                ],
                "daily_budget": 18000
            },
            {
                "day_number": 2, "date": "2026-03-16",
                "weather": {"day": "2026-03-16", "temp_high": 32, "temp_low": 24, "condition": "Partly Cloudy", "icon": "02d"},
                "activities": [
                    {"time": "07:00", "name": "Dudhsagar Falls Trip", "description": "Full-day excursion to Dudhsagar waterfalls via jeep safari.", "duration": "4 hours", "pro_tip": "Carry waterproof bags for your phone and camera.", "category": "adventure"},
                    {"time": "12:00", "name": "Spice Plantation Lunch", "description": "Traditional Goan thali at a spice plantation en route.", "duration": "1.5 hours", "pro_tip": "Buy fresh spices directly from the plantation - much cheaper than markets.", "category": "food"},
                    {"time": "14:30", "name": "Old Goa Churches", "description": "Visit Basilica of Bom Jesus and Se Cathedral.", "duration": "2 hours", "pro_tip": "Entry is free. Dress modestly as these are active places of worship.", "category": "heritage"},
                    {"time": "17:00", "name": "Panjim Latin Quarter", "description": "Walk through the colorful Portuguese-style houses of Fontainhas.", "duration": "1.5 hours", "pro_tip": "Perfect for Instagram photos - the pastel-colored buildings are gorgeous at golden hour.", "category": "sightseeing"},
                    {"time": "19:30", "name": "Mango Tree Restaurant", "description": "Riverside dinner with live Fado music.", "duration": "2 hours", "pro_tip": "Reserve a riverside table for the best atmosphere.", "category": "food"}
                ],
                "daily_budget": 16000
            },
            {
                "day_number": 3, "date": "2026-03-17",
                "weather": {"day": "2026-03-17", "temp_high": 34, "temp_low": 26, "condition": "Clear Sky", "icon": "01d"},
                "activities": [
                    {"time": "08:00", "name": "Anjuna Flea Market", "description": "Browse handicrafts, clothes, jewelry and souvenirs.", "duration": "2 hours", "pro_tip": "Bargain hard - start at 50% of the quoted price.", "category": "shopping"},
                    {"time": "10:30", "name": "Chapora Fort", "description": "The famous 'Dil Chahta Hai' fort with panoramic views.", "duration": "1.5 hours", "pro_tip": "Climb up early morning to avoid the heat and crowds.", "category": "sightseeing"},
                    {"time": "12:30", "name": "Lunch at Gunpowder", "description": "South Indian-Goan fusion cuisine in a garden setting.", "duration": "1.5 hours", "pro_tip": "Try their pork vindaloo - it's the best in Goa.", "category": "food"},
                    {"time": "14:30", "name": "Palolem Beach", "description": "Relax at Goa's most beautiful crescent-shaped beach.", "duration": "3 hours", "pro_tip": "Rent a kayak to spot dolphins in the bay.", "category": "beach"},
                    {"time": "18:00", "name": "Departure", "description": "Head to the airport with memories of an amazing trip!", "duration": "1.5 hours", "pro_tip": "Keep 2 hours buffer for airport traffic during peak season.", "category": "travel"}
                ],
                "daily_budget": 16000
            }
        ]
    },

    "tirupathi": {
        "destination": "Tirupathi, Andhra Pradesh",
        "total_days": 2,
        "total_budget": 25000,
        "budget_breakdown": {"accommodation": 8000, "food": 5000, "transport": 7000, "activities": 5000},
        "weather": [
            {"day": "2026-03-15", "temp_high": 35, "temp_low": 22, "condition": "Sunny", "icon": "01d"},
            {"day": "2026-03-16", "temp_high": 34, "temp_low": 21, "condition": "Clear Sky", "icon": "01d"}
        ],
        "attractions": [
            {"name": "Tirumala Venkateswara Temple", "rating": 4.9, "distance": "22 km", "category": "temple", "description": "One of the most visited temples in the world, dedicated to Lord Venkateswara."},
            {"name": "Sri Padmavathi Ammavari Temple", "rating": 4.5, "distance": "5 km", "category": "temple", "description": "Temple dedicated to Goddess Padmavathi, consort of Lord Venkateswara."},
            {"name": "Talakona Waterfall", "rating": 4.3, "distance": "49 km", "category": "nature", "description": "Highest waterfall in Andhra Pradesh surrounded by dense forest."},
            {"name": "Sri Venkateswara National Park", "rating": 4.2, "distance": "25 km", "category": "nature", "description": "Biodiverse park with endemic species of flora and fauna."},
            {"name": "Silathoranam", "rating": 4.4, "distance": "24 km", "category": "nature", "description": "Natural rock arch formation on Tirumala Hills, a geological wonder."}
        ],
        "hotels": [
            {"name": "Marasa Sarovar Premiere", "price_per_night": 5000, "rating": 4.4, "amenities": ["wifi", "pool", "restaurant", "ac"]},
            {"name": "Hotel Bliss", "price_per_night": 2500, "rating": 4.0, "amenities": ["wifi", "ac", "parking"]},
            {"name": "TTD Guest House", "price_per_night": 500, "rating": 3.5, "amenities": ["basic", "ac"]}
        ],
        "itinerary": [
            {
                "day_number": 1, "date": "2026-03-15",
                "weather": {"day": "2026-03-15", "temp_high": 35, "temp_low": 22, "condition": "Sunny", "icon": "01d"},
                "activities": [
                    {"time": "06:00", "name": "Arrive in Tirupathi", "description": "Reach Tirupathi and check in to hotel.", "duration": "1.5 hours", "pro_tip": "Book hotel near the bus stand for easy access to Tirumala.", "category": "travel"},
                    {"time": "08:00", "name": "Sri Padmavathi Temple", "description": "Visit the temple dedicated to Goddess Padmavathi.", "duration": "1.5 hours", "pro_tip": "Visit early morning to avoid long queues.", "category": "temple"},
                    {"time": "10:00", "name": "Travel to Tirumala", "description": "Take the ghat road bus to Tirumala hills.", "duration": "1 hour", "pro_tip": "APSRTC buses go every 5 minutes. Cost is just Rs 75.", "category": "travel"},
                    {"time": "11:30", "name": "Tirumala Venkateswara Temple", "description": "Darshan at the world-famous temple of Lord Balaji.", "duration": "4 hours", "pro_tip": "Book Rs 300 special darshan online at ttdsevaonline.com for shorter wait.", "category": "temple"},
                    {"time": "16:00", "name": "Silathoranam", "description": "Visit the natural rock arch formation.", "duration": "1 hour", "pro_tip": "It is a 1 km walk from the bus stand - wear comfortable shoes.", "category": "sightseeing"},
                    {"time": "18:00", "name": "Tirumala Laddu Prasadam", "description": "Collect the famous Tirumala laddus.", "duration": "1 hour", "pro_tip": "Each person can buy 2 laddus for Rs 50 with darshan ticket.", "category": "food"}
                ],
                "daily_budget": 13000
            },
            {
                "day_number": 2, "date": "2026-03-16",
                "weather": {"day": "2026-03-16", "temp_high": 34, "temp_low": 21, "condition": "Clear Sky", "icon": "01d"},
                "activities": [
                    {"time": "07:00", "name": "Talakona Waterfall", "description": "Day trip to the highest waterfall in AP.", "duration": "3 hours", "pro_tip": "Best visited during or just after monsoon for full water flow.", "category": "nature"},
                    {"time": "11:00", "name": "Sri Venkateswara National Park", "description": "Explore the biodiversity park with a guided nature walk.", "duration": "2 hours", "pro_tip": "Carry binoculars to spot rare birds and slender loris.", "category": "nature"},
                    {"time": "13:30", "name": "Lunch at Andhra Bhavan", "description": "Authentic Andhra meals with unlimited thali.", "duration": "1 hour", "pro_tip": "Try the pulihora and pesarattu - local specialties.", "category": "food"},
                    {"time": "15:00", "name": "Chandragiri Fort", "description": "Historic fort with a sound and light show.", "duration": "2 hours", "pro_tip": "The museum inside has rare Vijayanagara artifacts.", "category": "heritage"},
                    {"time": "18:00", "name": "Departure", "description": "Head back home with divine blessings!", "duration": "1 hour", "pro_tip": "Buy Tirupathi laddus at railway station if you missed them.", "category": "travel"}
                ],
                "daily_budget": 12000
            }
        ]
    },

    "yanam": {
        "destination": "Yanam, Puducherry",
        "total_days": 2,
        "total_budget": 15000,
        "budget_breakdown": {"accommodation": 4000, "food": 4000, "transport": 4000, "activities": 3000},
        "weather": [
            {"day": "2026-03-15", "temp_high": 34, "temp_low": 24, "condition": "Humid", "icon": "50d"},
            {"day": "2026-03-16", "temp_high": 33, "temp_low": 23, "condition": "Partly Cloudy", "icon": "02d"}
        ],
        "attractions": [
            {"name": "Yanam River Front", "rating": 4.2, "distance": "1 km", "category": "nature", "description": "Scenic riverfront along the Godavari with French colonial architecture."},
            {"name": "Rajiv Gandhi Memorial", "rating": 4.0, "distance": "2 km", "category": "heritage", "description": "Memorial park dedicated to former PM Rajiv Gandhi."},
            {"name": "French War Memorial", "rating": 4.1, "distance": "1.5 km", "category": "heritage", "description": "Monument commemorating French soldiers from colonial era."},
            {"name": "Yanam Church", "rating": 4.3, "distance": "1 km", "category": "heritage", "description": "Beautiful 18th-century church with French architectural style."},
            {"name": "Coringa Wildlife Sanctuary", "rating": 4.4, "distance": "25 km", "category": "nature", "description": "Mangrove forest sanctuary with rare bird species near Kakinada."}
        ],
        "hotels": [
            {"name": "Hotel & Convention Daspalla", "price_per_night": 3500, "rating": 4.2, "amenities": ["wifi", "ac", "restaurant", "pool"]},
            {"name": "Yanam Guest House", "price_per_night": 1200, "rating": 3.5, "amenities": ["ac", "parking"]},
            {"name": "OYO Yanam Town", "price_per_night": 800, "rating": 3.3, "amenities": ["wifi", "ac"]}
        ],
        "itinerary": [
            {
                "day_number": 1, "date": "2026-03-15",
                "weather": {"day": "2026-03-15", "temp_high": 34, "temp_low": 24, "condition": "Humid", "icon": "50d"},
                "activities": [
                    {"time": "09:00", "name": "Arrive in Yanam", "description": "Reach Yanam via Kakinada and check in.", "duration": "1.5 hours", "pro_tip": "Yanam is just 10 km from Kakinada - take an auto for Rs 150.", "category": "travel"},
                    {"time": "10:30", "name": "Yanam River Front Walk", "description": "Morning walk along the scenic Godavari riverfront.", "duration": "1.5 hours", "pro_tip": "Early morning is best for photography with mist over the river.", "category": "nature"},
                    {"time": "12:30", "name": "French Colonial Heritage Walk", "description": "Walk through French-era buildings, the church, and war memorial.", "duration": "2 hours", "pro_tip": "Yanam was a French colony until 1954 - the architecture is unique.", "category": "heritage"},
                    {"time": "15:00", "name": "Rajiv Gandhi Memorial", "description": "Visit the memorial park and gardens.", "duration": "1 hour", "pro_tip": "Free entry. Well-maintained gardens perfect for a peaceful evening.", "category": "sightseeing"},
                    {"time": "17:00", "name": "Local Andhra Seafood Dinner", "description": "Fresh fish and prawn curry at a local eatery.", "duration": "1.5 hours", "pro_tip": "Try the Godavari fish fry - Yanam is famous for fresh river fish.", "category": "food"}
                ],
                "daily_budget": 8000
            },
            {
                "day_number": 2, "date": "2026-03-16",
                "weather": {"day": "2026-03-16", "temp_high": 33, "temp_low": 23, "condition": "Partly Cloudy", "icon": "02d"},
                "activities": [
                    {"time": "07:00", "name": "Coringa Wildlife Sanctuary", "description": "Boat ride through dense mangrove forests.", "duration": "3 hours", "pro_tip": "Book a boat at Coringa for Rs 500 - you may spot fishing cats!", "category": "nature"},
                    {"time": "11:00", "name": "Kakinada Beach", "description": "Visit the nearby Kakinada beach and lighthouse.", "duration": "2 hours", "pro_tip": "The Uppada beach nearby has beautiful sunrise views.", "category": "beach"},
                    {"time": "13:30", "name": "Lunch at Subbayya Hotel", "description": "Famous Andhra meals in Kakinada.", "duration": "1 hour", "pro_tip": "Their bamboo chicken biryani is legendary.", "category": "food"},
                    {"time": "15:00", "name": "Shopping in Yanam", "description": "Buy duty-free liquor and French perfumes (Yanam is a UT).", "duration": "1.5 hours", "pro_tip": "Yanam being a Union Territory has cheaper liquor than AP.", "category": "shopping"},
                    {"time": "17:00", "name": "Departure", "description": "Head back with memories of this hidden gem!", "duration": "1 hour", "pro_tip": "Carry extra packing for the duty-free items.", "category": "travel"}
                ],
                "daily_budget": 7000
            }
        ]
    },

    "kasi": {
        "destination": "Varanasi (Kasi), Uttar Pradesh",
        "total_days": 3,
        "total_budget": 35000,
        "budget_breakdown": {"accommodation": 12000, "food": 8000, "transport": 7000, "activities": 8000},
        "weather": [
            {"day": "2026-03-15", "temp_high": 32, "temp_low": 18, "condition": "Sunny", "icon": "01d"},
            {"day": "2026-03-16", "temp_high": 33, "temp_low": 19, "condition": "Clear Sky", "icon": "01d"},
            {"day": "2026-03-17", "temp_high": 31, "temp_low": 17, "condition": "Hazy", "icon": "50d"}
        ],
        "attractions": [
            {"name": "Kashi Vishwanath Temple", "rating": 4.8, "distance": "3 km", "category": "temple", "description": "One of the 12 Jyotirlingas, the holiest Shiva temple in India."},
            {"name": "Dashashwamedh Ghat", "rating": 4.7, "distance": "2 km", "category": "spiritual", "description": "The main ghat with the spectacular Ganga Aarti every evening."},
            {"name": "Sarnath", "rating": 4.5, "distance": "10 km", "category": "heritage", "description": "Where Lord Buddha gave his first sermon. UNESCO site with ancient stupas."},
            {"name": "Manikarnika Ghat", "rating": 4.3, "distance": "2.5 km", "category": "spiritual", "description": "The primary cremation ghat, believed to grant moksha (liberation)."},
            {"name": "Ramnagar Fort", "rating": 4.2, "distance": "14 km", "category": "heritage", "description": "18th-century fort across the Ganges with a museum of vintage cars and weapons."}
        ],
        "hotels": [
            {"name": "Taj Ganges Varanasi", "price_per_night": 7000, "rating": 4.6, "amenities": ["wifi", "pool", "spa", "restaurant"]},
            {"name": "Hotel Surya Varanasi", "price_per_night": 3500, "rating": 4.1, "amenities": ["wifi", "ac", "restaurant"]},
            {"name": "Zostel Varanasi", "price_per_night": 800, "rating": 4.0, "amenities": ["wifi", "common-area", "rooftop"]}
        ],
        "itinerary": [
            {
                "day_number": 1, "date": "2026-03-15",
                "weather": {"day": "2026-03-15", "temp_high": 32, "temp_low": 18, "condition": "Sunny", "icon": "01d"},
                "activities": [
                    {"time": "08:00", "name": "Arrive in Varanasi", "description": "Check in and rest after journey.", "duration": "2 hours", "pro_tip": "Stay near Assi Ghat for a quieter experience away from crowds.", "category": "travel"},
                    {"time": "10:30", "name": "Kashi Vishwanath Temple", "description": "Visit the most sacred Shiva temple in India.", "duration": "2.5 hours", "pro_tip": "Book darshan online to skip the regular queue. Carry only phone, no bags.", "category": "temple"},
                    {"time": "13:30", "name": "Lunch at Kashi Chat Bhandar", "description": "Famous street food - tamatar chaat, kachori, and lassi.", "duration": "1 hour", "pro_tip": "The tamatar chaat here is unique to Varanasi - a must try!", "category": "food"},
                    {"time": "15:00", "name": "Boat Ride on Ganges", "description": "Row along the 84 ghats of Varanasi by boat.", "duration": "2 hours", "pro_tip": "Hire a private boat for Rs 500/hour. Best at sunrise or late afternoon.", "category": "sightseeing"},
                    {"time": "18:00", "name": "Ganga Aarti at Dashashwamedh", "description": "Witness the spectacular evening Ganga Aarti ceremony.", "duration": "1.5 hours", "pro_tip": "Reach by 5:30 PM to get a front-row seat on the steps.", "category": "spiritual"}
                ],
                "daily_budget": 12000
            },
            {
                "day_number": 2, "date": "2026-03-16",
                "weather": {"day": "2026-03-16", "temp_high": 33, "temp_low": 19, "condition": "Clear Sky", "icon": "01d"},
                "activities": [
                    {"time": "05:30", "name": "Sunrise Boat Ride", "description": "Watch the sunrise over the Ganges from a wooden boat.", "duration": "1.5 hours", "pro_tip": "The sunrise view with the ghats in golden light is magical.", "category": "spiritual"},
                    {"time": "08:00", "name": "Morning Walk through Ghats", "description": "Walk from Assi Ghat to Manikarnika Ghat along the river.", "duration": "2 hours", "pro_tip": "Watch silk weavers at work in the narrow lanes near the ghats.", "category": "sightseeing"},
                    {"time": "11:00", "name": "Sarnath Excursion", "description": "Visit where Buddha gave his first sermon. See the Dhamek Stupa and museum.", "duration": "3 hours", "pro_tip": "The Sarnath Museum has the original Lion Capital of Ashoka.", "category": "heritage"},
                    {"time": "15:00", "name": "Banarasi Silk Shopping", "description": "Visit the famous silk weaving workshops and showrooms.", "duration": "2 hours", "pro_tip": "Buy directly from weavers in the Muslim quarter for authentic prices.", "category": "shopping"},
                    {"time": "18:00", "name": "Dinner at Blue Lassi", "description": "Famous lassi shop followed by dinner at Pizzeria Vaatika.", "duration": "2 hours", "pro_tip": "Blue Lassi has been serving since 1925 - try the saffron flavor.", "category": "food"}
                ],
                "daily_budget": 12000
            },
            {
                "day_number": 3, "date": "2026-03-17",
                "weather": {"day": "2026-03-17", "temp_high": 31, "temp_low": 17, "condition": "Hazy", "icon": "50d"},
                "activities": [
                    {"time": "07:00", "name": "Subah-e-Banaras", "description": "Experience the spiritual morning rituals at the ghats.", "duration": "1.5 hours", "pro_tip": "Join a free walking tour to understand the rituals deeply.", "category": "spiritual"},
                    {"time": "09:00", "name": "Ramnagar Fort", "description": "Cross the Ganges to visit this 18th-century fort and museum.", "duration": "2 hours", "pro_tip": "The vintage car collection and weapons museum are fascinating.", "category": "heritage"},
                    {"time": "12:00", "name": "Lunch at Deena Chaat", "description": "The most famous chaat in all of UP.", "duration": "1 hour", "pro_tip": "Get the basket chaat and palak patta chaat.", "category": "food"},
                    {"time": "14:00", "name": "BHU & Bharat Kala Bhavan", "description": "Visit the beautiful campus and its world-class art museum.", "duration": "2 hours", "pro_tip": "The museum has rare miniature paintings and ancient sculptures.", "category": "heritage"},
                    {"time": "17:00", "name": "Departure", "description": "Leave Varanasi with spiritual memories for a lifetime.", "duration": "1 hour", "pro_tip": "Varanasi airport is just 26 km - keep 2 hours for traffic.", "category": "travel"}
                ],
                "daily_budget": 11000
            }
        ]
    }
}


# Chat responses for each destination
DEMO_CHAT = {
    "goa": [
        "Goa is perfect for beaches, nightlife, and seafood! The best time to visit is November to February for pleasant weather.",
        "For water sports at Baga Beach, expect to pay around Rs 500-1500 per activity. Always negotiate!",
        "Don't miss the Goan Fish Curry Rice - it's the soul of Goan cuisine. Britto's at Baga is iconic.",
        "Rent a scooter for Rs 300-400/day to explore at your own pace. It's the best way to see Goa.",
    ],
    "tirupathi": [
        "Tirupathi is the most visited pilgrimage site in the world! Lord Venkateswara temple gets 50,000+ visitors daily.",
        "Book your darshan tickets online at ttdsevaonline.com at least 2 days in advance. Rs 300 special darshan saves hours.",
        "The famous Tirupathi laddu is made with pure ghee and costs Rs 25 each. You can buy 2 per person.",
        "Wear comfortable clothes and shoes - the queue involves a lot of walking. Carry minimal belongings.",
    ],
    "yanam": [
        "Yanam is a hidden gem! It's one of India's smallest Union Territories, a former French colony on the Godavari river.",
        "Being a Union Territory, Yanam has cheaper liquor and some duty-free items. Great for budget shopping!",
        "The Coringa Wildlife Sanctuary nearby has the second-largest mangrove forest in India. Boat rides cost Rs 500.",
        "Try the fresh Godavari river fish - prawn curry and fish fry are local specialties you won't find this fresh elsewhere.",
    ],
    "kasi": [
        "Varanasi (Kasi) is the oldest living city in the world! Every lane has 3,000 years of history.",
        "The Ganga Aarti at Dashashwamedh Ghat is a must-see. Arrive by 5:30 PM to get good seats on the steps.",
        "Must-try street food: tamatar chaat, kachori sabzi, malaiyo (winter only), and the legendary Blue Lassi.",
        "Hire a boat for sunrise on the Ganges - Rs 500/hour for a private boat. It's the most spiritual experience in India.",
    ]
}


def get_demo_trip(destination: str) -> dict:
    """Return demo trip data if destination matches, else None."""
    key = destination.lower().strip()
    for demo_key, data in DEMO_DESTINATIONS.items():
        if demo_key in key or key in demo_key:
            return data
    return None


def get_demo_chat_response(destination: str, message: str) -> str:
    """Return a demo chat response based on destination."""
    
    # Exact matches for the 16 demo questions (4 per location)
    msg_lower = message.lower().strip()
    exact_matches = {
        # GOA
        "best time to visit goa?": "The best time to visit Goa is between November and mid-February. The weather is pleasantly cool and comfortable, perfect for relaxing on the beaches and enjoying the vibrant nightlife!",
        "what is the itinerary for goa?": "Your 3-day Goa itinerary includes: Day 1: Exploring Baga Beach, Fort Aguada, and Tito's Lane. Day 2: A jeep safari to Dudhsagar Falls, spice plantation lunch, and Panjim Latin Quarter. Day 3: Anjuna Flea market, Chapora Fort, and Palolem Beach.",
        "top water sports in goa?": "You must try parasailing, jet skiing, and banana boat rides at Baga or Calangute beach. For scuba diving and snorkeling, Grande Island is the best spot!",
        "best seafood in goa?": "For authentic Goan seafood, try the Goan Fish Curry Rice at Britto's in Baga, or the prawn balchao at Martin's Corner in South Goa.",
        
        # TIRUPATHI
        "how to book tirupathi darshan?": "You can book the Special Entry Darshan (Rs. 300) online through the official TTD website (ttdsevaonline.com). It's highly recommended to book at least 60 days in advance as slots fill up very quickly!",
        "what is the itinerary for tirupathi?": "Your 2-day Tirupathi itinerary involves: Day 1: Arrival, visiting Sri Padmavathi Temple, traveling up the ghat road, and the main Lord Balaji Darshan. Day 2: Nature trip to Talakona Waterfall, Sri Venkateswara National Park, and Chandragiri Fort.",
        "how to reach tirumala?": "You can take the APSRTC buses from Tirupathi bus stand which run every 5 minutes and cost Rs 75. Alternatively, you can trek up via the Alipiri or Srivari Mettu footpaths.",
        "is mobile phone allowed inside?": "No, mobile phones, cameras, and electronic gadgets are strictly prohibited inside the Tirumala temple. You must deposit them at the free safe deposit lockers before entering the queue.",

        # YANAM
        "what makes yanam special?": "Yanam is unique because it's a former French colony geographically located in Andhra Pradesh but governed by Puducherry! It offers a beautiful blend of French colonial architecture, Telugu culture, and serene views along the Godavari river.",
        "what is the itinerary for yanam?": "Your 2-day Yanam itinerary features: Day 1: Godavari riverfront walk, French Colonial Heritage walk, Rajiv Gandhi Memorial, and local seafood. Day 2: Boat ride in Coringa Wildlife Sanctuary, Kakinada Beach, and duty-free shopping.",
        "best time to visit coringa?": "Coringa Wildlife Sanctuary is best visited early in the morning between November and February. A boat ride costs around Rs 500, and you might spot the elusive fishing cat or rare migratory birds!",
        "famous food in yanam?": "Yanam is famous for blending Godavari style Andhra cuisine with subtle French influences. You must try the fresh river prawn curry (royyala kura) and the local Godavari fish fry.",

        # KASI (VARANASI)
        "which ghats to visit in kasi?": "Dashashwamedh Ghat is a must-visit for the spectacular evening Ganga Aarti. Assi Ghat is great for a peaceful morning boat ride, and Manikarnika Ghat offers a profound glimpse into the cycle of life and death.",
        "what is the itinerary for kasi?": "Your 3-day Kasi itinerary: Day 1: Kashi Vishwanath Darshan and evening Ganga Aarti. Day 2: Sunrise boat ride, walking the 84 ghats, and an excursion to Sarnath. Day 3: Subah-e-Banaras experience, Ramnagar Fort, and BHU campus.",
        "what time is the ganga aarti?": "The famous Ganga Aarti at Dashashwamedh Ghat takes place every evening at 6:45 PM in summer and 6:00 PM in winter. It's best to arrive 45 minutes early to secure a good viewing spot on the steps or rent a boat.",
        "best street food in varanasi?": "Varanasi is a food paradise! You must try the unique Tamatar Chaat at Kashi Chat Bhandar, fresh Malaiyo (in winter), Kachori Sabzi for breakfast, and the legendary saffron lassi at Blue Lassi."
    }
    
    if msg_lower in exact_matches:
        return exact_matches[msg_lower]
        
    key = destination.lower().strip()
    import random
    for demo_key, responses in DEMO_CHAT.items():
        if demo_key in key or key in demo_key:
            # Try to pick a contextually relevant response
            if any(w in msg_lower for w in ["food", "eat", "restaurant", "cuisine"]):
                return [r for r in responses if any(w in r.lower() for w in ["food", "eat", "curry", "lassi", "chaat", "fish"])] [0] if any(any(w in r.lower() for w in ["food", "eat", "curry", "lassi", "chaat", "fish"]) for r in responses) else random.choice(responses)
            if any(w in msg_lower for w in ["cost", "budget", "price", "money", "cheap"]):
                return [r for r in responses if any(w in r.lower() for w in ["rs", "cost", "pay", "price", "cheaper", "budget"])] [0] if any(any(w in r.lower() for w in ["rs", "cost", "pay", "price", "cheaper", "budget"]) for r in responses) else random.choice(responses)
            return random.choice(responses)
    return "I'd love to help with your trip! Could you tell me more about what you'd like to know?"

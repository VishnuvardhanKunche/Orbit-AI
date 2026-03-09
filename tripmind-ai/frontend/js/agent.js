// ============================================
// Orbit AI — Agent (Backend API Calls)
// ============================================

const Agent = {
  // Plan a new trip
  async planTrip(destination, startDate, endDate, travelers, budget, tripType) {
    try {
      const response = await fetch(`${CONFIG.API_BASE_URL}/plan-trip`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ destination, start_date: startDate, end_date: endDate, travelers: parseInt(travelers), budget: parseInt(budget), trip_type: tripType }),
      });
      if (!response.ok) throw new Error('Failed to plan trip');
      return await response.json();
    } catch (err) {
      console.error('Agent.planTrip error:', err);
      throw err;
    }
  },

  // Get itinerary for a specific day
  async getItinerary(tripId, day) {
    try {
      const response = await fetch(`${CONFIG.API_BASE_URL}/itinerary/${tripId}?day=${day}`);
      if (!response.ok) throw new Error('Failed to fetch itinerary');
      return await response.json();
    } catch (err) {
      console.error('Agent.getItinerary error:', err);
      throw err;
    }
  },

  // Chat with AI assistant
  async chat(tripId, message, context) {
    try {
      const response = await fetch(`${CONFIG.API_BASE_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ trip_id: tripId, message, context: context }),
      });
      if (!response.ok) throw new Error('Chat request failed');
      return await response.json();
    } catch (err) {
      console.error('Agent.chat error:', err);
      throw err;
    }
  },

  // Get route data
  async getRoute(tripId, day) {
    try {
      const response = await fetch(`${CONFIG.API_BASE_URL}/route/${tripId}?day=${day}`);
      if (!response.ok) throw new Error('Failed to fetch route');
      return await response.json();
    } catch (err) {
      console.error('Agent.getRoute error:', err);
      throw err;
    }
  },

  // Get dashboard data
  async getDashboard(tripId) {
    try {
      const response = await fetch(`${CONFIG.API_BASE_URL}/dashboard/${tripId}`);
      if (!response.ok) throw new Error('Failed to fetch dashboard');
      return await response.json();
    } catch (err) {
      console.error('Agent.getDashboard error:', err);
      throw err;
    }
  },
};

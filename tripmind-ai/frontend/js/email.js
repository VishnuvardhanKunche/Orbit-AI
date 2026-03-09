// ============================================
// TripMind AI — Email (EmailJS Integration)
// ============================================

const EmailModule = {
  init() {
    if (typeof emailjs !== 'undefined') {
      emailjs.init(CONFIG.EMAILJS_PUBLIC_KEY);
      console.log('EmailJS initialized');
    } else {
      console.warn('EmailJS SDK not loaded');
    }
  },

  // Send itinerary email
  async sendItinerary(toEmail, tripData) {
    try {
      const templateParams = {
        to_email: toEmail,
        trip_name: tripData.destination || 'Your Trip',
        trip_dates: tripData.dates || '',
        itinerary_html: this.buildItineraryHTML(tripData),
      };
      const result = await emailjs.send(
        CONFIG.EMAILJS_SERVICE_ID,
        CONFIG.EMAILJS_TEMPLATE_ID,
        templateParams
      );
      showToast('Itinerary sent to your email!', 'success');
      return result;
    } catch (err) {
      console.error('Email send error:', err);
      showToast('Failed to send email. Please try again.', 'error');
      throw err;
    }
  },

  // Build HTML content for email
  buildItineraryHTML(tripData) {
    if (!tripData.itinerary) return '<p>No itinerary data available.</p>';
    let html = `<h2>${tripData.destination}</h2>`;
    html += `<p>${tripData.dates} | ${tripData.travelers} travelers</p>`;
    if (tripData.itinerary.days) {
      tripData.itinerary.days.forEach(day => {
        html += `<h3>${day.title}</h3>`;
        if (day.activities) {
          day.activities.forEach(act => {
            html += `<p><strong>${act.time}</strong> — ${act.name}: ${act.description}</p>`;
          });
        }
      });
    }
    return html;
  },
};

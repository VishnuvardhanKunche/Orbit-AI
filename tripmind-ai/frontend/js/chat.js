// ============================================
// Orbit AI — Chat Module
// ============================================

const Chat = {
  messagesContainer: null,
  inputField: null,

  init(messagesSelector, inputSelector) {
    this.messagesContainer = document.querySelector(messagesSelector);
    this.inputField = document.querySelector(inputSelector);
    if (this.inputField) {
      this.inputField.focus();
    }

    // Populate sidebar with trip context
    const tripData = loadTripData();
    if (tripData) {
      document.getElementById('sidebar-trip-name').textContent = tripData.destination || 'Unknown Destination';
      let dates = '';
      if (tripData.startDate && tripData.endDate) dates = `${tripData.startDate} to ${tripData.endDate}`;
      else dates = tripData.dates || 'No dates selected';
      document.getElementById('sidebar-trip-dates').textContent = dates;
    }
  },

  // Add an AI message bubble
  addAIMessage(text, extras = {}) {
    const bubble = document.createElement('div');
    bubble.className = 'chat-bubble ai';
    let extraHTML = '';
    if (extras.verified) {
      extraHTML += '<div class="verified-badge">✅ VERIFIED ROUTE</div>';
    }
    if (extras.source) {
      extraHTML += `<div class="source-badge">🤖 Source: ${extras.source}</div>`;
    }
    if (extras.actionBtn) {
      extraHTML += `<button class="chat-action-btn" onclick="${extras.actionBtn.onclick}">↻ ${extras.actionBtn.label}</button>`;
    }
    bubble.innerHTML = `
      <div class="bubble-avatar">🤖</div>
      <div>
        <div class="bubble-content">${text}</div>
        ${extraHTML}
        <div class="chat-timestamp">${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</div>
      </div>
    `;
    this.messagesContainer.appendChild(bubble);
    this.scrollToBottom();
  },

  // Add a user message bubble
  addUserMessage(text) {
    const bubble = document.createElement('div');
    bubble.className = 'chat-bubble user';
    bubble.innerHTML = `
      <div>
        <div class="bubble-content">${text}</div>
        <div class="chat-timestamp">${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</div>
      </div>
    `;
    this.messagesContainer.appendChild(bubble);
    this.scrollToBottom();
  },

  // Add typing indicator
  showTyping() {
    const typing = document.createElement('div');
    typing.className = 'chat-bubble ai typing-indicator';
    typing.id = 'typing-indicator';
    typing.innerHTML = `
      <div class="bubble-avatar">🤖</div>
      <div class="bubble-content" style="padding:12px 18px;">
        <span class="dot-typing"></span>
      </div>
    `;
    this.messagesContainer.appendChild(typing);
    this.scrollToBottom();
  },

  hideTyping() {
    const el = document.getElementById('typing-indicator');
    if (el) el.remove();
  },

  scrollToBottom() {
    if (this.messagesContainer) {
      this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
    }
  },

  // Send message handler
  async sendMessage() {
    const text = this.inputField.value.trim();
    if (!text) return;
    this.addUserMessage(text);
    this.inputField.value = '';
    this.showTyping();
    try {
      const tripData = loadTripData() || { destination: 'Goa, India', dates: 'Dec 12 - Dec 15, 2024', budget: '₹50000' };
      const tripId = tripData ? tripData.id : 'demo';
      const response = await Agent.chat(tripId, text, tripData);
      this.hideTyping();
      this.addAIMessage(response.reply, {
        verified: response.verified,
        source: response.source,
        actionBtn: response.action ? { label: response.action.label, onclick: response.action.onclick } : null,
      });
    } catch (err) {
      this.hideTyping();
      this.addAIMessage('Sorry, I encountered an error. Please try again.');
    }
    this.inputField.focus();
  },

  saveUpdatedItinerary() {
    // Simulate updating the itinerary in localStorage
    showToast('Itinerary updated and saved! ✅', 'success');
  }
};

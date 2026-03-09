// ============================================
// Orbit AI — Main (Shared Utilities)
// ============================================

// Utility: show/hide elements
function show(el) { el.classList.remove('hidden'); }
function hide(el) { el.classList.add('hidden'); }
function toggle(el) { el.classList.toggle('hidden'); }

// Utility: query selectors
const $ = (sel, ctx = document) => ctx.querySelector(sel);
const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

// Utility: format currency
function formatCurrency(amount, currency = 'INR') {
  return new Intl.NumberFormat('en-US', { style: 'currency', currency }).format(amount);
}

// Utility: format date
function formatDate(dateStr) {
  const d = new Date(dateStr);
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
}

// Utility: navigate to page
function navigateTo(page) {
  window.location.href = page;
}

// Utility: get URL params
function getParam(key) {
  return new URLSearchParams(window.location.search).get(key);
}

// Utility: store trip data in localStorage
function saveTripData(data) {
  localStorage.setItem('orbit_trip', JSON.stringify(data));
}

function loadTripData() {
  const raw = localStorage.getItem('orbit_trip');
  return raw ? JSON.parse(raw) : null;
}

function clearTripData() {
  localStorage.removeItem('orbit_trip');
}

// Utility: simple toast notification
function showToast(message, type = 'info') {
  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.textContent = message;
  toast.style.cssText = `
    position: fixed; bottom: 24px; right: 24px;
    padding: 12px 24px; border-radius: 8px;
    color: #fff; font-weight: 600; font-size: 0.875rem;
    z-index: 9999; animation: fadeIn 0.3s ease;
    background: ${type === 'success' ? '#22C55E' : type === 'error' ? '#EF4444' : '#2563EB'};
  `;
  document.body.appendChild(toast);
  setTimeout(() => { toast.style.opacity = '0'; setTimeout(() => toast.remove(), 300); }, 3000);
}

// DOM ready
document.addEventListener('DOMContentLoaded', () => {
  console.log('Orbit AI initialized');
});

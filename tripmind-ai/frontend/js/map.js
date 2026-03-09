// ============================================
// TripMind AI — Map (Leaflet Integration)
// ============================================

let map = null;
let routeLayer = null;
let markers = [];

const MapModule = {
  // Initialize the Leaflet map
  init(containerId, center = [48.8566, 2.3522], zoom = CONFIG.DEFAULT_ZOOM) {
    map = L.map(containerId).setView(center, zoom);
    L.tileLayer(CONFIG.MAP_TILE_URL, {
      attribution: CONFIG.MAP_ATTRIBUTION,
      maxZoom: 18,
    }).addTo(map);
    return map;
  },

  // Add a numbered marker
  addMarker(lat, lng, label, popupText, color = '#2563EB') {
    const icon = L.divIcon({
      className: 'custom-marker',
      html: `<div style="
        background:${color}; color:#fff;
        width:32px; height:32px; border-radius:50%;
        display:flex; align-items:center; justify-content:center;
        font-weight:700; font-size:13px; font-family:Inter,sans-serif;
        box-shadow:0 2px 8px rgba(0,0,0,0.2);
      ">${label}</div>`,
      iconSize: [32, 32],
      iconAnchor: [16, 16],
    });
    const marker = L.marker([lat, lng], { icon }).addTo(map);
    if (popupText) marker.bindPopup(popupText);
    markers.push(marker);
    return marker;
  },

  // Add start marker (green)
  addStartMarker(lat, lng, popupText) {
    return this.addMarker(lat, lng, '🏠', popupText, '#22C55E');
  },

  // Draw route line between coordinates
  drawRoute(coords, color = '#2563EB') {
    if (routeLayer) map.removeLayer(routeLayer);
    routeLayer = L.polyline(coords, {
      color,
      weight: 3,
      dashArray: '8 8',
      opacity: 0.8,
    }).addTo(map);
    map.fitBounds(routeLayer.getBounds(), { padding: [50, 50] });
    return routeLayer;
  },

  // Clear all markers and routes
  clear() {
    markers.forEach(m => map.removeLayer(m));
    markers = [];
    if (routeLayer) { map.removeLayer(routeLayer); routeLayer = null; }
  },

  // Fit map to all markers
  fitToMarkers() {
    if (markers.length === 0) return;
    const group = L.featureGroup(markers);
    map.fitBounds(group.getBounds(), { padding: [50, 50] });
  },
};

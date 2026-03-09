// ============================================
// TripMind AI — PDF (jsPDF Integration)
// ============================================

const PDFModule = {
  // Generate and download itinerary PDF
  generatePDF(tripData) {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    // Header
    doc.setFontSize(22);
    doc.setTextColor(37, 99, 235); // primary blue
    doc.text('TripMind AI', 20, 20);

    doc.setFontSize(10);
    doc.setTextColor(100, 116, 139);
    doc.text('Your AI-powered travel itinerary', 20, 28);

    // Trip title
    doc.setFontSize(18);
    doc.setTextColor(30, 41, 59);
    doc.text(tripData.destination || 'Your Trip', 20, 44);

    doc.setFontSize(11);
    doc.setTextColor(100, 116, 139);
    doc.text(`${tripData.dates || ''} | ${tripData.travelers || 2} travelers | Budget: ${tripData.budget || 'N/A'}`, 20, 52);

    // Separator
    doc.setDrawColor(226, 232, 240);
    doc.line(20, 56, 190, 56);

    // Itinerary content
    let y = 65;
    if (tripData.itinerary && tripData.itinerary.days) {
      tripData.itinerary.days.forEach(day => {
        if (y > 260) { doc.addPage(); y = 20; }

        doc.setFontSize(14);
        doc.setTextColor(37, 99, 235);
        doc.text(day.title, 20, y);
        y += 8;

        if (day.activities) {
          day.activities.forEach(act => {
            if (y > 270) { doc.addPage(); y = 20; }

            doc.setFontSize(10);
            doc.setTextColor(37, 99, 235);
            doc.text(act.time, 24, y);

            doc.setTextColor(30, 41, 59);
            doc.text(` — ${act.name}`, 24 + doc.getTextWidth(act.time + ' '), y);
            y += 5;

            doc.setFontSize(9);
            doc.setTextColor(100, 116, 139);
            const lines = doc.splitTextToSize(act.description || '', 155);
            doc.text(lines, 28, y);
            y += lines.length * 4.5 + 4;
          });
        }
        y += 6;
      });
    } else {
      doc.setFontSize(11);
      doc.setTextColor(100, 116, 139);
      doc.text('No itinerary data available. Plan your trip first!', 20, y);
    }

    // Footer
    const pageCount = doc.internal.getNumberOfPages();
    for (let i = 1; i <= pageCount; i++) {
      doc.setPage(i);
      doc.setFontSize(8);
      doc.setTextColor(148, 163, 184);
      doc.text(`© ${new Date().getFullYear()} TripMind AI — Page ${i} of ${pageCount}`, 20, 290);
    }

    // Download
    const filename = `TripMind_${(tripData.destination || 'Trip').replace(/\s+/g, '_')}.pdf`;
    doc.save(filename);
    showToast('PDF downloaded!', 'success');
  },
};

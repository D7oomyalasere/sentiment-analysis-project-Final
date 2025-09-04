document.addEventListener("DOMContentLoaded", async () => {
  const token = localStorage.getItem("token");
  const container = document.getElementById("historyContainer");

  if (!token) {
    alert("⚠️ Please login to view your history.");
    window.location.href = "/login";
    return;
  }

  try {
    const response = await fetch("/history/", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    if (!response.ok) {
      throw new Error(`Server responded with status ${response.status}`);
    }

    const results = await response.json();

    if (!Array.isArray(results)) {
      throw new Error("Unexpected response format");
    }

    if (results.length === 0) {
      container.innerHTML = `
        <div class="history-item" style="text-align: center; color: #ccc;">
          <i class="fas fa-info-circle"></i> No analysis history found yet.
        </div>`;
      return;
    }

    results.forEach(item => {
      const div = document.createElement("div");
      div.className = "history-item";

      div.innerHTML = `
        <div class="sentiment">
          <i class="fas fa-circle" style="color: lightgreen;"></i>
          ${item.sentiment.toUpperCase()} — <span style="font-weight: 400;">${Math.round(item.confidence * 100)}%</span>
        </div>
        <div class="text">"${item.text}"</div>
        <div class="timestamp">
          <i class="fas fa-clock"></i> ${new Date(item.timestamp).toLocaleString()}
        </div>
      `;

      container.appendChild(div);
    });

  } catch (err) {
    console.error("❌ Error loading history:", err);
    container.innerHTML = `
      <div class="history-item" style="text-align: center; color: #e74c3c;">
        <i class="fas fa-exclamation-triangle"></i> Failed to load history. Please try again later.
      </div>`;
  }
});

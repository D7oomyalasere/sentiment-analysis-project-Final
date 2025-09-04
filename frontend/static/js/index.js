document.addEventListener("DOMContentLoaded", () => {
    const analyzeBtn = document.getElementById("analyzeBtn");
    const textInput = document.getElementById("textInput");
    const sentimentText = document.getElementById("sentimentText");
    const analyzedText = document.getElementById("analyzedText");
    const confidenceFill = document.getElementById("confidenceFill");
    const historyList = document.getElementById("historyList");
  
    analyzeBtn.addEventListener("click", async () => {
      const text = textInput.value.trim();
      if (!text) {
        alert("⚠️ Please enter text to analyze.");
        return;
      }
  
      const token = localStorage.getItem("token");
      const headers = {
        "Content-Type": "application/json"
      };
      if (token) {
        headers["Authorization"] = `Bearer ${token}`;
      } else {
        alert("❗ You must be logged in to analyze.");
        return;
      }
  
      console.log("🚀 Sending text to /predict/:", text);
      console.log("🛡️ Using token:", token);
  
      try {
        const response = await fetch("/predict/predict", {
          method: "POST",
          headers: headers,
          body: JSON.stringify({ text })
        });
  
        const data = await response.json();
  
        console.log("📥 Response from /predict/:", data);
  
        if (response.ok) {
          sentimentText.textContent = data.sentiment;
          analyzedText.textContent = data.text;
          const confidence = data.confidence || data.score || 0;
          confidenceFill.style.width = `${Math.round(confidence * 100)}%`;
          confidenceFill.textContent = `${Math.round(confidence * 100)}%`;
  
          const li = document.createElement("li");
          li.textContent = `${data.text} → ${data.sentiment}`;
          historyList.prepend(li);
        } else {
          alert(`❌ Error: ${data.detail || "Unknown error occurred."}`);
        }
      } catch (error) {
        console.error("🔥 Error in fetch:", error);
        alert("🚨 Network error occurred. Please try again.");
      }
    });
  });
  
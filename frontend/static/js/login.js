window.addEventListener("load", () => {
  const loginForm = document.getElementById("loginForm");
  const emailInput = document.getElementById("email");
  const passwordInput = document.getElementById("password");

  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();

    if (!email || !password) {
      alert("⚠️ Please fill in both fields.");
      return;
    }

    try {
      const response = await fetch("/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
      });

      const data = await response.json();

      if (response.ok) {
        localStorage.setItem("token", data.access_token);
        console.log("✅ Token saved, redirecting...");
        window.location.href = "/analyze";
      } else {
        alert(`❌ ${data.detail || "Login failed."}`);
      }
    } catch (error) {
      console.error("🚨 Error during login:", error);
      alert("🚨 Network error. Try again later.");
    }
  });
});

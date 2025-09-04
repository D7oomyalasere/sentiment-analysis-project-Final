document.getElementById("registerForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const btn = this.querySelector("button");
  const originalText = btn.innerHTML;

  // استرجاع البيانات
  const username = document.getElementById("username").value.trim();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();
  const date = document.getElementById("date").value;
  const gender = document.getElementById("gender").value;

  // تحقق بسيط من المدخلات
  if (!username || !email || !password || !date || !gender) {
    return alert("⚠️ Please fill in all fields.");
  }

  // التحقق من صحة البريد الإلكتروني
  const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
  if (!emailPattern.test(email)) {
    return alert("⚠️ Please enter a valid email.");
  }

  // التحقق من قوة كلمة المرور
  if (password.length < 8) {
    return alert("⚠️ Password must be at least 8 characters long.");
  }

  // عرض التحميل
  btn.disabled = true;
  btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Registering...`;

  try {
    const response = await fetch("/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, email, password, date, gender })
    });

    const result = await response.json();

    if (response.ok) {
      alert("✅ Account created successfully! Redirecting to login...");
      window.location.href = "/login";
    } else {
      alert("❌ " + (result.detail || "Registration failed."));
    }
  } catch (error) {
    console.error("Registration error:", error);
    alert("❌ Something went wrong. Please try again.");
  } finally {
    // إعادة الزر لحالته الطبيعية
    btn.disabled = false;
    btn.innerHTML = originalText;
  }
});


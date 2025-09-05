# 📌 Sentiment Analysis Project | مشروع تحليل المشاعر

## 🌍 English Version

### 🔹 Overview

This is a **Sentiment Analysis Web Application** built with **FastAPI (Backend)** and a simple **HTML/CSS/JS Frontend**.
It allows users to input English text and get the **predicted sentiment** using a trained deep learning model (LSTM/BERT).

### 🔹 Features

* 🔑 User Authentication (Login & Register).
* 📝 Sentiment Prediction (7 Categories: sadness, disappointment, anger, neutral, happiness, excitement, gratitude).
* 📊 History Tracking (stores past analyses).
* 🌐 Simple Web Interface.
* 🗄️ Database Integration.

### 🔹 Project Structure

```
📂 sentiment-analysis-project-Final
 ┣ 📂 backend        # FastAPI backend, routers, database
 ┣ 📂 frontend       # Static HTML, CSS, JS files
 ┣ 📂 model          # Sentiment analysis model files
 ┣ 📜 main.py        # Main entry point
 ┣ 📜 requirements.txt
 ┣ 📜 README.md
 ┣ 📜 .env
```

### 🔹 Installation & Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/D7oomyalasere/sentiment-analysis-project-Final.git
   cd sentiment-analysis-project-Final
   ```
2. **Create and activate virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate # On Linux/Mac
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Run the server**

   ```bash
   uvicorn main:app --reload
   ```
5. **Access the app**

   * API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   * Frontend: [http://127.0.0.1:8000/static/front.html](http://127.0.0.1:8000/static/front.html)

---

## 🇸🇦 النسخة العربية

### 🔹 نظرة عامة

هذا المشروع هو **تطبيق ويب لتحليل المشاعر** مبني باستخدام **FastAPI (الخلفية)** وواجهة بسيطة **HTML/CSS/JS**.
يسمح للمستخدم بإدخال نص باللغة الإنجليزية والحصول على **تصنيف المشاعر** باستخدام نموذج تعلم عميق (LSTM/BERT).

### 🔹 المميزات

* 🔑 تسجيل دخول وتسجيل مستخدمين.
* 📝 تحليل النصوص وتصنيفها (7 فئات: الحزن، خيبة الأمل، الغضب، محايد، السعادة، الحماس، الامتنان).
* 📊 حفظ سجل التحليلات السابقة.
* 🌐 واجهة ويب سهلة.
* 🗄️ قاعدة بيانات متكاملة.

### 🔹 هيكل المشروع

```
📂 sentiment-analysis-project-Final
 ┣ 📂 backend        # الكود الخلفي + قاعدة البيانات
 ┣ 📂 frontend       # ملفات الواجهة الأمامية (HTML/CSS/JS)
 ┣ 📂 model          # ملفات نموذج تحليل المشاعر
 ┣ 📜 main.py        # نقطة التشغيل الرئيسية
 ┣ 📜 requirements.txt
 ┣ 📜 README.md
 ┣ 📜 .env
```

### 🔹 خطوات التشغيل

1. **تحميل المشروع**

   ```bash
   git clone https://github.com/D7oomyalasere/sentiment-analysis-project-Final.git
   cd sentiment-analysis-project-Final
   ```
2. **إنشاء وتفعيل بيئة بايثون**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # على Windows
   source venv/bin/activate # على Linux/Mac
   ```
3. **تثبيت المكتبات المطلوبة**

   ```bash
   pip install -r requirements.txt
   ```
4. **تشغيل السيرفر**

   ```bash
   uvicorn main:app --reload
   ```
5. **الوصول للتطبيق**

   * واجهة الـ API: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   * واجهة المستخدم: [http://127.0.0.1:8000/static/front.html](http://127.0.0.1:8000/static/front.html)

---

📌 **Note / ملاحظة**:
The project is still under development and can be improved with:

* Advanced frontend (React/Vue).
* Better model (Transformer-based like BERT).
* Deployment online (Heroku, Render, etc.).

import os
import sys

from fastapi import FastAPI
from fastapi.testclient import TestClient

# ✅ أضف المسار الصحيح للـ backend إلى sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_path = os.path.abspath(os.path.join(current_dir, "..", "backend"))
routers_path = os.path.join(backend_path, "routers")

if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

if routers_path not in sys.path:
    sys.path.insert(0, routers_path)

try:
    from routers.predict_router import router
    print("📦 تم تحميل predict_router بنجاح ✅")
except Exception as e:
    print("❌ فشل استيراد الراوتر:", e)
    raise e

# ⛳️ إعداد FastAPI للتست
app = FastAPI()
app.include_router(router, prefix="/predict", tags=["Prediction"])

client = TestClient(app)

def test_predict_sentiment():
    payload = {"text": "This is amazing!"}
    response = client.post("/predict/predict", json=payload)
    print("🧪 STATUS:", response.status_code)
    print("🧪 BODY:", response.text)
    assert response.status_code in [200, 401]

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from backend import schemas, models, database
from backend.load_model import predict_emotion
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)

# 🔐 إعداد التوكن
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.post("/", response_model=schemas.SentimentResponse)
def predict(
    input: schemas.TextInput,
    db: Session = Depends(database.get_db),
    token: str = Depends(oauth2_scheme)
):
    try:
        # ✅ فك التوكن والتحقق
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        # ✅ تحليل النص باستخدام النموذج
        result_data = predict_emotion(input.text)
        sentiment = result_data["label"]
        confidence = result_data["confidence"]

        # ✅ تخزين النتيجة في قاعدة البيانات
        result = models.SentimentResult(
            text=input.text,
            sentiment=sentiment,
            confidence=confidence,  # ✅ أضف هذا السطر
            user_id=user_id,
            timestamp=datetime.utcnow() + timedelta(hours=3)
    )

        db.add(result)
        db.commit()

        return {
            "text": input.text,
            "sentiment": sentiment,
            "score": confidence,
            "confidence": confidence,
            "timestamp": result.timestamp
        }

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        print("🔥 Error in /predict:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

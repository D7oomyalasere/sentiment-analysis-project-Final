from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from backend import database, models, schemas
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    tags=["History"]
)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.get("/", response_model=list[schemas.SentimentResponse])
def get_user_history(
    db: Session = Depends(database.get_db),
    token: str = Depends(oauth2_scheme)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        results = db.query(models.SentimentResult).filter(
            models.SentimentResult.user_id == user_id
        ).order_by(models.SentimentResult.timestamp.desc()).all()
        return results

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    except Exception as e:
        print("🔥 Error loading history:", repr(e))  # ← هذا يعرض الخطأ
        raise HTTPException(status_code=500, detail=str(e))  # ← هذا يوصله للواجهة
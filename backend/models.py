from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Date, Float
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from backend.database import Base
import enum

# ✅ تعريف Enum للمشاعر
class SentimentEnum(enum.Enum):
    sadness = "sadness"
    joy = "joy"
    anger = "anger"
    fear = "fear"
    neutral = "neutral"
    surprise = "surprise"
    disgust = "disgust"

# ✅ جدول المستخدمين
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    date = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)

    sentiments = relationship("SentimentResult", back_populates="user")

# ✅ جدول نتائج تحليل المشاعر
class SentimentResult(Base):
    __tablename__ = "sentiment_results"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(1000), nullable=False)
    sentiment = Column(Enum(SentimentEnum), nullable=False)
    confidence = Column(Float, nullable=True)  # إذا أضفتها سابقًا
    timestamp = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=3))  # ✅ الوقت السعودي

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="sentiments")

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# =====================================
# 🧍‍♂️ المستخدم
# =====================================

# 🔹 نموذج إدخال عند إنشاء مستخدم جديد
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    date: str  # تاريخ الميلاد أو التسجيل بصيغة نصية
    gender: str

# 🔹 نموذج لتسجيل الدخول
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# 🔹 نموذج الاستجابة بعد إنشاء الحساب أو الحصول على معلومات المستخدم
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    date: str
    gender: str

    class Config:
        from_attributes = True  # ✅ Pydantic v2: بديل orm_mode


# =====================================
# 🔐 التوكن
# =====================================

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# =====================================
# 💬 تحليل المشاعر
# =====================================

# 🔹 إدخال نص للتحليل
class TextInput(BaseModel):
    text: str

# 🔹 استجابة تحليل المشاعر
class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    score: Optional[float] = None
    confidence: Optional[float] = None
    timestamp: datetime

    class Config:
        from_attributes = True
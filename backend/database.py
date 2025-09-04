# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

# بيانات الاتصال بقاعدة البيانات
DATABASE_USERNAME = "root"
DATABASE_PASSWORD = quote_plus("Qq@z1122")  # تأمين الباسورد بالترميز
DATABASE_HOST = "localhost"
DATABASE_NAME = "sentiment_db"

# رابط الاتصال باستخدام pymysql
DATABASE_URL = f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

# إنشاء محرك قاعدة البيانات
engine = create_engine(DATABASE_URL, echo=True)

# إعداد الجلسة
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# تعريف الأساس لإنشاء الجداول
Base = declarative_base()

# دالة لإرجاع الجلسة في كل طلب
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# اختبار الاتصال بقاعدة البيانات (اختياري)
try:
    with engine.connect() as connection:
        print("Connection to the database is successful!")
except Exception as e:
    print(f"Error: {e}")

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
import torch
import os

# تحديد مسار مجلد النموذج
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../model")

# تحميل التوكنرايزر والموديل المدرب
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

# تحديد الجهاز المناسب (GPU أو CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

# mapping للنتائج الرقمية → أسماء المشاعر
id2label = {
    0: "joy",
    1: "sadness",
    2: "anger",
    3: "fear",
    4: "surprise",
    5: "disgust",
    6: "neutral"
}

# دالة توقع المشاعر + الثقة
def predict_emotion(text: str) -> dict:
    # تجهيز الإدخال للنموذج
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # تنفيذ التنبؤ
    with torch.no_grad():
        outputs = model(**inputs)
        probs = softmax(outputs.logits, dim=1)
        predicted_class = torch.argmax(probs, dim=1).item()
        confidence = probs[0][predicted_class].item()

    return {
        "label": id2label[predicted_class],
        "confidence": confidence
    }

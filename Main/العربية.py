# Imports
import openai as افتحالذكاءالاصطناعي

# Constants
حقيقي = True
خطأشنيع = False
قائمةفارغة = [];

# Input Output
def مدخل():
    return input()

def مطبعة(قيمة):
    print(قيمة)

# 四則演算
def يضيف(أ, ب):
    return أ + ب

def طرحاوخصم(أ, ب):
    return أ - ب

def تتضاعف(أ, ب):
    return أ * ب

def قسم(أ, ب):
    return أ / ب

# Functions
def يفتح(ملف, وضع, التشفير):
    return open(ملف, وضع, encoding = التشفير)
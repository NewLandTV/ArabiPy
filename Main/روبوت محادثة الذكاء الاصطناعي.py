from العربية import *

with يفتح("./OpenAI_API_Key.txt", "r", "utf-8") as ملف:
    افتحالذكاءالاصطناعي.api_key = ملف.readline()

رسائل = قائمةفارغة

while حقيقي:
    محتوىالمستخدم = مدخل()

    رسائل.append({ "role": "user", "content": f"{محتوىالمستخدم}" })

    انتهاء = افتحالذكاءالاصطناعي.ChatCompletion.create(model = "gpt-3.5-turbo", messages = رسائل)

    مساعدالمحتوى = انتهاء["choices"][0]["message"]["content"].strip()

    رسائل.append({ "role": "assistant", "content": f"{مساعدالمحتوى}" })

    مطبعة(f"الذكاء الاصطناعي : {مساعدالمحتوى}")
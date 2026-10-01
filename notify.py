import os
import requests

def send_telegram_notify(message, token, chat_id):
    """ส่งข้อความผ่าน Telegram Bot"""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, json=payload)

def main():
    # กำหนดค่าพื้นที่และ % ฝนตก (สามารถเชื่อมต่อ API พยากรณ์อากาศจริง เช่น อุตุนิยมวิทยา ได้ที่จุดนี้)
    location = os.getenv("LOCATION", "ต.กกสะทอน อ.ด่านซ้าย จ.เลย")
    rain_chance = int(os.getenv("RAIN_CHANCE", "65")) # ดึงค่า % จากสภาพอากาศ หรือค่าที่ตั้งไว้

    # เงื่อนไขสร้างข้อความ
    if rain_chance >= 60:
        message = f"วันนี้พื้นที่ {location} มีโอกาสฝนตก {rain_chance}% แนะนำให้พกร่มครับ ☔"
    else:
        message = f"วันนี้พื้นที่ {location} มีโอกาสฝนตก {rain_chance}% ไม่ต้องพกร่มไปก็ได้ครับ ☀️"

    print(f"Generated Message: {message}")

    # ดึง Token สำหรับการแจ้งเตือนจาก Secrets
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if telegram_token and telegram_chat_id:
        send_telegram_notify(message, telegram_token, telegram_chat_id)
        print("ส่งแจ้งเตือนเรียบร้อยแล้ว")

if __name__ == "__main__":
    main()

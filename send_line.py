import os
import requests

def send_line_message(message, channel_access_token, user_id):
    """ส่งข้อความแจ้งเตือนผ่าน LINE Messaging API"""
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {channel_access_token}"
    }
    payload = {
        "to": user_id,
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("ส่งแจ้งเตือนเข้า LINE สำเร็จ!")
    else:
        print(f"เกิดข้อผิดพลาด: {response.status_code} - {response.text}")

def main():
    # รับค่าตำแหน่งและ % ฝนตกจาก environment variables
    location = os.getenv("LOCATION", "ต.กกสะทอน อ.ด่านซ้าย จ.เลย")
    
    try:
        rain_chance = int(os.getenv("RAIN_CHANCE", "65"))
    except ValueError:
        rain_chance = 0

    # เงื่อนไขการสร้างข้อความตามเงื่อนไขที่กำหนด
    if rain_chance >= 60:
        message = f"[{location}]\nวันนี้มีโอกาสฝนตก {rain_chance}% แนะนำให้พกร่มครับ ☔"
    else:
        message = f"[{location}]\nวันนี้มีโอกาสฝนตก {rain_chance}% ไม่ต้องพกร่มไปก็ได้ครับ ☀️"

    print(f"ข้อความที่จะส่ง: {message}")

    # ดึงค่า Keys จาก GitHub Secrets
    line_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    line_user_id = os.getenv("LINE_USER_ID")

    if line_access_token and line_user_id:
        send_line_message(message, line_access_token, line_user_id)
    else:
        print("กรุณาตั้งค่า LINE_CHANNEL_ACCESS_TOKEN และ LINE_USER_ID ใน Secrets")

if __name__ == "__main__":
    main()

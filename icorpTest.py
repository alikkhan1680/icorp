import requests
import json
import time

WEBHOOK_URL = "https://webhook.site/0b0a15c2-1178-4b82-81bd-5abaaf46534c"
API_URL = "https://test.icorp.uz/interview.php"
WEBHOOK_TOKEN = "0b0a15c2-1178-4b82-81bd-5abaaf46534c"
GET_URL = f"https://webhook.site/token/{WEBHOOK_TOKEN}/requests?sorting=newest"

def get_part1(msg):
    response = requests.post(API_URL, json={"msg": msg, "url": WEBHOOK_URL})
    return response.json()["part1"]

def wait_for_part2(get_url, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            data = requests.get(get_url).json()
            if data['data']:
                payload_webhook = json.loads(data['data'][0]['content'])
                part2 = payload_webhook.get('part2')
                if part2:
                    return part2
        except (json.JSONDecodeError, KeyError):
            pass
        time.sleep(1)
    return None

def main():
    msg_text = input("Payload uchun xabar kiriting: ").strip()
    part1 = get_part1(msg_text)

    part2 = wait_for_part2(GET_URL)
    if not part2:
        print("2-qism kodi kelmadi, tekshirib ko‘ring!")
        return

    combined_code = json.dumps({"part1": part1, "part2": part2})
    final_response = requests.get(API_URL, params={"code": combined_code})
    print("Final message:", final_response.text)

if __name__ == "__main__":
    main()

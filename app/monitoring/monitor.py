import requests
import time
from datetime import datetime

URL = "http://host.docker.internal:5000/health"

while True:
    try:
        response = requests.get(URL, timeout=5)

        if response.status_code == 200:
            print(f"[{datetime.now()}] ✅ Application is UP")

        else:
            print(f"[{datetime.now()}] ⚠️ Application returned status {response.status_code}")

    except requests.exceptions.RequestException:
        print(f"[{datetime.now()}] 🚨 INCIDENT: Application is DOWN")

    time.sleep(10)
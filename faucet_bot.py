import requests
import time
from datetime import datetime

url = "https://faucet.omni.network/base-sepolia?_data=routes%2Fbase-sepolia"
address = "0x30e25eaa01f60acf52470ccfc57cad3e245b43c9"

headers = {
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://faucet.omni.network",
    "Referer": "https://faucet.omni.network/base-sepolia",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}

data = f"account={address}"

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)

while True:
    log("🚀 Mengirim permintaan faucet...")
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        log("✅ Klaim berhasil atau diterima!")
        log(f"Respon: {response.text}")
    else:
        log(f"⚠️ Gagal klaim: {response.status_code}")
        log(f"Respon: {response.text}")

    log("🕒 Menunggu 3 jam untuk klaim berikutnya...\n")
    time.sleep(3 * 60 * 60)  # 3 jam

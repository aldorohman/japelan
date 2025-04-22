import requests
import time

url = "https://faucet.omni.network/base-sepolia?_data=routes%2Fbase-sepolia"
address = "0x30e25eaa01f60acf52470ccfc57cad3e245b43c9"

headers = {
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://faucet.omni.network",
    "Referer": "https://faucet.omni.network/base-sepolia",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}

data = f"account={address}"

while True:
    print("🚀 Mengirim permintaan faucet...")
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        print("✅ Klaim berhasil atau diterima!")
    else:
        print(f"⚠️ Gagal klaim: {response.status_code}")
        print(response.text)

    print("🕒 Menunggu 3 jam untuk klaim berikutnya...")
    time.sleep(3 * 60 * 60)  # 3 jam

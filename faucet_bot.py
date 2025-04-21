import requests
import time

# Ganti dengan URL faucet dan alamat kamu
FAUCET_URL = 'https://faucet.omni.network/base-sepolia'
MY_ADDRESS = '0xc741e8d3dbde1255e2961df114ccc66075c5a6d5'

def claim_faucet():
    try:
        data = {'address': MY_ADDRESS}
        response = requests.post(FAUCET_URL, json=data)
        
        if response.status_code == 200:
            print("✅ Klaim faucet berhasil:", response.json())
        else:
            print("❌ Gagal klaim:", response.status_code, response.text)
    except Exception as e:
        print("⚠️ Error saat klaim:", str(e))

# Loop terus-menerus setiap 3 jam
while True:
    print("🚀 Klaim faucet dimulai...")
    claim_faucet()
    print("⏳ Menunggu 3 jam sebelum klaim berikutnya...\n")
    time.sleep(3 * 60 * 60)  # 3 jam dalam detik

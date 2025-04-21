import requests
import schedule
import time

# Ganti dengan endpoint faucet dan EVM address kamu
FAUCET_URL = 'https://faucet.omni.network/base-sepolia'
MY_ADDRESS = '0xc741e8d3dbde1255e2961df114ccc66075c5a6d5'

def claim_faucet():
    try:
        data = {'address': MY_ADDRESS}
        response = requests.post(FAUCET_URL, json=data)
        
        if response.status_code == 200:
            print("✅ Faucet claimed:", response.json())
        else:
            print("❌ Gagal klaim:", response.status_code, response.text)
    except Exception as e:
        print("⚠️ Error:", str(e))

# Setiap 3 jam
schedule.every(3).hours.do(claim_faucet)

print("⏳ Bot aktif. Menunggu waktu klaim faucet...")
while True:
    schedule.run_pending()
    time.sleep(10)

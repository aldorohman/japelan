from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

CHROMEDRIVER_PATH = './chromedriver'  # atau path lengkap kalau di luar folder
FAUCET_URL = 'https://faucet.omni.network/base-sepolia'  # Ganti dengan URL faucet kamu
MY_ADDRESS = '0xc741e8d3dbde1255e2961df114ccc66075c5a6d5'

def claim_faucet():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # hilangkan ini kalau mau lihat browser-nya
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)

    try:
        driver.get(FAUCET_URL)

        # Ganti selector sesuai form faucet-nya
        address_input = driver.find_element(By.NAME, "address")
        address_input.send_keys(MY_ADDRESS)

        claim_button = driver.find_element(By.ID, "claimButton")
        claim_button.click()

        print("✅ Klaim berhasil!")
    except Exception as e:
        print("⚠️ Error:", str(e))
    finally:
        driver.quit()

# Loop setiap 3 jam
while True:
    print("🚀 Klaim faucet dimulai...")
    claim_faucet()
    print("⏳ Menunggu 3 jam...\n")
    time.sleep(3 * 60 * 60)

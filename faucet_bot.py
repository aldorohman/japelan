from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc

FAUCET_URL = "https://faucet.omni.network/base-sepolia"
CLAIM_INTERVAL = 3 * 60 * 60  # 3 hours in seconds

def claim_faucet():
    print("Launching browser...")
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = uc.Chrome(options=options)
    driver.get(FAUCET_URL)
    print("Opened faucet page.")

    time.sleep(10)  # Tunggu semua elemen termuat (atau bisa ditingkatkan dengan WebDriverWait)

    try:
        # Klik tombol connect wallet (jika ada)
        connect_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Connect Wallet')]")
        connect_btn.click()
        print("Clicked Connect Wallet")
        time.sleep(5)

        # Di sini kamu perlu manual connect MetaMask atau integrasikan MetaMask handler (kompleks dan berisiko)
        input("Silakan login wallet & authorize faucet (tekan Enter jika sudah)...")

        # Klik tombol Claim
        claim_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Claim')]")
        claim_btn.click()
        print("Clicked Claim Button")

        time.sleep(10)  # Tunggu transaksi selesai
        print("Claim successful (assuming no CAPTCHA)")

    except Exception as e:
        print(f"Error occurred: {e}")

    driver.quit()

if __name__ == "__main__":
    while True:
        claim_faucet()
        print(f"Waiting 3 hours for next claim...")
        time.sleep(CLAIM_INTERVAL)

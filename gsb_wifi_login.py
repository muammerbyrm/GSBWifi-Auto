import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

URL = "https://wifi.gsb.gov.tr/"
USERNAME = os.getenv("GSB_USERNAME")
PASSWORD = os.getenv("GSB_PASSWORD")

USERNAME_FIELD = (By.NAME, "j_username")
PASSWORD_FIELD = (By.NAME, "j_password")
LOGIN_BUTTON = (By.NAME, "submit")


def find_chromedriver():
    """Önce .env yolu, sonra drivers/ klasörü. Bulamazsa None (Selenium Manager devreye girer)."""
    env_path = os.getenv("CHROMEDRIVER_PATH")
    if env_path and Path(env_path).is_file():
        return str(Path(env_path))

    exe_name = "chromedriver.exe" if os.name == "nt" else "chromedriver"
    local = BASE_DIR / "drivers" / exe_name
    if local.is_file():
        return str(local)

    return None


def create_driver():
    driver_path = find_chromedriver()
    if driver_path:
        print(f"   Yerel chromedriver kullanılıyor: {driver_path}")
        return webdriver.Chrome(service=Service(executable_path=driver_path))

    print("   Yerel chromedriver bulunamadı, otomatik indirme deneniyor (internet gerekir)...")
    return webdriver.Chrome()


def main():
    if not USERNAME or not PASSWORD:
        sys.exit("HATA: .env dosyasında GSB_USERNAME ve GSB_PASSWORD tanımlı olmalı.")

    driver = None
    try:
        print("1) Chrome başlatılıyor...")
        driver = create_driver()
        wait = WebDriverWait(driver, 10)

        print(f"2) Sayfa açılıyor: {URL}")
        driver.get(URL)
        print("   Sayfa başlığı:", driver.title)

        print("3) Kullanıcı adı yazılıyor...")
        user_input = wait.until(EC.presence_of_element_located(USERNAME_FIELD))
        user_input.clear()
        user_input.send_keys(USERNAME)

        print("4) Şifre yazılıyor...")
        pass_input = driver.find_element(*PASSWORD_FIELD)
        pass_input.clear()
        pass_input.send_keys(PASSWORD)

        print("5) Giriş butonuna tıklanıyor...")
        driver.find_element(*LOGIN_BUTTON).click()
        time.sleep(2)
        print("   Giriş denemesi tamamlandı.")

    except Exception as e:
        print("HATA OLUŞTU:", repr(e))

    finally:
        input("Tarayıcıyı kapatmak için Enter'a bas...")
        if driver:
            driver.quit()


if __name__ == "__main__":
    main()
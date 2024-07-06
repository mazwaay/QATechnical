import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-popup-blocking')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_searching_with_irrelevant_keywords(browser):
    website = "https://shop.bukuerlangga.com/"
    browser.get(website)

    search_bar = browser.find_element(By.NAME, "judul")
    search_bar.send_keys("sepeda listrik" + Keys.ENTER)

    time.sleep(5)
    
    try:
        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h4"), "Data Tidak Ditemukan"))
        print("Teks 'Data Tidak Ditemukan' ditemukan pada tag h4.")
    except TimeoutException:
        print("Teks 'Data Tidak Ditemukan' tidak ditemukan pada tag h5 dalam waktu 10 detik.")

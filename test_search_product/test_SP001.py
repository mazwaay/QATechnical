import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

def test_login_with_valid_data(browser):
    website = "https://shop.bukuerlangga.com/"
    browser.get(website)

    search_bar = browser.find_element(By.NAME, "judul")
    search_bar.send_keys("phintar" + Keys.ENTER)

    time.sleep(5)
    
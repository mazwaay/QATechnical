import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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

def test_login_with_empty_password(browser):
    website = "https://shop.bukuerlangga.com/"
    browser.get(website)

    button_masuk = browser.find_element(By.LINK_TEXT, "Masuk")
    button_masuk.click()

    email = browser.find_element(By.ID, "identity")
    password = browser.find_element(By.ID, "password")
    button_login = browser.find_element(By.ID, "slogin")

    email.send_keys("mazway.testing@gmail.com")
    password.send_keys("")
    button_login.click()

    time.sleep(5)

    error_message = browser.find_element(By.CSS_SELECTOR, ".text-danger.ifmessage-password")
    assert "The Password field is required." in error_message.text, "Pesan kesalahan tidak sesuai atau tidak ditemukan"

def test_login_with_empty_email(browser):
    website = "https://shop.bukuerlangga.com/"
    browser.get(website)

    button_masuk = browser.find_element(By.LINK_TEXT, "Masuk")
    button_masuk.click()

    email = browser.find_element(By.ID, "identity")
    password = browser.find_element(By.ID, "password")
    button_login = browser.find_element(By.ID, "slogin")

    email.send_keys("")
    password.send_keys("anakjaman1")
    button_login.click()

    time.sleep(5)

    error_message = browser.find_element(By.CSS_SELECTOR, ".text-danger.ifmessage-identity")
    assert "The Identity field is required." in error_message.text, "Pesan kesalahan tidak sesuai atau tidak ditemukan"

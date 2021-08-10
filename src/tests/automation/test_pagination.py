import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_logout():

    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')

    name = "testuser1"
    email = name + "@example.com"
    pw = "Abcd123$"

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("http://localhost:1667/#/login")
    time.sleep(5)
    driver.find_element_by_css_selector(
        "#app > div > div > div > div > form > fieldset:nth-child(1) > input").send_keys(email)
    driver.find_element_by_css_selector(
        "#app > div > div > div > div > form > fieldset:nth-child(2) > input").send_keys(pw)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > button").click()

    time.sleep(5)

    driver.find_element_by_css_selector("#app > nav > div > ul > li:nth-child(5) > a").click()
    time.sleep(5)
    assert len(driver.find_elements_by_css_selector("#app > nav > div > ul > li:nth-child(5) > a")) == 0

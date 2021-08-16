import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# TC 02 - Bejelentkezés vizsgálata, a teszt a bejelentkezés utáni,
# főoldalra történő visszairányítást tekinti sikeres esetnek.
def test_login():

    name = "testuser1"
    email = name + "@example.com"
    pw = "Abcd123$"

    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("http://localhost:1667/#/login")
    time.sleep(5)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(1) > input").send_keys(email)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(2) > input").send_keys(pw)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > button").click()

    time.sleep(5)
    assert driver.current_url == "http://localhost:1667/#/"

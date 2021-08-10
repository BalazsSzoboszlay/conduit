import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def test_editdata():

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
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(1) > input").send_keys(email)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(2) > input").send_keys(pw)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > button").click()

    time.sleep(5)

    driver.get("http://localhost:1667/#/editor")
    time.sleep(5)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input").clear()
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input").send_keys("Title8" + str(time.time()))
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(2) > input").send_keys("Subtitle1")
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(3) > textarea").send_keys("Message")

    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(4) > div > div > ul > li > input").send_keys("Testtag")
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(4) > div > div > ul > li > input").send_keys(Keys.RETURN)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > button").click()
    time.sleep(5)

    driver.find_element_by_css_selector("#app > div > div.banner > div > div > span > a").click()
    time.sleep(5)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input").clear()
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input").send_keys("modified title")

    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(2) > input").clear()
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(2) > input").send_keys("modified")
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(3) > textarea").clear()
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(3) > textarea").send_keys("modified")
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(4) > div > div > ul > li > input").clear()
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(4) > div > div > ul > li > input").send_keys("modified")
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(4) > div > div > ul > li > input").send_keys(Keys.RETURN)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > button").click()
    time.sleep(5)

    assert driver.find_element_by_css_selector("#app > div > div.banner > div > h1").text == "modified title"
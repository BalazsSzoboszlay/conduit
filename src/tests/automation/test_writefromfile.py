import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def addnewdata(driver, intitle, inabout, inmessage, intags):
    driver.find_element_by_css_selector("#app > nav > div > ul > li:nth-child(2) > a").click()
    time.sleep(5)

    # app > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input").clear()
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input").send_keys(intitle)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(2) > input").send_keys(inabout)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(3) > textarea").send_keys(inmessage)

    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(4) > div > div > ul > li > input").send_keys(intags)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(4) > div > div > ul > li > input").send_keys(Keys.RETURN)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > button").click()
    time.sleep(5)


# Bemeneti tesztadatok megadása külső fájlból.
# A teszt a saját mappájában megtalálható input.txt fájlból várja a tesztadatokat.
def test_writefromfile():
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

    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'input.txt')

    with open(filename) as file:
        content = file.readlines()
        content = [x.strip() for x in content]

    time.sleep(5)
    addnewdata(driver, content[0], content[1], content[2], content[3])
    time.sleep(5)
    addnewdata(driver, content[4], content[5], content[6], content[7])
    print(os.path.dirname(os.path.realpath(__file__)))
    assert driver.current_url == "http://localhost:1667/#/articles/title-7"

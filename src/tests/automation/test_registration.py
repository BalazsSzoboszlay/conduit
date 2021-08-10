import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Regisztráció tesztelése, a teszt a mappájában található counter.txt fájlból szed sorszámot és
# eggyel megnövelve felül is írja
def testregistration():

    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'counter.txt')

    file = open(filename, 'r')
    temp = int(file.readline())
    file.close()

    name = "user" + str(temp)
    email = name + "@example.com"
    pw = "Abcd123$"
    temp += 1
    file2 = open(filename, 'w')
    file2.write(str(temp))
    file2.close()

    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("http://localhost:1667/#/register")
    time.sleep(5)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(1) > input").send_keys(name)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(2) > input").send_keys(email)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(3) > input").send_keys(pw)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > button").click()
    time.sleep(5)
    assert driver.current_url == "http://localhost:1667/#/"

import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_listallelements():

    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)

    if os.path.exists("output.txt"):
        os.remove("output.txt")

    name = "testuser1"
    email = name + "@example.com"
    pw = "Abcd123$"

    driver.get("http://localhost:1667/#/login")
    time.sleep(3)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(1) > input").send_keys(email)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(2) > input").send_keys(pw)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > button").click()

    time.sleep(3)

    driver.get("http://localhost:1667/#/")
    time.sleep(5)
    text = ""
    n = range(10)
    for x in n:
        # print("aa: " + str(x))
        text += "\n" + driver.find_elements_by_class_name("article-meta").__getitem__(x).text
        text += "\n" + driver.find_elements_by_class_name("preview-link").__getitem__(x).text
        text += "\n------------"
        #  print(len(driver.find_elements_by_class_name("article-meta")))

    file = open('output.txt', 'w')
    file.write(text)
    file.close()

    assert os.path.exists("output.txt")
    assert os.stat("output.txt").st_size > 0

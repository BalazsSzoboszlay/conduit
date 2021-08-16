import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

counter = 0


def listallelements(driver):
    time.sleep(5)
    text = ""
    n = range(len(driver.find_elements_by_class_name("article-meta")))
    for x in n:
        # print("aa: " + str(x))
        global counter
        counter += 1
        text += "\n" + driver.find_elements_by_class_name("article-meta").__getitem__(x).text
        text += "\n" + driver.find_elements_by_class_name("preview-link").__getitem__(x).text
        text += "\n------------"

# TC 05 - Lapozás vizsgálata, a teszt feltételezi,
# hogy több lap van és a lapozó felület látható és kattintható.
def test_pagination():
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
    i = 1
    driver.get("http://localhost:1667/#/")
    n = range(1)

    for x in n:
        print("oldal száma: " + str(i))
        listallelements(driver)
        driver.find_elements_by_class_name("page-link").__getitem__(i).click()
        i += 1

    assert counter > 10

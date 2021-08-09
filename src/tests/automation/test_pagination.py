import time

from selenium import webdriver

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


def test_pagination():
    name = "user33"
    email = name + "@hotmail.com"
    pw = "Userpass1"

    driver = webdriver.Chrome("driver/chromedriver")

    driver.get("http://localhost:1667/#/login")
    time.sleep(3)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(1) > input").send_keys(email)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(2) > input").send_keys(pw)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > button").click()

    time.sleep(3)
    i = 1
    driver.get("http://localhost:1667/#/")
    n = range(1)

    for x in n:
        print("oldal száma: " + str(i))
        listallelements(driver)
        driver.find_elements_by_class_name("page-link").__getitem__(i).click()
        i += 1

    assert counter > 10
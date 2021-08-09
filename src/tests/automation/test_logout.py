import time

from selenium import webdriver

def test_logout():
    file = open('counter.txt', 'r')
    temp = int(file.readline())
    file.close()

    name = "user33"
    email = name + "@hotmail.com"
    pw = "Userpass1"
    temp += 1
    file2 = open('counter.txt', 'w')
    file2.write(str(temp))
    file2.close()

    driver = webdriver.Chrome("driver/chromedriver")

    driver.get("http://localhost:1667/#/login")
    time.sleep(3)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(1) > input").send_keys(email)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(2) > input").send_keys(pw)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > button").click()

    time.sleep(3)

    driver.find_element_by_css_selector("#app > nav > div > ul > li:nth-child(5) > a").click()
    time.sleep(2)
    assert len(driver.find_elements_by_css_selector("#app > nav > div > ul > li:nth-child(5) > a")) == 0
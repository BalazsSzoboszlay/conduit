import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def addnewdata(driver, intitle, inabout, inmessage, intags):

    driver.find_element_by_css_selector("#app > nav > div > ul > li:nth-child(2) > a").click()
    time.sleep(3)

    # app > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input").clear()
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input").send_keys(intitle)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(2) > input").send_keys(inabout)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(3) > textarea").send_keys(inmessage)

    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(4) > div > div > ul > li > input").send_keys(intags)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(4) > div > div > ul > li > input").send_keys(Keys.RETURN)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > button").click()
    time.sleep(3)


def test_writefromfile():
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

    with open("input.txt") as file:
        content = file.readlines()
        content = [x.strip() for x in content]

    time.sleep(5)
    addnewdata(driver, content[0], content[1], content[2], content[3])
    time.sleep(5)
    addnewdata(driver, content[4], content[5], content[6], content[7])

    assert driver.current_url == "http://localhost:1667/#/articles/title-7"

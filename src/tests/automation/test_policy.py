import time

from selenium import webdriver
def test_policy():

    driver = webdriver.Chrome("driver/chromedriver")
    driver.get("http://localhost:1667/#/")
    driver.delete_all_cookies()
    time.sleep(2)
    assert driver.find_element_by_css_selector("#cookie-policy-panel > div > div.cookie__bar__buttons > button.cookie__bar__buttons__button.cookie__bar__buttons__button--accept").is_displayed()
    driver.find_element_by_css_selector("#cookie-policy-panel > div > div.cookie__bar__buttons > button.cookie__bar__buttons__button.cookie__bar__buttons__button--accept").click()
    time.sleep(2)
    assert driver.get_cookie("vue-cookie-accept-decline-cookie-policy-panel") is not None
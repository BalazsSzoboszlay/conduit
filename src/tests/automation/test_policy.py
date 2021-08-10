import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Adatvédelmi nyilatkozat elfogadás/elutasítás tesztelése, a teszt a panel meglétét,
# majd az elfogadásra kattintáskor a panel eltűnését vizsgálja.
def test_policy():
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://localhost:1667/#/")
    driver.delete_all_cookies()
    time.sleep(5)
    assert driver.find_element_by_css_selector("#cookie-policy-panel > div > div.cookie__bar__buttons > button.cookie__bar__buttons__button.cookie__bar__buttons__button--accept").is_displayed()
    driver.find_element_by_css_selector("#cookie-policy-panel > div > div.cookie__bar__buttons > button.cookie__bar__buttons__button.cookie__bar__buttons__button--accept").click()
    time.sleep(5)
    assert driver.get_cookie("vue-cookie-accept-decline-cookie-policy-panel") is not None
"""Работа с явными ожиданиями"""

from selenium import webdriver
from formula import formula
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    button = browser.find_element_by_id('book')

    text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button.click()
    ans = formula(int(browser.find_element_by_id('input_value').text))
    browser.find_element_by_id('answer').send_keys(str(ans))
    browser.find_element_by_id('solve').click()
    sleep(10)

finally:
    browser.quit()

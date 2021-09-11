from selenium import webdriver
from time import sleep
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element_by_class_name('btn').click()
    windows = browser.window_handles
    browser.switch_to.window(windows[1])

    txts = browser.find_elements_by_css_selector('label .nowrap')
    form = txts[0].text.replace('What is ', '').replace(', where x =', '')
    # print(form)
    val = int(txts[1].text)
    # print(val)
    ans = math.log(abs(12 * math.sin(val)))
    browser.find_element_by_class_name('form-control').send_keys(str(ans))
    browser.find_element_by_class_name('btn').click()
    sleep(10)

finally:
    browser.quit()


from selenium import webdriver
from formula import formula

driver = webdriver.Chrome()
try:
    driver.get('http://suninjuly.github.io/get_attribute.html')
    atr = driver.find_element_by_id('treasure').get_attribute('valuex')
    ans = str(formula(int(atr)))
    driver.find_element_by_id('answer').send_keys(ans)
    driver.find_element_by_id('robotCheckbox').click()
    driver.find_element_by_id('robotsRule').click()
    driver.find_element_by_class_name('btn').click()

finally:
    driver.quit()

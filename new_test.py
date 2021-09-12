import unittest
from selenium import webdriver
import time
#
#
# driver = webdriver.Chrome()
# try:
#     driver.get('http://suninjuly.github.io/registration2.html')
#     driver.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys('Ivan')
#     driver.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys('Petrov')
#     driver.find_element_by_css_selector('[placeholder="Input your email"]').send_keys('ivan@petrov')
#
#     btn = driver.find_element_by_css_selector('button.btn')
#     btn.click()
#     time.sleep(1)
#     welcome_text_elt = driver.find_element_by_tag_name('h1')
#     welcome_text = welcome_text_elt.text
#     assert welcome_text == 'Congratulations! You have successfully registered!'
#     # self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!')
# finally:
#     driver.quit()
class TestStep(unittest.TestCase):
    def test_registration1(self):
        driver = webdriver.Chrome()
        driver.get('http://suninjuly.github.io/registration1.html')
        driver.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys('Ivan')
        driver.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys('Petrov')
        driver.find_element_by_css_selector('[placeholder="Input your email"]').send_keys('ivan@petrov')
        btn = driver.find_element_by_css_selector('button.btn')
        btn.click()
        time.sleep(1)
        welcome_text_elt = driver.find_element_by_tag_name('h1')
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!')
        driver.quit()

    def test_registration2(self):
        driver = webdriver.Chrome()
        driver.get('http://suninjuly.github.io/registration2.html')
        driver.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys('Ivan')
        driver.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys('Petrov')
        driver.find_element_by_css_selector('[placeholder="Input your email"]').send_keys('ivan@petrov')
        btn = driver.find_element_by_css_selector('button.btn')
        btn.click()
        time.sleep(1)
        welcome_text_elt = driver.find_element_by_tag_name('h1')
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!')
        driver.quit()


if __name__ == '__main__':
    unittest.main()

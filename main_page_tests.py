#-*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

name = "Ciocia Krysia"
email = "mojemail.com"
witryna = "http://strona-krysi.pl"
komentarz = "Pyszne danie! Robie je raz w tygodniu na obiad!"

class MyClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_adding_comment(self):
        driver = self.driver
        driver.get("http://gotuj-z-iza.cba.pl")
        first_post = driver.find_element_by_css_selector("#post-101 > a > img")
        first_post.click()
        podpis_field = driver.find_element_by_css_selector("#author")
        podpis_field.send_keys(name)
        email_field = driver.find_element_by_css_selector("#email")
        email_field.send_keys(email)
        witryna_field = driver.find_element_by_css_selector("#url")
        witryna_field.send_keys(witryna)
        komentarz_field = driver.find_element_by_css_selector("#comment")
        komentarz_field.send_keys(komentarz)
        add_button = driver.find_element_by_css_selector("#submit")
        add_button.click()

        error = WebDriverWait(driver, 1, driver.find_element_by_css_selector('#error-page'))
        driver.quit()

        



if __name__ == "__main__":
    unittest.main()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.config import BASE_URL


class ContactPage(BasePage):
    SUBMIT_BTN = (By.XPATH, '//button[@type="submit"]')
    CONTACT_FORM = (By.XPATH, '//*[normalize-space()="Ask Us Anything"]/..//form')

    FIRST_NAME = (By.XPATH, '(//*[@aria-required="true"]/../..//label)[2]')
    LAST_NAME = (By.XPATH, '(//*[@aria-required="true"]/../..//label)[3]')
    EMAIL = (By.XPATH, '(//*[@aria-required="true"]/../..//label)[4]')
    PHONE = (By.XPATH, '(//*[@aria-required="true"]/../..//label)[5]')
    HOW_DID = (By.XPATH, '(//*[@aria-required="true"]/../..//label[contains(text(),"*")])[6]')
    CHECKBOX = (By.XPATH, '//div[@class="checkbox"]//*[@aria-required="true"]/../label')
    MANDATORY_FIELDS = [FIRST_NAME, LAST_NAME, EMAIL, PHONE, HOW_DID, CHECKBOX]
    red_color = '#FF4D40'

    def click_submit_btn(self):
        btn = self.driver.find_element(*self.SUBMIT_BTN)
        btn.click()

    def get_field_color(self, field):
        contact_form = self.driver.find_element(*self.CONTACT_FORM)
        hex_color = self.get_element_color(field)
        if hex_color == self.red_color:
            return "Red"
        else:
            return "White"













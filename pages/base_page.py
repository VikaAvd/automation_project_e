from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.utils import rgba_to_hex


class BasePage:
    COOKIES_BTN = (By.XPATH, '//*[text()="Accept All"]')
    CONTACT_US_BTN = (By.XPATH, '(//*[.=" CONTACT US"]/..)[2]')

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def close_browser(self):
        self.driver.quit()

    def get_page_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title

    def click_accept_cookies(self):
        btn = self.driver.find_element(*self.COOKIES_BTN)
        btn.click()

    def click_contact_us_btn(self):
        btn = self.driver.find_element(*self.CONTACT_US_BTN)
        btn.click()

    def scroll_to_web_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # or use next !!
        # element.location_once_scrolled_into_view

    def get_element_color(self, locator):
        element = self.driver.find_element(*locator)
        element_color = element.value_of_css_property("color")
        # print(element.text)
        return rgba_to_hex(str(element_color))
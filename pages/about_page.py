import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.config import BASE_URL


class AboutPage(BasePage):
    ABOUT_PAGE_URL = f'{BASE_URL}/about'
    EXPECTED_FILE_NAME = "EPAM_Corporate_Overview_Q3_october.pdf"
    LOGO = (By.XPATH, '//*[contains(@class,"header__logo-container desktop-logo")]')
    DOWNLOAD_BTN = (By.XPATH, '//*[@id="main"]/div[1]/div[5]/section/div[2]/div/div/div[1]/div/div[3]/div/a/span')
    #DOWNLOAD_BTN = (By.XPATH, '//div[normalize-space()="EPAM at a Glance"]/..//a[ @class="button-ui-23 btn-focusable"]')

    def open_about_page(self):
        self.open_url(self.ABOUT_PAGE_URL)

    def click_epam_logo(self):
        logo =  self.driver.find_element(*self.LOGO)
        logo.click()

    def scroll_to_web_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # or use next !!
        # element.location_once_scrolled_into_view

    def get_and_wait_element_is_clickable(self, element):
        wait = WebDriverWait(self.driver, 10)  # adjust the wait time as needed
        return wait.until(EC.element_to_be_clickable(*element))

    def click_download_button(self):
        wait = WebDriverWait(self.driver, 10)  # adjust the wait time as needed
        button = wait.until(EC.element_to_be_clickable(self.DOWNLOAD_BTN ))
        # button.location_once_scrolled_into_view
        self.scroll_to_web_element(button)
        time.sleep(2)
        button.click()








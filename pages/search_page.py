import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_BTN = '//span[.="Search"]/..'
    SEARCH_FIELD = '//input[@name="q" and @type="search"] '
    SEARCH_RESULT_COUNTER = '//h2[@class="search-results__counter"]'

    def search_with(self, search_text):
        search_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SEARCH_BTN))
        )
        search_btn.click()
        time.sleep(1)
        search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SEARCH_FIELD))
        )
        search_field.send_keys("AI" + Keys.RETURN)
        # time.sleep(1)

    def get_search_result_count(self):
        result_counter = self.driver.find_element(By.XPATH, self.SEARCH_RESULT_COUNTER)

        if not result_counter.text.strip():
            return 0
        else:
            return int(result_counter.text.split()[0])




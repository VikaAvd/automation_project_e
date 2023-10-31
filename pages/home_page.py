from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.utils import rgba_to_hex

class HomePage(BasePage):

    POLICIES_TITLE = (By.XPATH, '//h2[.="policies"]')
    POLICIES_ITEM = (By.XPATH, '//h2[.="policies"]/..//a[@class="fat-links"]')
    UKRAINE_BTN = (By.XPATH, '//*[@class="location-selector__panel"]/ul/li/a[@lang="uk"]')
    LANG_BTN = (By.XPATH, '(//*[@class="mobile-location-selector__button-section"]/button)[2]')
    THEME_BTN = (By.XPATH, '(//*[@class="theme-switcher-ui"]/*/div[@class="switch"])[2]')
    THEME_MODE = (By.XPATH, '//header')
    LOCATION_BLOCK = (By.XPATH, '(//div[@class="section__wrapper section--padding-no "])[9]')
    TAB_ITEMS = (By.XPATH, '//div[@role="tablist"]/div/a[@role="tab"]')
    TAB_ITEM = (By.XPATH, '//a[@role="tab" and text()="%s"]')


    def get_policy_title(self):
        policies_title = self.driver.find_element(*self.POLICIES_TITLE)
        self.driver.execute_script("arguments[0].scrollIntoView();", policies_title)
        return policies_title.text

    def get_policies_list(self):
        policies_list = self.driver.find_elements(*self.POLICIES_ITEM)
        actual_policies = []
        # Iterate through each <li> element and extract text from the <a> tag
        for element in policies_list:
            actual_policies.append(element.text)
        return actual_policies

    def switch_language(self):
        lang_btn = self.driver.find_element(*self.LANG_BTN)
        lang_btn.click()

        ukraine_btn = self.driver.find_element(*self.UKRAINE_BTN)
        ukraine_btn.click()

    def switch_theme(self):
        lang_btn = self.driver.find_element(*self.THEME_BTN)
        lang_btn.click()

    def get_theme_mode(self):
        header_area = self.driver.find_element(*self.THEME_MODE)
        header_color = header_area.value_of_css_property("color")
        hex_color = rgba_to_hex(str(header_color))
        if hex_color == '#231F20':
            return 'Dark Mode'
        elif hex_color == '#000000':
            return 'Light Mode'

    def get_regions_list(self):
        items_list = self.driver.find_elements(*self.TAB_ITEMS)
        # print(f"len(items_list) = {len(items_list)}")
        items = []
        for element in items_list:
            items.append(element.text)
            # print(element.text)
        # print("items= ", items)
        return items

    def regions_is_selected(self,  region_name=None):
        locator = (self.TAB_ITEM[0], self.TAB_ITEM[1] % region_name)
        region_tab = self.driver.find_element(*locator)

        actions = ActionChains(self.driver)
        actions.move_to_element(region_tab).perform()
        region_tab.click()
        return True






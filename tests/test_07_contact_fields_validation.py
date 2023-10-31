import time
import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.contact_page import ContactPage
from utils.config import BASE_URL, BROWSER, IMPLICIT_TIMEOUT


class TestFormValidation(unittest.TestCase):

    def setUp(self):
        drivers = {
            "chrome": webdriver.Chrome,
            "firefox": webdriver.Firefox
        }

        if BROWSER in drivers:
            self.driver = drivers[BROWSER]()
        else:
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICIT_TIMEOUT)

    def test_form_validation(self):
        home_page = HomePage(self.driver)
        home_page.open_url(BASE_URL)
        home_page.click_accept_cookies()
        home_page.click_contact_us_btn()

        contact_page = ContactPage(self.driver)
        contact_page.click_submit_btn()

        expected_color = "Red"
        for field in contact_page.MANDATORY_FIELDS:
            actual_color = contact_page.get_field_color(field)
            print("actual_color / field", actual_color, field)
            self.assertEqual(actual_color, expected_color,
                             f"Warning color mismatch. Actual: {actual_color}, Expected: {expected_color} color for {field[1]}")


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

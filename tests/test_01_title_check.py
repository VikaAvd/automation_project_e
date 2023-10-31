import unittest
import pytest
from selenium import webdriver
from pages.home_page import HomePage
from utils.config import BASE_URL, BROWSER, IMPLICIT_TIMEOUT


class TestTitle(unittest.TestCase):
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

    def test_check_epam_title(self):
        home_page = HomePage(self.driver)
        home_page.open_url(BASE_URL)
        home_page.click_accept_cookies()

        expected_title = "EPAM | Software Engineering & Product Development Services"
        actual_title = home_page.get_page_title()

        self.assertEqual(actual_title, expected_title,
                         f"Title mismatch. Actual: {actual_title}, Expected: {expected_title}")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

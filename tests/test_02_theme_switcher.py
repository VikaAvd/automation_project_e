import time
import unittest
from selenium import webdriver
from pages.home_page import HomePage
from utils.config import BASE_URL, BROWSER, IMPLICIT_TIMEOUT


class TestThemeSwitcher(unittest.TestCase):
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

    def test_theme_switching(self):
        home_page = HomePage(self.driver)
        home_page.open_url(BASE_URL)

        home_page.switch_theme()
        self.driver.implicitly_wait(IMPLICIT_TIMEOUT)

        actual_theme_mode = home_page.get_theme_mode()
        expected_theme_mode = 'Light Mode'

        self.assertEqual(actual_theme_mode, expected_theme_mode,
                         f"Theme mode mismatch. Actual: {actual_theme_mode}, Expected: {expected_theme_mode}")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

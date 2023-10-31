import time
import unittest
from selenium import webdriver
from pages.about_page import AboutPage
from utils.config import BASE_URL, BROWSER, IMPLICIT_TIMEOUT

class TestLogoLink(unittest.TestCase):
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

    def test_check_logo_link(self):
        about_page = AboutPage(self.driver)
        about_page.open_url(f"{BASE_URL}/about")

        about_page.click_epam_logo()
        actual_url = about_page.get_page_url()

        expected_url =  "www.epam.com"
        self.assertIn( expected_url, actual_url,
                         f"Page mismatch. Actual: {actual_url}, Expected: {expected_url}")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

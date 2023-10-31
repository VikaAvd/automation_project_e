import time
import unittest
from selenium import webdriver
from pages.home_page import HomePage
from utils.config import BASE_URL, BROWSER, IMPLICIT_TIMEOUT


class TestLocationBox(unittest.TestCase):
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

    def test_check_Location_refions(self):
        home_page = HomePage(self.driver)
        home_page.open_url(BASE_URL)
        home_page.click_accept_cookies()

        expected_regions = ['AMERICAS', 'EMEA', 'APAC']
        actual_regions = home_page.get_regions_list()
        self.assertListEqual(expected_regions, actual_regions,
                             f"regions list mismatch. Actual: {actual_regions}, Expected: {expected_regions}")

        for region in expected_regions:
            assert home_page.regions_is_selected(region) is True, f"The {region} regions was not selected"
        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

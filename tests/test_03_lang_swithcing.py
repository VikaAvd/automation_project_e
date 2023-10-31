import time
import unittest
from selenium import webdriver
from pages.home_page import HomePage
from utils.config import BASE_URL, BROWSER, IMPLICIT_TIMEOUT


class TestLangSwitcher(unittest.TestCase):
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

    def test_change_language_to_ua(self):
        home_page = HomePage(self.driver)
        home_page.open_url(BASE_URL)

        home_page.switch_language()
        time.sleep(10)

        actual_title = home_page.get_page_title()
        print(f"###{actual_title}###")
        expected_ua_title = 'EPAM Ukraine - найбільша ІТ-компанія в Україні | Вакансії'

        self.assertEqual(actual_title, expected_ua_title,
                         f"Opened page location mismatch. Actual: {actual_title}, Expected: {expected_ua_title}")
        assert "найбільша ІТ-компанія в Україні" in actual_title
        # Some time this TC is failing due to getting empty header on https://careers.epam.ua/

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

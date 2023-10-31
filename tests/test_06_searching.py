import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.search_page import SearchPage
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

    def test_check_searching(self):
        home_page = HomePage(self.driver)
        home_page.open_url(BASE_URL)
        home_page.click_accept_cookies()
        search_page = SearchPage(self.driver)
        search_text = "AI"
        search_page.search_with(search_text)
        count = search_page.get_search_result_count()
        self.assertTrue(count > 0,
                         f" Fails while expected found something about: {search_text}")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.about_page import AboutPage
from utils.config import BROWSER, DOWNLOAD_DIR, IMPLICIT_TIMEOUT, BASE_URL
from utils.utils import clear_downloaded_file_by_name


class TestReportDownload(unittest.TestCase):

    def setUp(self):
        drivers = {
            "chrome": webdriver.Chrome,
            "firefox": webdriver.Firefox
        }

        if BROWSER in drivers:
            self.driver = drivers[BROWSER]()
        else:
            self.driver = webdriver.Chrome()

        self.download_dir = DOWNLOAD_DIR
        os.makedirs(self.download_dir, exist_ok=True)
        self.download_dir = os.path.abspath(self.download_dir)


        if BROWSER == "chrome":
            chrome_options = Options()
            prefs = {"download.default_directory": self.download_dir}
            chrome_options.add_experimental_option("prefs", prefs)
            self.driver = webdriver.Chrome(options=chrome_options)

        elif BROWSER == "firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.dir", self.download_dir)

        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICIT_TIMEOUT)

    def test_report_downloading(self):
        about_page = AboutPage(self.driver)
        clear_downloaded_file_by_name(DOWNLOAD_DIR, about_page.EXPECTED_FILE_NAME)

        about_page.open_about_page()
        about_page.open_url(f"{BASE_URL}/about")
        about_page.click_accept_cookies()
        self.driver.get('https://www.epam.com/about')
        time.sleep(5)
        about_page.click_download_button()
        # wait for the download to complete
        time.sleep(15)  # adjust this value based on your internet speed

        # check if the file is downloaded
        expected_file = os.path.join(self.download_dir, about_page.EXPECTED_FILE_NAME)
        self.assertTrue(os.path.exists(expected_file), "File not found!")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

import unittest
from selenium import webdriver
from pages.home_page import HomePage
from utils.config import BASE_URL, BROWSER, IMPLICIT_TIMEOUT

class TestPolicies(unittest.TestCase):
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

    def test_check_epam_policies(self):
        home_page = HomePage(self.driver)
        home_page.open_url(BASE_URL)

        expected_policy_title = 'POLICIES'
        expected_policies = ['INVESTORS', 'OPEN SOURCE', 'PRIVACY POLICY', 'COOKIE POLICY', 'APPLICANT PRIVACY NOTICE',
            'WEB ACCESSIBILITY']

        actual_policy_title = home_page.get_policy_title()
        self.assertEqual(actual_policy_title, expected_policy_title,
                         f"Policy mismatch. Actual: {actual_policy_title}, Expected: {expected_policy_title}")
        actual_policies = home_page.get_policies_list()
        self.assertListEqual(actual_policies, expected_policies,
                         f"Policies list mismatch. Actual: {actual_policies}, Expected: {expected_policies}")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

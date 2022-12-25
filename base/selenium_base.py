from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.login_input_element = 'log_inputEmail'
        self.pass_input_element = 'log_inputPassword'
        self.auth_btn = 'AuthButton'

    @staticmethod
    def get_selenium_by(find_by):
        locating = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'id': By.ID,
            'cls_name': By.CLASS_NAME,
            'name': By.NAME,
            'text': By.LINK_TEXT
        }
        return locating[find_by]

    def is_visible(self, find_by, locator) -> WebElement:
        """Wait and return WebElement if visible"""
        return self.wait.until(ec.visibility_of_element_located((self.get_selenium_by(find_by=find_by),
                                                                 locator)))

    def is_present(self, find_by, locator) -> WebElement:
        """Waiting and returning a WebElement if present in the DOM"""
        return self.wait.until(ec.presence_of_element_located((self.get_selenium_by(find_by=find_by),
                                                               locator)))

    def is_not_present(self, find_by, locator) -> WebElement:
        """Waiting for an element to disappear"""
        return self.wait.until(ec.invisibility_of_element_located((self.get_selenium_by(find_by=find_by),
                                                                   locator)))

    def are_visible(self, find_by, locator) -> List[WebElement]:
        """Waiting and returning WebElements if they are visible"""
        return self.wait.until(ec.visibility_of_all_elements_located((self.get_selenium_by(find_by=find_by),
                                                                      locator)))

    def are_present(self, find_by, locator) -> List[WebElement]:
        """Waiting and returning WebElements if they are present in the DOM"""
        return self.wait.until(ec.presence_of_all_elements_located((self.get_selenium_by(find_by=find_by),
                                                                    locator)))

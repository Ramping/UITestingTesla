from typing import List
from selenium.webdriver.common.keys import Keys
import locale
from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class BuyCar(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def __get_button_menu(self) -> WebElement:
        """Find menu button"""
        return self.is_visible('css', 'button[special="menuNavItem"]')

    def __get_modelx_in_menu(self) -> WebElement:
        """Find model x link"""
        return self.is_visible('css', 'a[title="Model X"]')

    def __get_buy_button(self) -> WebElement:
        """Find "Buy Now" button"""
        return self.is_visible('css', 'div.tcl-badges__button.tcl-animate.tcl-animate--to-reveal.tcl-animate--revealed>a[title="Buy Now"]')

    def get_no_result_tag(self) -> WebElement:
        """Find no results tag"""
        return self.is_visible('css', '.no-results-title')

    def go_to_modelx(self):
        """Goes to model x section"""
        self.__get_button_menu().click()
        self.__get_modelx_in_menu().click()

import time

from selenium.webdriver.common.by import By
from Pages.basePage import BasePage


class SearchProduct(BasePage):
    SEARCH_TAB = (By.ID, "twotabsearchtextbox")
    SEASRCH_BUTTON_CLICK = (By.ID, "nav-search-submit-button")
    GET_IT_TODAY = (By.XPATH, "//span[@class='a-size-base a-color-base' and text()='Get It Today']")

    def search_for_product(self, productname):
        self.send_keys(self.SEARCH_TAB, productname)
        self.click(self.SEASRCH_BUTTON_CLICK)
        self.click(self.GET_IT_TODAY)






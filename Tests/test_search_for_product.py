from Pages.Product_search import SearchProduct
from Utilities.TestData import TestData


class TestSearchProductName:


    def test_search_for_a_product(self, driver):
        launch = SearchProduct(driver)
        launch.search_for_product(TestData.productName1)


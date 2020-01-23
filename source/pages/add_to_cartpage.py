import logging
import time

from source.pages.home_page_search_product import HomePageSearchProduct
from source.utilities.generic_methods import GenericMethods
from source.utilities import excel
from source.utilities import customlogger as cl

'''
@author:Akshay
@email:akshay.kodur@gmail.com
@date:9th Jan
'''

class AddToCart(GenericMethods):
    """
        Searching products in Amazon
        """
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        # We are inheriting GenericMethods for webdriver in generic methods
        # constructor chaining
        super().__init__(driver)
        self.driver = driver
        HomePageSearchProduct(driver)

    def addToCart(self):
        self.switch_to_child_window(self.driver)
        self.timeSleep()
        self.elementClick("//input[@id='add-to-cart-button']","xpath")

    def verifyAddtoCart(self):
        actual_res = excel.get_value("Cart", "TC_002", "SuccessMessage")
        print(actual_res)
        expected_res = self.getText("//h1[@class='a-size-medium a-text-bold']","xpath")
        print(expected_res)
        assert expected_res in actual_res ,print("success message not verified")
        print("success message verified")

    def verifyAddedProduct(self):
        self.elementClick("//a[@id='hlb-view-cart-announce']","xpath")
        product_added = excel.get_value("Cart", "TC_002", "SuccessMessageAfterSelected")
        actual_added_product = self.getText("(//span[contains(text(),'Apple iPhone XR (64GB) - Black')])[1]","xpath")
        assert product_added in actual_added_product,"Product added is not matching"
        print("Product added successfully")
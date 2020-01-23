import logging
import time

from source.utilities.generic_methods import GenericMethods

from source.utilities import customlogger as cl

'''
@author:Akshay
@email:akshay.kodur@gmail.com
@date:9th Jan
'''


class HomePageSearchProduct(GenericMethods):
    """
    Searching products in Amazon
    """
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        # We are inheriting GenericMethods for webdriver in generic methods
        # constructor chaining
        super().__init__(driver)
        self.driver = driver
        self.search_Product_id = "twotabsearchtextbox"

    def searchBox(self, productName):
        # using self keyword we can access the methods in generic
        self.sendKeys(productName, self.search_Product_id)
        time.sleep(3)
    def clickOnProduct(self):
        self.elementClick("(//span[text()='Apple iPhone XR (64GB) - Black'])[2]","xpath")
        self.timeSleep()
    

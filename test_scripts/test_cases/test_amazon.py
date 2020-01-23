from source.pages.home_page_search_product import HomePageSearchProduct as searchProd
from source.pages.add_to_cartpage import AddToCart as addtc
from source.utilities.webdriver_factory import WebDriverFactory

#searching the product in search box
class HomeSearchProduct(WebDriverFactory):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def searchProduct(self,name):
        searchProd(self.driver).searchBox(name)
        searchProd(self.driver).elementClick("//input[@value='Go']","xpath")
        searchProd(self.driver).clickOnProduct()
    def add_To_cart(self):
        addtc(self.driver).addToCart()
        addtc(self.driver).verifyAddtoCart()
        addtc(self.driver).verifyAddedProduct()




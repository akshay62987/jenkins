import os
import time
from traceback import print_stack
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException,  ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from source.utilities import customlogger as cl
import logging
class GenericMethods():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver
    def screenshot(self,resultMesg):
        fileName=resultMesg+"."+str(round(time.time()*1000))+".png"
        screenshotDirectory="../screenshot/"
        relativeFilename=screenshotDirectory+fileName
        currentDirectory=os.path.dirname(__file__)
        destinationFile=os.path.join(currentDirectory,relativeFilename)
        destinationDirectory=os.path.join(currentDirectory,screenshotDirectory)
        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("screenshot save the directory:"+destinationFile)
        except:
            self.log.error("### Exception occured")
            print_stack()
    def getTitle(self):
        return self.driver.title

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator Type" + locatorType + "not correct/supported")
            return False

    def getElement(self,locator,locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            self.log.info("Element found with locator:" + locator + "and locatorType:" + locatorType)
        except:
            self.log.info("Element not found with locator:" + locator + "and locatorType" + locatorType)
        return element

    def clearText(self,locator,locatorType="id"):
        try:
            self.getElement(locator,locatorType).clear()
            self.log.info("The text field is cleared with locator" + locator + "and locatorType" + locatorType)
        except:
            self.log.error("##### Not able to clear #####")

    def elementClick(self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            self.log.info("clicked on element with locator:"+locator+ "locatorType" + locatorType)
        except:
            self.log.info("Cannot click on the element with locator:" + locator + "locatorType" + locatorType)

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locator type: " + locatorType)
        except:
            self.log.info("Cannot Send data on element with locator: " + locator + " locator type: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementPresentCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not Found")
                return False
        except:
            self.log.info("Element not Found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                             ":: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=10, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable(byType, locator))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element
    def switch_to_child_window(self,driver):
        child_window = None
        parent_window = driver.current_window_handle
        window_ids = driver.window_handles
        try:
            for window_id in window_ids:
                if window_id !=parent_window:
                    child_window = window_id
                    break
            driver.switch_to.window(child_window)
            self.log.info("Switched to the child window")
        except Exception:
            self.log.info("Unable to change the focus to the child window")
            print_stack()

    def timeSleep(self):
        time.sleep(3)

    def getText(self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            text=element.text
            self.log.info("Text web element is captured")
        except Exception:
            self.log.info("Text web element is not captured")
        return text

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(12)
driver.maximize_window()
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("Iphone XR")
driver.find_element_by_xpath("//input[@value='Go']").click()
driver.find_element_by_xpath("//span[text()='Apple iPhone XR (64GB) - Yellow']").click()
child = driver.window_handles[1]
driver.switch_to_window(child)
driver.find_element_by_xpath("//input[@id='add-to-cart-button']").click()
driver.find_element_by_xpath("//a[@id='hlb-view-cart-announce']").click()
# cur_url = driver.current_url
# print(cur_url)
# exp_url = "https://www.amazon.in/gp/cart/view.html/ref=lh_cart"
# assert exp_url in cur_url, "Url mismatch"
# print("URL is matching")
expec_title = "Apple iPhone XR (64GB) - Yellow"
actual_title = driver.find_element_by_xpath("//span[@class='a-size-medium sc-product-title']").text
print(actual_title)
assert actual_title in expec_title,"False"
print("Product added to the cart....Verified")
driver.quit()
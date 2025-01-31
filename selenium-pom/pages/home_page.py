from selenium.webdriver.common.by import By


class HomePage():


   def __init__(self,driver):
       self.driver = driver


   search_input  = (By.ID, "searchInputId")
   search_button  = (By.CSS_SELECTOR, "button[data-automation-id = 'searchIconBlock']")


   def search_product(self, product):
      self.driver.find_element(*self.search_input).send_keys(product)
      self.driver.find_element(*self.search_button).click()




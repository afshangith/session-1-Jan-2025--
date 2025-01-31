from selenium.webdriver.common.by import By


class  CartPage():

    def __init__(self, driver):
        self.driver = driver


    product_title = (By.CSS_SELECTOR, "a[data-automation-id ='at-product-title-link']")
    check_out_button = (By.CSS_SELECTOR, "[id='checkoutButton']")


    def verify_cart_product(self, expected_product):
        product = self.driver.find_element(*self.product_title).text
        assert product ==  expected_product


    def click_cart_button(self):
        self.driver.find_element(*self.check_out_button).click()

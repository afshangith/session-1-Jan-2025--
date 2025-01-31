from selenium.webdriver.common.by import By


class ProductDetailPage():

    def __init__(self, driver):
        self.driver = driver


    product_title_field = (By.CSS_SELECTOR, "h1[data-automation-id = 'product-title']")
    add_cart_button = (By.CSS_SELECTOR, "p[data-automation-id = 'addToCart']")
    view_checkout_button = (By.CSS_SELECTOR, "button[data-automation-id ='at-panel-checkout-button']")


    def verify_product(self, expected_product_title):
        product_text = self.driver.find_element(*self.product_title_field).text
        assert product_text == expected_product_title


    def add_to_cart(self):
        self.driver.find_element(*self.add_cart_button).click()


    def checkout_button(self):
        self.driver.find_element(*self.view_checkout_button).click()


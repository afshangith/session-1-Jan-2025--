from selenium.webdriver.common.by import By


class SignInPage():

    def __init__(self, driver):
        self.driver = driver

    user_input = (By.ID, 'email')
    password_input = (By.ID, 'cartSignInPassword')
    sign_in_button = (By.CSS_SELECTOR, "[data-automation-id='at-sign-in-button']")
    create_new_account = (By.CSS_SELECTOR,'button[data-automation-id = "at-create-account-button"]')


    def login_in_app(self,user,password):
         self.driver.find_element(*self.user_input).send_keys(user)
         self.driver.find_element(*self.password_input).send_keys(password)
         self.driver.find_element(*self.sign_in_button).click()


    def click_create_new_account_button(self):
        self.driver.find_element(*self.create_new_account).click()






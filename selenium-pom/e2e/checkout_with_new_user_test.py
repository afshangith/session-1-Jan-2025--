from base_test import BaseTest
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage
from pages.signin_page import SignInPage


class TestCheckOutExistingUser(BaseTest):


    def test_checkout_with_new_user(self):
        home_page = HomePage(self.driver)
        home_page.search_product("Archaeo Sarro 2-pc. Tab Top Window Tier")
        product_detail_page = ProductDetailPage(self.driver)
        product_detail_page.verify_product("Archaeo Sarro 2-pc. Tab Top Window Tier")
        product_detail_page.add_to_cart()
        product_detail_page.checkout_button()
        cart_page = CartPage(self.driver)
        cart_page.verify_cart_product("Archaeo Sarro 2-pc. Tab Top Window Tier")
        cart_page.click_cart_button()
        sign_in_page = SignInPage(self.driver)
        sign_in_page.click_create_new_account_button()

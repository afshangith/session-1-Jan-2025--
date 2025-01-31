from base_test import BaseTest
from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage


class TestSearch(BaseTest):


    def test_search(self):
        home_page = HomePage(self.driver)
        home_page.search_product("Archaeo Sarro 2-pc. Tab Top Window Tier")
        product_detail_page = ProductDetailPage(self.driver)
        product_detail_page.verify_product("Archaeo Sarro 2-pc. Tab Top Window Tier")

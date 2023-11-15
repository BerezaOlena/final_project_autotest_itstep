import pytest
from ..pages.base_page import BasePage
from ..pages.order_page import OrderPage
from ..pages.signup_login_page import SignupLoginPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order_page
class TestOrderPage:
    def setup_method(self):
        pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_login_to_cabinet(self, browser):
        pass

    def test_order_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page_l = SignupLoginPage(browser, self.link_to_cabinet)
        page_l.is_button_enter_to_signup_login()
        page_l.is_email_login_input(sets.TEST_EMAIL)
        page_l.is_password_login_input(sets.PASSWORD)
        page_l.is_button_login_push()
        page.is_arrivals_table_8_push()
        page.is_arrivals_table_8_to_cart()
        page.is_arrivals_table_8_to_cart_push()
        page.is_cart_title()
        page.is_button_close()
        page.is_count_product_in_cart()
        page.is_continue_shopping()
        page.is_order()
        page.is_clear_cart()
        page.is_order_push()
        page.explicitly_wait(5)
        page.is_order_text()
        page.is_button_order()
        page.is_button_order_push()
        page.is_alert_success_order()
        page.explicitly_wait(5)

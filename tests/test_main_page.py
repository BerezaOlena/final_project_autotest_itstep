import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
from ..settings import sets
import random


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        hash_name = "%032x" % random.getrandbits(128)
        self.email_for_subscribe = f"{hash_name}@mail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_phone()
        page.is_button_email()
        page.is_button_feedback()
        page.is_button_delivery()
        page.is_button_warranty()
        page.is_button_login_signup()
        page.is_button_logo_icon()
        page.is_button_search_input()
        page.is_button_search()
        page.is_button_wish()
        page.is_button_wish_count()
        page.is_button_cart()
        page.is_button_cart_count()
        page.is_button_currency()
        page.is_button_currency_uah()
        page.is_button_currency_usd()
        page.is_button_currency_eur()
        page.is_button_samsung()
        page.is_button_samsung_j701()
        page.is_button_new()
        page.is_button_sale()
        page.is_button_hits()

    def test_main_page_body(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_refund()
        page.is_button_free_delivery()
        page.is_button_delayed_payment()
        page.is_button_technical_support()
        page.is_button_slider()
        page.is_button_slider_3()
        page.is_button_category_charging()
        page.is_button_category_charging_wireless()
        page.is_button_arrivals_view_all()
        page.is_button_arrivals_previous()
        page.is_button_arrivals_next()
        page.is_button_arrivals_table()
        page.is_button_arrivals_table_8()
        page.is_button_hits_view_all()
        page.is_button_hits_previous()
        page.is_button_hits_next()
        page.is_button_hits_table()
        page.is_button_hits_table_5()
        page.is_button_trends_previous()
        page.is_button_trends_next()
        page.is_button_trends_table_2()

    def test_main_page_footer(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_subscribed()
        page.is_button_subscribed_email()
        page.is_button_newsletter_icon()
        page.is_button_newsletter_text()
        page.is_button_newsletter_title()
        page.is_button_logo_footer()
        page.is_button_telegram()
        page.is_button_phone_footer()

    def test_main_page_subscribed_action(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.subscribed_email_input(self.email_for_subscribe)
        page.is_alert_success_subscribed()

# pytest -s -v
# pytest -s -v --browser_name="firefox"
# pytest -s -v --browser_mode="gui"
# pytest -s -v --browser_window_size="max"
# pytest -s -v --browser_name="firefox" --browser_mode="gui"
# pytest -s -v --browser_name="firefox" --browser_window_size="max"
# pytest -s -v --browser_mode="gui" --browser_window_size="max"
# pytest -s -v --browser_name="firefox" --browser_mode="gui" --browser_window_size="max"

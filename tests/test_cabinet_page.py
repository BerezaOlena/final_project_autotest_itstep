import pytest
from ..pages.base_page import BasePage
from ..pages.cabinet_page import CabinetPage
from ..pages.signup_login_page import SignupLoginPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.cabinet_page
class TestCabinetPage:

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_cabinet_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = CabinetPage(browser, self.link_to_cabinet)
        page_l = SignupLoginPage(browser, self.link_to_cabinet)
        page_l.is_button_enter_to_signup_login()
        page_l.is_email_login_input("xotrecroummabru-7139@yopmail.com")
        page_l.is_password_login_input("mabru-7139")
        page_l.is_button_login_push()
        page_l.is_alert_success()
        page.is_main()
        page.is_user_cabinet()
        page.is_user_cabinet_text()
        page.is_order_history()
        page.is_check_cart()
        page.is_check_wish()
        page.is_show_view()
        page.is_feedback_error()
        page.is_currency_actual()
        page.is_video_view()
        page.is_user_feedback()
        page.is_info()
        page.is_name()
        page.is_name_input()
        page.is_add_name()
        page.is_password()
        page.is_password_input()
        page.is_edit_password()
        page.is_email()
        page.is_email_input()
        page.is_edit_email()
        page.is_phone()
        page.is_phone_input()
        page.is_add_phone()
        page.is_address()
        page.is_address_input()
        page.is_add_address()

import pytest
from ..pages.base_page import BasePage
from ..pages.signup_login_page import SignupLoginPage
from ..settings import sets
import random


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.signup_login_page
class TestSignupLoginPage:

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def setup_method(self):
        hash_name = "%016x" % random.getrandbits(128)
        self.email_for_signup_login = f"{hash_name}@mail.com"
        self.password_for_signup_login = f"@@{hash_name}@@"

    def test_signup_login_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.is_button_enter_to_signup_login()
        page.is_button_signup_push()
        page.is_signup_top_text()
        page.is_email_text_signup()
        page.is_email_signup()
        page.is_email_signup_input(self.email_for_signup_login)
        page.is_password_text_signup()
        page.is_password_signup()
        page.is_password_signup_input(self.password_for_signup_login)
        page.is_login_button()
        page.is_signup_button()
        page.is_signup_button_push()
        page.is_alert_success()
        page.is_button_enter_to_signup_login()
        page.is_enter_top_text()
        page.is_email_text_login()
        page.is_email_login()
        page.is_email_login_input(self.email_for_signup_login)
        page.is_password_text_login()
        page.is_password_login()
        page.is_password_login_input(self.password_for_signup_login)
        page.is_button_signup()
        page.is_button_login()
        page.is_button_login_push()
        page.is_alert_success()

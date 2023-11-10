from ..pages import base_page, locators
import inspect


class SignupLoginPage(base_page.BasePage):

    def is_button_enter_to_signup_login(self):
        assert self.click_element(*locators.BasePageLocators.LOGIN_SIGNUP), \
            "Element 'login' is not present or intractable"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_enter_top_text(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.ENTER_TOP_TEXT), \
            "Element 'enter_top_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email_text_login(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.EMAIL_TEXT_LOGIN), \
            "Element 'email_text_login' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email_login(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.EMAIL_LOGIN), \
            "Element 'email_login' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email_login_input(self, email):
        assert self.input_data(*locators.SignupLoginPageLocators.EMAIL_LOGIN, email), \
            "Element 'email_login_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_text_login(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.PASSWORD_TEXT_LOGIN), \
            "Element 'password_text_login' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_login(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.PASSWORD_LOGIN), \
            "Element 'password_login' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_login_input(self, password):
        assert self.input_data(*locators.SignupLoginPageLocators.PASSWORD_LOGIN, password), \
            "Element 'password_login_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_signup(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.BUTTON_SIGNUP), \
            "Element 'button_signup' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_signup_push(self):
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_SIGNUP), \
            "Element 'button_signup' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_login(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.BUTTON_LOGIN), \
            "Element 'button_login' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_login_push(self):
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_LOGIN), \
            "Element 'button_login_push' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_alert_success(self):
        assert self.is_element_appears_after_while(*locators.SignupLoginPageLocators.ALERT_SUCCESS_SIGNUP_LOGIN,
                                                   timeout=5), \
            "Button 'alert_success_subscribed' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_signup_top_text(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.SIGNUP_TOP_TEXT), \
            "Element 'signup_top_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email_text_signup(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.EMAIL_TEXT_SIGNUP), \
            "Element 'email_text_signup' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email_signup(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.EMAIL_SIGNUP), \
            "Element 'email_signup' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email_signup_input(self, email):
        assert self.input_data(*locators.SignupLoginPageLocators.EMAIL_SIGNUP, email), \
            "Element 'email_signup_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_text_signup(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.PASSWORD_TEXT_SIGNUP), \
            "Element 'password_text_signup' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_signup(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.PASSWORD_SIGNUP), \
            "Element 'password_signup' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_signup_input(self, password):
        assert self.input_data(*locators.SignupLoginPageLocators.PASSWORD_SIGNUP, password), \
            "Element 'password_signup_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_signup_button(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.SIGNUP_BUTTON), \
            "Element 'signup_button' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_signup_button_push(self):
        assert self.click_element(*locators.SignupLoginPageLocators.SIGNUP_BUTTON), \
            "Element 'signup_button' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_login_button(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.LOGIN_BUTTON), \
            "Element 'login_button' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_login_button_push(self):
        assert self.click_element(*locators.SignupLoginPageLocators.LOGIN_BUTTON), \
            "Element 'login_button_push' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

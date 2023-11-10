from ..pages import locators, main_page, base_page
import inspect


class CabinetPage(base_page.BasePage):

    def is_main(self):
        assert self.is_element_present(*locators.CabinetPageLocators.MAIN), \
            "Element 'main' is not present or intractable"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_user_cabinet(self):
        assert self.is_element_present(*locators.CabinetPageLocators.USER_CABINET), \
            "Element 'user_cabinet' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_user_cabinet_text(self):
        assert self.is_element_present(*locators.CabinetPageLocators.USER_CABINET_TEXT), \
            "Element 'user_cabinet_text' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_order_history(self):
        assert self.is_element_present(*locators.CabinetPageLocators.ORDER_HISTORY), \
            "Element 'order_history' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_check_cart(self):
        assert self.is_element_present(*locators.CabinetPageLocators.CHECK_CART), \
            "Element 'check_cart' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_check_wish(self):
        assert self.is_element_present(*locators.CabinetPageLocators.CHECK_WISH), \
            "Element 'check_wish' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_show_view(self):
        assert self.is_element_present(*locators.CabinetPageLocators.SHOW_VIEW), \
            "Element 'show_view' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_feedback_error(self):
        assert self.is_element_present(*locators.CabinetPageLocators.FEEDBACK_ERROR), \
            "Element 'feedback_error' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_currency_actual(self):
        assert self.is_element_present(*locators.CabinetPageLocators.CURRENCY_ACTUAL), \
            "Element 'currency_actual' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_video_view(self):
        assert self.is_element_present(*locators.CabinetPageLocators.VIDEO_VIEW), \
            "Element 'video_view' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_user_feedback(self):
        assert self.is_element_present(*locators.CabinetPageLocators.USER_FEEDBACK), \
            "Element 'user_feedback' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info(self):
        assert self.is_element_present(*locators.CabinetPageLocators.INFO), \
            "Element 'info' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_name(self):
        assert self.is_element_present(*locators.CabinetPageLocators.NAME), \
            "Element 'name' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_name_input(self):
        assert self.is_element_present(*locators.CabinetPageLocators.NAME_INPUT), \
            "Element 'name_input' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_add_name(self):
        assert self.is_element_present(*locators.CabinetPageLocators.ADD_NAME), \
            "Element 'add_name' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password(self):
        assert self.is_element_present(*locators.CabinetPageLocators.PASSWORD), \
            "Element 'password' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_input(self):
        assert self.is_element_present(*locators.CabinetPageLocators.PASSWORD_INPUT), \
            "Element 'password_input' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_edit_password(self):
        assert self.is_element_present(*locators.CabinetPageLocators.EDIT_PASSWORD), \
            "Element 'edit_password' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email(self):
        assert self.is_element_present(*locators.CabinetPageLocators.EMAIL), \
            "Element 'email' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email_input(self):
        assert self.is_element_present(*locators.CabinetPageLocators.EMAIL_INPUT), \
            "Element 'password_input' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_edit_email(self):
        assert self.is_element_present(*locators.CabinetPageLocators.EDIT_EMAIL), \
            "Element 'edit_password' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_phone(self):
        assert self.is_element_present(*locators.CabinetPageLocators.PHONE), \
            "Element 'phone' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_phone_input(self):
        assert self.is_element_present(*locators.CabinetPageLocators.PHONE_INPUT), \
            "Element 'phone_input' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_add_phone(self):
        assert self.is_element_present(*locators.CabinetPageLocators.ADD_PHONE), \
            "Element 'add_phone' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_address(self):
        assert self.is_element_present(*locators.CabinetPageLocators.ADDRESS), \
            "Element 'address' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_address_input(self):
        assert self.is_element_present(*locators.CabinetPageLocators.ADDRESS_INPUT), \
            "Element 'address_input' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_add_address(self):
        assert self.is_element_present(*locators.CabinetPageLocators.ADD_ADDRESS), \
            "Element 'add_address' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

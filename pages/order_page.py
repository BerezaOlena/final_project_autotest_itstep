from ..pages import base_page, locators
import inspect
import re


class OrderPage(base_page.BasePage):
    def is_logo_icon_push(self):
        assert self.click_element(*locators.BasePageLocators.LOGO_ICON), \
            "Button 'logo_icon' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_arrivals_table_8_push(self):
        assert self.click_element(*locators.MainPageLocators.ARRIVALS_TABLE_8), \
            "Element 'arrivals_table_8_push' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_arrivals_table_8_to_cart(self):
        assert self.is_element_present(*locators.OrderPageLocators.ARRIVALS_TABLE_8_TO_CART), \
            "Element 'enter_top_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_arrivals_table_8_to_cart_push(self):
        assert self.click_element(*locators.OrderPageLocators.ARRIVALS_TABLE_8_TO_CART), \
            "Element 'arrivals_table_8_to_cart_push' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_cart_title(self):
        assert self.is_element_present(*locators.OrderPageLocators.CART_TITLE), \
            "Element 'cart_title' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_close(self):
        assert self.is_element_present(*locators.OrderPageLocators.BUTTON_CLOSE), \
            "Element 'button_close' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_count_product_in_cart(self):
        assert self.is_element_present(*locators.OrderPageLocators.COUNT_PRODUCT_IN_CART), \
            "Element 'count_product_in_cart' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_continue_shopping(self):
        assert self.is_element_present(*locators.OrderPageLocators.CONTINUE_SHOPPING), \
            "Element 'continue_shopping' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_order(self):
        assert self.is_element_present(*locators.OrderPageLocators.ORDER), \
            "Element 'order' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_order_push(self):
        assert self.click_element(*locators.OrderPageLocators.ORDER), \
            "Element 'enter_top_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_clear_cart(self):
        assert self.is_element_present(*locators.OrderPageLocators.CLEAR_CART), \
            "Element 'clear_cart' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_order_text(self):
        assert self.is_element_present(*locators.OrderPageLocators.ORDER_TEXT), \
            "Element 'order_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email_text_order(self):
        assert self.is_element_present(*locators.OrderPageLocators.EMAIL_TEXT_ORDER), \
            "Element 'email_text_order' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email_order(self):
        assert self.is_element_present(*locators.OrderPageLocators.EMAIL_ORDER), \
            "Element 'email_order' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email_order_input(self, email):
        assert self.input_data(*locators.OrderPageLocators.EMAIL_ORDER, email), \
            "Element 'email_order_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_text_order(self):
        assert self.is_element_present(*locators.OrderPageLocators.PASSWORD_TEXT_ORDER), \
            "Element 'password_text_order' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_order(self):
        assert self.is_element_present(*locators.OrderPageLocators.PASSWORD_ORDER), \
            "Element 'password_order' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_order_input(self, password):
        assert self.input_data(*locators.OrderPageLocators.PASSWORD_ORDER, password), \
            "Element 'password_order_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_order(self):
        assert self.is_element_present(*locators.OrderPageLocators.BUTTON_ORDER), \
            "Element 'button_order' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_order_push(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ORDER), \
            "Element 'button_order' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_alert_success_order(self):
        assert self.is_element_appears_after_while(*locators.OrderPageLocators.ALERT_SUCCESS_ORDER, timeout=5), \
            "Element 'alert_success_order' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_logo_icon_push(self):
        assert self.click_element(*locators.BasePageLocators.LOGO_ICON), \
            "Button 'logo_icon_push' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

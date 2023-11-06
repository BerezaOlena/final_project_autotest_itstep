from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):
    def is_button_phone(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE), \
            "Button phone is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_button_email(self):
        assert self.is_element_present(*locators.BasePageLocators.EMAIL), \
            "Button email is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_feedback(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.FEEDBACK), \
            "Button feedback is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_delivery(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.DELIVERY), \
            "Button delivery is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_warranty(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.WARRANTY), \
            "Button warranty is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_login(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGIN_SIGNUP), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_logo_icon(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_ICON), \
            "Button logo icon is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_search_input(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_INPUT), \
            "Button search input is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_search(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_BUTTON), \
            "Button search is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_wish(self):
        assert self.is_element_present(*locators.BasePageLocators.WISH), \
            "Button wish is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_wish_count(self):
        assert self.is_element_present(*locators.BasePageLocators.WISH_COUNT), \
            "Button wish count is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_cart(self):
        assert self.is_element_present(*locators.BasePageLocators.CART), \
            "Button cart is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_cart_count(self):
        assert self.is_element_present(*locators.BasePageLocators.CART_COUNT), \
            "Button cart count is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_currency(self):
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
            "Button currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_currency_uah(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "Button currency is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY_UAH), \
            "Button currency uah is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_currency_usd(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "Button currency is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY_USD), \
            "Button currency usd is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_currency_eur(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "Button currency is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY_EUR), \
            "Button currency eur is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_samsung(self):
        assert self.is_element_present(*locators.BasePageLocators.SAMSUNG), \
            "Button samsung is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_samsung_j701(self):
        assert self.hover_action(*locators.BasePageLocators.SAMSUNG), \
            "Button samsung is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.SAMSUNG_J701), \
            "Button samsung j701 is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_new(self):
        assert self.is_element_present(*locators.BasePageLocators.NEW), \
            "Button new is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_sale(self):
        assert self.is_element_present(*locators.BasePageLocators.SALE), \
            "Button sale is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_hits(self):
        assert self.is_element_present(*locators.BasePageLocators.HITS), \
            "Button hits is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_subscribed(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBED_FOOTER), \
            "Button subscribed is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_button_subscribed_email(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBED_EMAIL_FOOTER), \
            "Button subscribed email is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_newsletter_icon(self):
        assert self.is_element_present(*locators.BasePageLocators.NEWSLETTER_ICON), \
            "Button newsletter icon is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_newsletter_text(self):
        assert self.is_element_present(*locators.BasePageLocators.NEWSLETTER_TEXT), \
            "Button newsletter text is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_newsletter_title(self):
        assert self.is_element_present(*locators.BasePageLocators.NEWSLETTER_TITLE), \
            "Button newsletter title is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_logo_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_FOOTER), \
            "Button logo footer is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_telegram(self):
        assert self.is_element_present(*locators.BasePageLocators.TELEGRAM_FOOTER), \
            "Button telegram is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_phone_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE_FOOTER), \
            "Button phone footer is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_refund(self):
        assert self.is_element_present(*locators.MainPageLocators.REFUND), \
            "Button refund is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_button_free_delivery(self):
        assert self.is_element_present(*locators.MainPageLocators.FREE_DELIVERY), \
            "Button free delivery is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_delayed_payment(self):
        assert self.is_element_present(*locators.MainPageLocators.ARRIVALS_TABLE_8), \
            "Button delayed payment is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_technical_support(self):
        assert self.is_element_present(*locators.MainPageLocators.TECHNICAL_SUPPORT), \
            "Button technical support is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_arrivals_view_all(self):
        assert self.is_element_present(*locators.MainPageLocators.ARRIVALS_VIEW_ALL), \
            "Button arrivals view all is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_arrivals_previous(self):
        assert self.is_element_present(*locators.MainPageLocators.ARRIVALS_PREVIOUS), \
            "Button arrivals previous is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_arrivals_next(self):
        assert self.is_element_present(*locators.MainPageLocators.ARRIVALS_NEXT), \
            "Button arrivals next is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_arrivals_table(self):
        assert self.is_element_present(*locators.MainPageLocators.ARRIVALS_TABLE), \
            "Button arrivals table is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_arrivals_table_8(self):
        assert self.is_element_present(*locators.MainPageLocators.ARRIVALS_TABLE_8), \
            "Button arrivals table 8 is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_hits_view_all(self):
        assert self.is_element_present(*locators.MainPageLocators.HITS_VIEW_ALL), \
            "Button hits view all is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_hits_previous(self):
        assert self.is_element_present(*locators.MainPageLocators.HITS_PREVIOUS), \
            "Button hits previous is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_hits_next(self):
        assert self.is_element_present(*locators.MainPageLocators.HITS_NEXT), \
            "Button hits next is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_hits_table(self):
        assert self.is_element_present(*locators.MainPageLocators.HITS_TABLE), \
            "Button hits table is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_hits_table_5(self):
        assert self.is_element_present(*locators.MainPageLocators.HITS_TABLE_5), \
            "Button hits table 5 is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_trends_previous(self):
        assert self.is_element_present(*locators.MainPageLocators.TRENDS_PREVIOUS), \
            "Button trends previous is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_trends_next(self):
        assert self.is_element_present(*locators.MainPageLocators.TRENDS_NEXT), \
            "Button trends next is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_trends_table_2(self):
        assert self.is_element_present(*locators.MainPageLocators.TRENDS_TABLE_2), \
            "Button trends table 2 is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")




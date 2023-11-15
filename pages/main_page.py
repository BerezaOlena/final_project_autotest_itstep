from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):
    # HEADER
    def is_button_phone(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE), \
            "Button 'phone' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_button_email(self):
        assert self.is_element_present(*locators.BasePageLocators.EMAIL), \
            "Button 'email' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_feedback(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.FEEDBACK), \
            "Button 'feedback' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_delivery(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.DELIVERY), \
            "Button 'delivery' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_warranty(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.WARRANTY), \
            "Button 'warranty' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_login_signup(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGIN_SIGNUP), \
            "Button 'login_signup' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_logo_icon(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_ICON), \
            "Button 'logo_icon' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_search_input(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_INPUT), \
            "Button 'search_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_search(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_BUTTON), \
            "Button 'search' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_wish(self):
        assert self.is_element_present(*locators.BasePageLocators.WISH), \
            "Button 'wish' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_wish_count(self):
        assert self.is_element_present(*locators.BasePageLocators.WISH_COUNT), \
            "Button 'wish_count' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_cart(self):
        assert self.is_element_present(*locators.BasePageLocators.CART), \
            "Button 'cart' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_cart_count(self):
        assert self.is_element_present(*locators.BasePageLocators.CART_COUNT), \
            "Button 'cart_count' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_currency(self):
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
            "Button 'currency' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_currency_uah(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "Button 'currency' is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY_UAH), \
            "Button 'currency_uah' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_currency_usd(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "Button 'currency' is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY_USD), \
            "Button 'currency_usd' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_currency_eur(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "Button 'currency' is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY_EUR), \
            "Button 'currency_eur' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_samsung(self):
        assert self.is_element_present(*locators.BasePageLocators.SAMSUNG), \
            "Button 'samsung' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_samsung_j701(self):
        assert self.hover_action(*locators.BasePageLocators.SAMSUNG), \
            "Button 'samsung' is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.SAMSUNG_J701), \
            "Button 'samsung_j701' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_new(self):
        assert self.is_element_present(*locators.BasePageLocators.NEW), \
            "Button 'new' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_sale(self):
        assert self.is_element_present(*locators.BasePageLocators.SALE), \
            "Button 'sale' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_hits(self):
        assert self.is_element_present(*locators.BasePageLocators.HITS), \
            "Button 'hits' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    # BODY
    def is_button_refund(self):
        assert self.is_element_present(*locators.MainPageLocators.REFUND), \
            "Button 'refund' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_button_free_delivery(self):
        assert self.is_element_present(*locators.MainPageLocators.FREE_DELIVERY), \
            "Button 'free_delivery' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_delayed_payment(self):
        assert self.is_element_present(*locators.MainPageLocators.ARRIVALS_TABLE_8), \
            "Button 'delayed_payment' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_technical_support(self):
        assert self.is_element_present(*locators.MainPageLocators.TECHNICAL_SUPPORT), \
            "Button 'technical_support' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_slider(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDER), \
            "Button 'slider' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_slider_3(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDER_3), \
            "Button 'slider_3' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_category_charging(self):
        assert self.is_element_present(*locators.MainPageLocators.CATEGORY_CHARGING), \
            "Button 'category_charging' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_category_charging_wireless(self):
        assert self.hover_action(*locators.MainPageLocators.CATEGORY_CHARGING), \
            "Button 'category_charging' is not present or intractable"
        assert self.is_element_present(*locators.MainPageLocators.CATEGORY_CHARGING_WIRELESS), \
            "Button 'category_charging_wireless' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_arrivals_view_all(self):
        assert self.is_element_present(*locators.MainPageLocators.ARRIVALS_VIEW_ALL), \
            "Button ''arrivals_view_all'' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_arrivals_previous(self):
        assert self.is_element_present(*locators.MainPageLocators.ARRIVALS_PREVIOUS), \
            "Button 'arrivals_previous' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_arrivals_next(self):
        assert self.is_element_present(*locators.MainPageLocators.ARRIVALS_NEXT), \
            "Button 'arrivals_next' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_arrivals_table(self):
        assert self.is_element_present(*locators.MainPageLocators.ARRIVALS_TABLE), \
            "Button 'arrivals_table' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_arrivals_table_8(self):
        assert self.is_element_present(*locators.MainPageLocators.ARRIVALS_TABLE_8), \
            "Button 'arrivals_table_8' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_hits_view_all(self):
        assert self.is_element_present(*locators.MainPageLocators.HITS_VIEW_ALL), \
            "Button 'hits_view_all' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_hits_previous(self):
        assert self.is_element_present(*locators.MainPageLocators.HITS_PREVIOUS), \
            "Button 'hits_previous' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_hits_next(self):
        assert self.is_element_present(*locators.MainPageLocators.HITS_NEXT), \
            "Button 'hits_next' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_hits_table(self):
        assert self.is_element_present(*locators.MainPageLocators.HITS_TABLE), \
            "Button 'hits_table' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_hits_table_5(self):
        assert self.is_element_present(*locators.MainPageLocators.HITS_TABLE_5), \
            "Button 'hits_table_5' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_trends_previous(self):
        assert self.is_element_present(*locators.MainPageLocators.TRENDS_PREVIOUS), \
            "Button 'trends_previous' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_trends_next(self):
        assert self.is_element_present(*locators.MainPageLocators.TRENDS_NEXT), \
            "Button 'trends_next' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_trends_table_2(self):
        assert self.is_element_present(*locators.MainPageLocators.TRENDS_TABLE_2), \
            "Button 'trends_table_2' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    # FOOTER
    def is_button_subscribed(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBED_FOOTER), \
            "Button 'subscribed' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_button_subscribed_email(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBED_EMAIL_FOOTER), \
            "Button 'subscribed_email' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def subscribed_email_input(self, email):
        assert self.input_data(*locators.BasePageLocators.SUBSCRIBED_EMAIL_FOOTER, email), \
            "Element 'subscribed_email' is not present"
        self.explicitly_wait(5)
        assert self.click_element(*locators.BasePageLocators.SUBSCRIBED_FOOTER), \
            "Element 'subscribed' is not present or intractable"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_alert_success_subscribed(self):
        assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
            "Button 'alert_success_subscribed' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_newsletter_icon(self):
        assert self.is_element_present(*locators.BasePageLocators.NEWSLETTER_ICON), \
            "Button 'newsletter_icon' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_newsletter_text(self):
        assert self.is_element_present(*locators.BasePageLocators.NEWSLETTER_TEXT), \
            "Button 'newsletter_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_newsletter_title(self):
        assert self.is_element_present(*locators.BasePageLocators.NEWSLETTER_TITLE), \
            "Button 'newsletter_title' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_logo_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_FOOTER), \
            "Button 'logo_footer' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_telegram(self):
        assert self.is_element_present(*locators.BasePageLocators.TELEGRAM_FOOTER), \
            "Button 'telegram' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_phone_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE_FOOTER), \
            "Button 'phone_footer' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

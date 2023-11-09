from selenium.webdriver.common.by import By


class BasePageLocators:
    # HEADER
    PHONE = (By.XPATH, "//div[text()='+38 098 911 95 22']")
    EMAIL = (By.XPATH, "//a[@href='mailto:']")
    DETAILS = (By.XPATH, "//a[text()='Детали сотрудничества']")
    FEEDBACK = (By.XPATH, "//a[@href='singlepage/feedback']")
    DELIVERY = (By.XPATH, "//a[@href='singlepage/delivery']")
    WARRANTY = (By.XPATH, "//a[@href='singlepage/warranty']")
    LOGIN_SIGNUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")

    LOGO_ICON = (By.XPATH, "//img[@src='images/logo.png']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Поиск товара...']")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='header_search_button trans_300']")
    WISH = (By.XPATH, "//img[@src='images/heart.png']")
    WISH_COUNT = (By.XPATH, "//span[@class='qty_wish']")
    CART = (By.XPATH, "//img[@src='images/cart.png']")
    CART_COUNT = (By.XPATH, "//span[@class='qty_products']")
    CURRENCY = (By.XPATH, "//select[@id='currency']")
    CURRENCY_UAH = (By.XPATH, "//option[text()='UAH']")
    CURRENCY_USD = (By.XPATH, "//option[text()='USD']")
    CURRENCY_EUR = (By.XPATH, "//option[text()='EUR']")

    SAMSUNG = (By.XPATH, "//div[text()='Samsung']")
    SAMSUNG_J701 = (By.XPATH, "//a[text()='Samsung J701']")
    HITS = (By.XPATH, "//span[text()='Хиты']")
    NEW = (By.XPATH, "//span[text()='Новинки']")
    SALE = (By.XPATH, "//span[text()='Скидки']")

    # FOOTER
    SUBSCRIBED_FOOTER = (By.XPATH, "//button[@class='newsletter_button']")
    SUBSCRIBED_EMAIL_FOOTER = (By.XPATH, "//input[@class='newsletter_input']")
    NEWSLETTER_ICON = (By.XPATH, "//img[@src='images/send.png']")
    NEWSLETTER_TITLE = (By.XPATH, "//div[@class='newsletter_title']")
    NEWSLETTER_TEXT = (By.XPATH, "//p[text()='...и узнайте о новинках и скидках первыми']")
    LOGO_FOOTER = (By.XPATH, "//img[@src='images/send.png']")
    TELEGRAM_FOOTER = (By.XPATH, "//a[@href='https://t.me/casenik_com_ua']")
    PHONE_FOOTER = (By.XPATH, "//div[@class='footer_phone']")

    ALERT_SUCCESS = (By.XPATH, "//div[@class='alert alert-success']")
    ALERT_ERROR = (By.XPATH, "//div[@class='alert alert-danger']")


class MainPageLocators:
    # BODY
    REFUND = (By.XPATH, "//div[@class='characteristics']//div[text()='Возврат средств']")
    FREE_DELIVERY = (By.XPATH, "//div[@class='characteristics']//div[text()='Бесплатная доставка']")
    DELAYED_PAYMENT = (By.XPATH, "//div[@class='characteristics']//div[text()='Отсрочка оплаты']")
    TECHNICAL_SUPPORT = (By.XPATH, "//div[@class='characteristics']//div[text()='Тех.поддержка']")

    SLIDER = (By.XPATH, "//div[@class='banner']//div[@class='slick-track']")
    SLIDER_3 = (By.XPATH, "//div[@class='banner']//div[@class='slick-track']//div[@data-slick-index='3']")
    CATEGORY_CHARGING = (By.XPATH, "//a[@href='category/zaryadki']")
    CATEGORY_CHARGING_WIRELESS = (By.XPATH, "//a[@href='category/Besprovodnye-BZU']")

    ARRIVALS_VIEW_ALL = (By.XPATH, "//div[@class='arrivals_nav_container']//a[@href='main/showNew']")
    ARRIVALS_PREVIOUS = (By.XPATH, "//div[@class='arrivals_nav_container']//i[@class='fas fa-chevron-left']")
    ARRIVALS_NEXT = (By.XPATH, "//div[@class='arrivals_nav_container']//i[@class='fas fa-chevron-right']")
    ARRIVALS_TABLE = (By.XPATH, "//div[@class='product_panel panel active']")
    ARRIVALS_TABLE_8 = (By.XPATH, "//div[@class='new_arrivals']//div[@data-slick-index='2']/div[2]")

    HITS_VIEW_ALL = (By.XPATH, "//div[@class='best_nav_container']//a[@href='main/showHit']")
    HITS_PREVIOUS = (By.XPATH, "//div[@class='best_prev best_nav']//i[@class='fas fa-chevron-left']")
    HITS_NEXT = (By.XPATH, "//div[@class='best_next best_nav']//i[@class='fas fa-chevron-right']")
    HITS_TABLE = (By.XPATH, "//div[@class='bestsellers_panel panel active']//div[@class='slick-list draggable']")
    HITS_TABLE_5 = (By.XPATH, "//div[@class='best_sellers']//div[@data-slick-index='4']")

    TRENDS_PREVIOUS = (
        By.XPATH, "//div[@class='trends_prev trends_nav slick-arrow']//i[@class='fas fa-angle-left ml-auto']")
    TRENDS_NEXT = (
        By.XPATH, "//div[@class='trends_next trends_nav slick-arrow']//i[@class='fas fa-angle-right ml-auto']")
    TRENDS_TABLE_2 = (By.XPATH, "//div[@class='trends_slider_container']//div[@data-slick-index='7']")

    # PRODUCT_CART
    ARRIVALS_TABLE_8_TO_CART = (
        By.XPATH, "//div[@class='new_arrivals']//div[@data-slick-index='2']/div[2]//button[@class='product_cart_button']")
    COUNT_PRODUCT_IN_CART = (
        By.XPATH, "//div[@id='cart']//td[text()='1 шт. ']")
    CONTINUE_SHOPPING = (
        By.XPATH, "//div[@class='modal fade show']//div[@class='modal-footer']//button[@class='btn btn-default']")
    ORDER = (By.XPATH, "//div[@class='modal fade show']//div[@class='modal-footer']//a[@class='btn btn-primary']")
    CLEAR_CART = (
        By.XPATH, "//div[@class='modal fade show']//div[@class='modal-footer']//button[@class='btn btn-danger']")
    BUTTON_CLOSE = (By.XPATH, "//div[@id='cart']//button[@class='close']")
    ORDER_TEXT = (By.XPATH, "//h2[text()='Оформление заказа']")


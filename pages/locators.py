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
    ARRIVALS_TABLE_8 = (
        By.XPATH, "//div[@class='new_arrivals']//div[@data-slick-index='2']/div[2]//div[@class='product_name']")

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


class OrderPageLocators:
    # PRODUCT_CART
    ARRIVALS_TABLE_8_TO_CART = (By.XPATH, "//button[@class='product_cart_button button cart_button']")
    CART_TITLE = (By.XPATH, "//h4[@id='myModalLabel']")
    BUTTON_CLOSE = (By.XPATH, "//div[@id='cart']//button[@class='close']")
    COUNT_PRODUCT_IN_CART = (By.XPATH, "//div[@id='cart']//td[text()='1 шт. ']")
    CONTINUE_SHOPPING = (
        By.XPATH, "//div[@class='modal fade show']//div[@class='modal-footer']//button[@class='btn btn-default']")
    ORDER = (By.XPATH, "//div[@class='modal fade show']//div[@class='modal-footer']//a[@class='btn btn-primary']")
    CLEAR_CART = (
        By.XPATH, "//div[@class='modal fade show']//div[@class='modal-footer']//button[@class='btn btn-danger']")

    ORDER_TEXT = (By.XPATH, "//h2[text()='Оформление заказа']")
    EMAIL_TEXT_ORDER = (By.XPATH, "//form[@action='cart/checkout']//label[@for='email']")
    EMAIL_ORDER = (By.XPATH, "//form[@action='cart/checkout']//input[@id='email']")
    PASSWORD_TEXT_ORDER = (By.XPATH, "//form[@action='cart/checkout']//label[@for='pasword']")
    PASSWORD_ORDER = (By.XPATH, "//form[@action='cart/checkout']//input[@id='password']")
    BUTTON_ORDER = (By.XPATH, "//button[@class='btn green']")

    ALERT_SUCCESS_ORDER = (By.XPATH, "//div[@class='alert alert-success']")
    ALERT_ERROR_ORDER = (By.XPATH, "//div[@class='alert alert-danger']")


class SignupLoginPageLocators:
    ENTER_TOP_TEXT = (By.XPATH, "//h1[text()='Вход']")
    EMAIL_TEXT_LOGIN = (By.XPATH, "//form[@action='user/login']//label[@for='email']")
    EMAIL_LOGIN = (By.XPATH, "//form[@action='user/login']//input[@id='email']")
    PASSWORD_TEXT_LOGIN = (By.XPATH, "//form[@action='user/login']//label[@for='pasword']")
    PASSWORD_LOGIN = (By.XPATH, "//form[@action='user/login']//input[@id='pasword']")
    BUTTON_LOGIN = (By.XPATH, "//form[@action='user/login']//button[@class='btn button-gen']")
    BUTTON_SIGNUP = (By.XPATH, "//form[@action='user/login']//a[@class='prior-two']")

    SIGNUP_TOP_TEXT = (By.XPATH, "//h1[text()='Регистрация']")
    EMAIL_TEXT_SIGNUP = (By.XPATH, "//form[@id='signup']//label[@for='email']")
    EMAIL_SIGNUP = (By.XPATH, "//form[@id='signup']//input[@id='email']")
    PASSWORD_TEXT_SIGNUP = (By.XPATH, "//form[@id='signup']//label[@for='pasword']")
    PASSWORD_SIGNUP = (By.XPATH, "//form[@id='signup']//input[@id='pasword']")
    SIGNUP_BUTTON = (By.XPATH, "//form[@id='signup']//button[@class='btn button-gen']")
    LOGIN_BUTTON = (By.XPATH, "//form[@id='signup']//a[@class='prior-two']")

    ALERT_SUCCESS_SIGNUP_LOGIN = (By.XPATH, "//div[@id='alert-success']")
    ALERT_ERROR_SIGNUP_LOGIN = (By.XPATH, "//div[@class='alert alert-danger']")

    LOGOUT_BUTTON = (By.XPATH, "//a[@href='user/logout']")
    CABINET_BUTTON = (By.XPATH, "//a[@href='user/cabinet']")

class CabinetPageLocators:
    MAIN = (By.XPATH, "//ol[@class='breadcrumb']//a[@href='https://casenik.com.ua']")
    USER_CABINET = (By.XPATH, "//li[text()='Личный кабинет']")
    USER_CABINET_TEXT = (By.XPATH, "//div[@class='register-top heading']")
    ORDER_HISTORY = (By.XPATH, "//a[@href='user/orders']")
    CHECK_CART = (By.XPATH, "//li//a[@href='cart/show']")
    CHECK_WISH = (By.XPATH, "//li//a[@href='wish/show']")
    SHOW_VIEW = (By.XPATH, "//li//a[@href='main/showViewed']")
    FEEDBACK_ERROR = (By.XPATH, "//li//a[@href='singlepage/feedback']")
    CURRENCY_ACTUAL = (By.XPATH, "//li//a[@href='https://finance.i.ua/']")
    VIDEO_VIEW = (
        By.XPATH, "//li//a[@href='https://www.youtube.com/channel/UCCzEy1yfgV5kwDbO3qnAEzw?view_as=subscriber']")
    USER_FEEDBACK = (By.XPATH, "//li//a[@href='singlepage/feedback'][text()=' Оставить отзыв о магазине']")
    INFO = (By.XPATH, "//h4[text()='Мои данные ']")
    NAME = (By.XPATH, "//p[text()='Имя']")
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    ADD_NAME = (By.XPATH, "//div[@class='cabmin-infa']//div[1]//a[text()='Добавить']")
    PASSWORD = (By.XPATH, "//p[text()='Пароль']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    EDIT_PASSWORD = (By.XPATH, "//div[@class='cabmin-infa']//div[2]//a[text()='Редактировать']")
    EMAIL = (By.XPATH, "//p[text()='Email']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    EDIT_EMAIL = (By.XPATH, "//div[@class='cabmin-infa']//div[3]//a[text()='Редактировать']")
    PHONE = (By.XPATH, "//p[text()='Номер телефона']")
    PHONE_INPUT = (By.XPATH, "//input[@name='phone']")
    ADD_PHONE = (By.XPATH, "//div[@class='cabmin-infa']//div[4]//a[text()='Добавить']")
    ADDRESS = (By.XPATH, "//p[text()='Адрес']")
    ADDRESS_INPUT = (By.XPATH, "//input[@name='address']")
    ADD_ADDRESS = (By.XPATH, "//div[@class='cabmin-infa']//div[5]//a[text()='Добавить']")


class CategoryPageLocators:
    TITLE_CATEGORY = (By.XPATH, "//h1[@class='mb-3 mt-0']")
    AVAILABILITY_YES = (By.XPATH, "//div[@class='shop_sidebar']//section[3]/div[2]//label[1]/I")
    AVAILABILITY_EXPECTED = (By.XPATH, "//div[@class='shop_sidebar']//section[3]/div[2]//label[2]/I")
    AVAILABILITY_UNDER_ORDER = (By.XPATH, "//div[@class='shop_sidebar']//section[3]/div[2]//label[3]/I")
    BREND_APPLE = (By.XPATH, "//div[@class='shop_sidebar']//section[1]/div[2]//label[1]/I")
    BREND_XAOMI = (By.XPATH, "//div[@class='shop_sidebar']//section[1]/div[2]//label[2]/I")
    BREND_HUAWEI = (By.XPATH, "//div[@class='shop_sidebar']//section[1]/div[2]//label[3]/I")
    BREND_MEIZU = (By.XPATH, "//div[@class='shop_sidebar']//section[1]/div[2]//label[4]/I")
    BREND_LENOVO = (By.XPATH, "//div[@class='shop_sidebar']//section[1]/div[2]//label[5]/I")
    BREND_SAMSUNG = (By.XPATH, "//div[@class='shop_sidebar']//section[1]/div[2]//label[6]/I")
    PRICE_RANGE_0_5 = (By.XPATH, "//div[@class='shop_sidebar']//section[2]/div[2]//label[1]/I")
    PRICE_RANGE_5_10 = (By.XPATH, "//div[@class='shop_sidebar']//section[2]/div[2]//label[2]/I")
    PRICE_RANGE_10_20 = (By.XPATH, "//div[@class='shop_sidebar']//section[2]/div[2]//label[3]/I")
    PRICE_RANGE_20_50 = (By.XPATH, "//div[@class='shop_sidebar']//section[2]/div[2]//label[4]/I")
    PRICE_RANGE_50_100 = (By.XPATH, "//div[@class='shop_sidebar']//section[2]/div[2]//label[5]/I")
    PRICE_RANGE_MORE_100 = (By.XPATH, "//div[@class='shop_sidebar']//section[2]/div[2]//label[6]/I")
    FINDING_ITEMS = (By.XPATH, "//div[@class='shop_product_count']")
    SORT = (By.XPATH, "//span[@class='sorting_text']//i[@class='fas fa-chevron-down']")
    SORT_DOWN = (By.XPATH, "//li[@class='shop_sorting_button sort-desc']")
    SORT_UP = (By.XPATH, "//li[@class='shop_sorting_button sort-asc']")
    MAIN_PAGE = (By.XPATH, "//ol//li[1]")
    CATEGORY_PAGE = (By.XPATH, "//ol//li[2]")
    PAGE_1_CATEGORY = (By.XPATH, "//ul[@class='pagination']//li[1]")
    PAGE_2_CATEGORY = (By.XPATH, "//ul[@class='pagination']//li[2]")
    PAGE_3_CATEGORY = (By.XPATH, "//ul[@class='pagination']//li[3]")
    PAGE_NAV_LINK_CATEGORY = (By.XPATH, "//ul[@class='pagination']//li[4]")


class SearchPageLocators:
    MAIN_PAGE_CATEGORY = (By.XPATH, "//ol[@class='breadcrumb']//li[1]")
    SEARCH_PAGE = (By.XPATH, "//ol[@class='breadcrumb']//li[2]")
    TITLE_SEARCH = (By.XPATH, "//h1[@class='pb-3']")
    PAGE_1_SEARCH = (By.XPATH, "//ul[@class='pagination']//li[1]")
    PAGE_2_SEARCH = (By.XPATH, "//ul[@class='pagination']//li[2]")
    PAGE_3_SEARCH = (By.XPATH, "//ul[@class='pagination']//li[3]")
    PAGE_NAV_LINK_SEARCH = (By.XPATH, "//ul[@class='pagination']//li[4]")
    PAGE_NAV_LINK_END_SEARCH = (By.XPATH, "//ul[@class='pagination']//li[4]")


class ProductPageLocators:
    pass

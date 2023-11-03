from selenium.webdriver.common.by import By


class BasePageLocators:
    # HEADER
    LOGIN_SIGNUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")
    FEEDBACK = (By.XPATH, "//a[@href='singlepage/feedback']")
    DELIVERY = (By.XPATH, "//a[@href='singlepage/delivery']")
    WARRANTY = (By.XPATH, "//a[@href='singlepage/warranty']")
    COOPERATION = (By.XPATH, "//a[text()='Детали сотрудничества']")
    CURRENCY = (By.XPATH, "//select[@id='currency']")
    CURRENCY_UAH = (By.XPATH, "//option[text()='UAH']")
    CURRENCY_USD = (By.XPATH, "//option[text()='USD']")
    CURRENCY_EUR = (By.XPATH, "//option[text()='EUR']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Поиск товара...']")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='header_search_button trans_300']")
    LOGO_ICON = (By.XPATH, "//img[@src='images/logo.png']")
    WISH = (By.XPATH, "//img[@src='images/heart.png']")
    WISH_COUNT = (By.XPATH, "//span[@class='qty_wish']")
    CART = (By.XPATH, "//img[@src='images/cart.png']")
    CART_COUNT = (By.XPATH, "//span[@class='qty_products']")

    HITS = (By.XPATH, "//span[text()='Хиты']")
    NEW = (By.XPATH, "//span[text()='Новинки']")
    SALE = (By.XPATH, "//span[text()='Скидки']")
    SAMSUNG = (By.XPATH, "//div[text()='Samsung']")
    SAMSUNG_A310 = (By.XPATH, "//a[text()='Samsung J701']")

    # FOOTER
    SUBSCRIBED_FOOTER = (By.XPATH, "//button[text()='Подписаться!']")
    SUBSCRIBED_EMAIL_FOOTER = (By.XPATH, "//input[@class='newsletter_input']")
    NEWSLETTER_ICON = (By.XPATH, "//img[@src='images/send.png']")
    NEWSLETTER_TITLE = (By.XPATH, "//div[@class='newsletter_title']")
    NEWSLETTER_TEXT = (By.XPATH, "//p[text()='...и узнайте о новинках и скидках первыми']")
    LOGO_FOOTER = (By.XPATH, "img[@src='images/logo-footer.png']")
    TELEGRAM_FOOTER = (By.XPATH, "//a[@href='https://t.me/casenik_com_ua']")
    TELEGRAM_PHONE = (By.XPATH, "//div[@class='footer_phone']")

    # BODY
    REFUND = (By.XPATH, "//div[@class='characteristics']//div[text()='Возврат средств']")
    FREE_DELIVERY = (By.XPATH, "//div[@class='characteristics']//div[text()='Бесплатная доставка']")
    DELAYED_PAYMENT = (By.XPATH, "//div[@class='characteristics']//div[text()='Отсрочка оплаты']")
    TECHNICAL_SUPPORT = (By.XPATH, "//div[@class='characteristics']//div[text()='Тех.поддержка']")

    ARRIVALS_VIEW_ALL = (By.XPATH, "//div[@class='arrivals_nav_container']//a[@href='main/showNew']")
    ARRIVALS_PREVIOUS = (By.XPATH, "//div[@class='arrivals_nav_container']//i[@class='fas fa-chevron-left']")
    ARRIVALS_NEXT = (By.XPATH, "//div[@class='arrivals_nav_container']//i[@class='fas fa-chevron-right']")
    ARRIVALS_TABLE = (By.XPATH, "//div[@class='product_panel panel active']")
    ARRIVALS_TABLE_8 = (
        By.XPATH,
        "//div[@class='product_name']//a[text()='Гидрогелевая бронепленка пленка Smartex Xiaomi Redmi Note 5A Prime']")

    HITS_VIEW_ALL = (By.XPATH, "//div[@class='best_nav_container']//a[@href='main/showHit']")
    HITS_PREVIOUS = (By.XPATH, "//div[@class='best_prev best_nav']//i[@class='fas fa-chevron-left']")
    HITS_NEXT = (By.XPATH, "//div[@class='best_next best_nav']//i[@class='fas fa-chevron-right']")
    HITS_TABLE = (By.XPATH, "//div[@class='bestsellers_panel panel active']//div[@class='slick-list draggable']")
    HITS_TABLE_5 = (
        By.XPATH,
        "//div[@data-slick-index='4']//a[text()='Компьютерная мышка HOCO DI04 BT Wireless Mouse Black']")

    TRENDS_PREVIOUS = (
        By.XPATH, "//div[@class='trends_prev trends_nav slick-arrow']//i[@class='fas fa-angle-left ml-auto]")
    TRENDS_NEXT = (
        By.XPATH, "//div[@class='trends_next trends_nav slick-arrow']//i[@class='fas fa-angle-right ml-auto']")
    TRENDS_TABLE_2 = (
        By.XPATH, "//div[@data-slick-index='7']//a[text()='Наушники HOCO ES20 PLUS AirPods2 Bluetooth/ White']")

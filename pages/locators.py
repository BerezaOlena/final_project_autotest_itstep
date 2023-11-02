from selenium.webdriver.common.by import By


class BasePageLocators:
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

    SUBSCRIBED_FOOTER = (By.XPATH, "//button[text()='Подписаться!']")
    SUBSCRIBED_EMAIL_FOOTER = (By.XPATH, "//input[@class='newsletter_input']")
    NEWSLETTER_ICON = (By.XPATH, "//img[@src='images/send.png']")
    NEWSLETTER_TITLE = (By.XPATH, "//div[@class='newsletter_title']")
    NEWSLETTER_TEXT = (By.XPATH, "//p[text()='...и узнайте о новинках и скидках первыми']")
    LOGO_FOOTER = (By.XPATH, "img[@src='images/logo-footer.png']")
    TELEGRAM_FOOTER = (By.XPATH, "//a[@href='https://t.me/casenik_com_ua']")
    TELEGRAM_PHONE = (By.XPATH, "//div[@class='footer_phone']")


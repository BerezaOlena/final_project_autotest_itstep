from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")
    FEEDBACK = (By.XPATH, "//a[text()='Обратная связь']")  # //a[@href="singlepage/feedback"]
    DELIVERY = (By.XPATH, "//a[text()='Доставка']")  # //a[@href="singlepage/delivery"]
    WARRANTY = (By.XPATH, "//a[text()='Гарантия']")  # //a[@href="singlepage/warranty"]
    COOPERATION = (By.XPATH, "//a[text()='Детали сотрудничества']")  # //i[@class="fas fa-chevron-down"]
    CURRENCY = (By.XPATH, "//select[@id='currency']")
    CURRENCY_UAH = (By.XPATH, "//option[text()='UAH']")
    CURRENCY_USD = (By.XPATH, "//option[text()='USD']")
    CURRENCY_EUR = (By.XPATH, "//option[text()='EUR']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Поиск товара...']")
    # SEARCH_INPUT = (By.XPATH, "//input[@class='header_search_input tt-input']")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='header_search_button trans_300']")
    LOGO_ICON = (By.XPATH, "//img[@src='images/logo.png']")
    WISH = (By.XPATH, "//img[@src='images/heart.png']")
    WISH_COUNT = (By.XPATH, "//span[@class='qty_wish']")
    CART = (By.XPATH, "//img[@src='images/cart.png']")
    CART_COUNT = (By.XPATH, "//span[@class='qty_products']")

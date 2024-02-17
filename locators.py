from selenium.webdriver.common.by import By


class TestLocators:

    # Кнопка Личный кабинет
    PROFILE_LINK = By.XPATH, ".//a[(@href='/account')]"
    # Кнопка Конструктор
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[contains(text(),'Конструктор')]"
    # Кнопка Логотип
    LOGO_LINK = By.XPATH, ".//a[(@href='/')]"

    # Кнопка входа на главной странице
    LOGIN_BUTTON_DASHBOARD = By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]"
    # Кнопка входа на странице профиля
    LOGIN_BUTTON_PROFILE = By.XPATH, ".//button[contains(text(),'Войти')]"
    # Кнопка входа на странице регистрации и восстановления пароля
    LOGIN_LINK_REGISTRATION_RESET_FORM = By.XPATH, ".//a[(@href='/login')]"

    # Кнопка Выход в профиле
    LOGOUT_BUTTON_PROFILE = By.XPATH, ".//button[contains(text(),'Выход')]"
    # Кнопка Профиль в личном кабинете
    PROFILE_BUTTON_PROFILE = By.XPATH, ".//a[(@href='/account/profile')]"
    # Поле Имя в профиле
    NAME_FIELD_PROFILE = By.XPATH, ".//input[(@name='Name')]"

    # Кнопка Булки
    BUNS_TAB = By.XPATH, ".//span[contains(text(),'Булки')]"
    # Кнопка Соусы
    SAUCES_TAB = By.XPATH, ".//span[contains(text(),'Соусы')]"
    # Кнопка Начинки
    FILLINGS_TAB = By.XPATH, ".//span[contains(text(),'Начинки')]"

    # Кнопка Булки
    BUNS_DIV = By.XPATH, ".//span[contains(text(),'Булки')]/parent::div"
    # Кнопка Соусы
    SAUCES_DIV = By.XPATH, ".//span[contains(text(),'Соусы')]/parent::div"
    # Кнопка Начинки
    FILLINGS_DIV = By.XPATH, ".//span[contains(text(),'Начинки')]/parent::div"

    # Заголовок Булки
    BUNS_HEADER = By.XPATH, ".//h2[contains(text(),'Булки')]"
    # Заголовок Соусы
    SAUCES_HEADER = By.XPATH, ".//h2[contains(text(),'Соусы')]"
    # Заголовок Начинки
    FILLINGS_HEADER = By.XPATH, ".//h2[contains(text(),'Начинки')]"

    # Ссылка регистрации для нового пользователя
    REGISTER_LINK = By.XPATH, ".//a[(@href='/register')]"
    # Сообщение об ошибке при регистрации
    REGISTER_ERROR_MESSAGE = By.XPATH, ".//p[(@class='input__error text_type_main-default')]"

    # поле ввода имени при регистрации
    INPUT_NAME = By.XPATH, "//*[text()='Имя']/following-sibling::input"
    # поле ввода Логина при регистрации
    REGISTRATION_NAME = By.XPATH, "//*[text()='Имя']/following-sibling::input"
    # поле ввода email при регистрации
    INPUT_EMAIL = By.XPATH, "//*[text()='Email']/following-sibling::input"

    # поле ввода пароля
    INPUT_PASSWORD = By.XPATH, ".//input[(@type='password')]"

    # поле ввода email для входа
    LOGIN_EMAIL = By.XPATH, ".//input[(@name='name')]"

    # кнопка Зарегистрироваться
    REGISTER_BUTTON = By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]"
    # кнопка Войти на форме логина
    LOGIN_FORM_LOGIN_BUTTON = By.XPATH, ".//button[contains(text(),'Войти')]"

    # заголовок Соберите бургер
    FORM_BURGER_TEXT = By.XPATH, ".//h1[contains(text(),'Соберите бургер')]"

    @staticmethod
    def gen_user_name_link(user):
        PROFILE_USER_NAME_FIELD = By.XPATH, f".//input[(@value ='{user.get('name')}')]"
        return PROFILE_USER_NAME_FIELD

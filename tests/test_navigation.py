from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestNavigation:

    def test_dashboard_to_profile_link(self, driver, registered_user):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                TestLocators.LOGIN_BUTTON_PROFILE
            ))

        # Логин
        driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(registered_user.get('email'))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(registered_user.get('password'))
        driver.find_element(*TestLocators.LOGIN_FORM_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        # Переход в личный кабинет
        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.PROFILE_BUTTON_PROFILE
        ))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_profile_to_constructor_link(self, driver, registered_user):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGIN_BUTTON_PROFILE
        ))

        # Логин
        driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(registered_user.get('email'))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(registered_user.get('password'))
        driver.find_element(*TestLocators.LOGIN_FORM_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        # Переход в личный кабинет
        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.PROFILE_BUTTON_PROFILE
        ))

        # Переход в конструктор
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_profile_to_dashboard_link(self, driver, registered_user):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGIN_BUTTON_PROFILE
        ))

        # Логин
        driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(registered_user.get('email'))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(registered_user.get('password'))
        driver.find_element(*TestLocators.LOGIN_FORM_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        # Переход в личный кабинет
        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.PROFILE_BUTTON_PROFILE
        ))

        # Переход на главную страницу
        driver.find_element(*TestLocators.LOGO_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
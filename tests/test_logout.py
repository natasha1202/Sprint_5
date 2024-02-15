from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestLogout:

    def test_logout_from_profile(self, driver, registered_user):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        # Логин
        driver.find_element(*TestLocators.LOGIN_BUTTON_DASHBOARD).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGIN_FORM_LOGIN_BUTTON
        ))

        driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(registered_user.get('email'))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(registered_user.get('password'))
        driver.find_element(*TestLocators.LOGIN_FORM_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        # Выход через страницу профиля
        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGOUT_BUTTON_PROFILE
        ))
        driver.find_element(*TestLocators.LOGOUT_BUTTON_PROFILE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGIN_FORM_LOGIN_BUTTON
        ))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
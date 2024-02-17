from locators import TestLocators

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_registration_correct_user_success(self, driver, new_user):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        # Регистрация
        driver.find_element(*TestLocators.PROFILE_LINK).click()
        driver.find_element(*TestLocators.REGISTER_LINK).click()
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(new_user.get('name'))
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(new_user.get('email'))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(new_user.get('password'))
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGIN_FORM_LOGIN_BUTTON))

        # Логин
        driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(new_user.get('email'))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(new_user.get('password'))
        driver.find_element(*TestLocators.LOGIN_FORM_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT))

        # Проверка имени пользователя в личном кабинете
        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.NAME_FIELD_PROFILE))

        assert driver.find_element(*TestLocators.NAME_FIELD_PROFILE).get_attribute('value') == new_user.get('name')

    def test_registration_too_short_password(self, driver, not_correct_user):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        driver.find_element(*TestLocators.PROFILE_LINK).click()
        driver.find_element(*TestLocators.REGISTER_LINK).click()
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(not_correct_user.get('name'))
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(not_correct_user.get('email'))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(not_correct_user.get('password'))
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        assert driver.find_element(*TestLocators.REGISTER_ERROR_MESSAGE).text == "Некорректный пароль"

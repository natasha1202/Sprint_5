from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from page_url import PageUrl


class TestLogin:

    def test_login_from_dashboard_success(self, driver, registered_user):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        driver.find_element(*TestLocators.LOGIN_BUTTON_DASHBOARD).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGIN_FORM_LOGIN_BUTTON
        ))

        # Логин
        driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(registered_user.get('email'))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(registered_user.get('password'))
        driver.find_element(*TestLocators.LOGIN_FORM_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        # Проверка имени авторизованного пользователя
        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
           TestLocators.NAME_FIELD_PROFILE
        ))
        assert (driver.find_element(*TestLocators.NAME_FIELD_PROFILE).get_attribute('value')
                == registered_user.get('name'))

    def test_login_from_profile_success(self, driver, registered_user):
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

        # Проверка имени авторизованного пользователя
        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                TestLocators.NAME_FIELD_PROFILE
            ))
        assert (driver.find_element(*TestLocators.NAME_FIELD_PROFILE).get_attribute('value')
                == registered_user.get('name'))

    def test_login_from_registration_page_success(self, driver, registered_user):
        driver.get(PageUrl.REGISTRATION_PAGE_URL)

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                TestLocators.LOGIN_LINK_REGISTRATION_RESET_FORM
            ))

        driver.find_element(*TestLocators.LOGIN_LINK_REGISTRATION_RESET_FORM).click()

        # Логин
        driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(registered_user.get('email'))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(registered_user.get('password'))
        driver.find_element(*TestLocators.LOGIN_FORM_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                TestLocators.FORM_BURGER_TEXT
            ))

        # Проверка имени авторизованного пользователя
        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                TestLocators.NAME_FIELD_PROFILE
            ))
        assert (driver.find_element(*TestLocators.NAME_FIELD_PROFILE).get_attribute('value')
                == registered_user.get('name'))

    def test_login_from_reset_page_success(self, driver, registered_user):
        driver.get(PageUrl.RESET_PAGE_URL)

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                TestLocators.LOGIN_LINK_REGISTRATION_RESET_FORM
            ))

        driver.find_element(*TestLocators.LOGIN_LINK_REGISTRATION_RESET_FORM).click()

        # Логин
        driver.find_element(*TestLocators.LOGIN_EMAIL).send_keys(registered_user.get('email'))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(registered_user.get('password'))
        driver.find_element(*TestLocators.LOGIN_FORM_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                TestLocators.FORM_BURGER_TEXT
            ))

        # Проверка имени авторизованного пользователя
        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                TestLocators.NAME_FIELD_PROFILE
            ))
        assert (driver.find_element(*TestLocators.NAME_FIELD_PROFILE).get_attribute('value')
                == registered_user.get('name'))

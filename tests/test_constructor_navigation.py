from locators import TestLocators

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorNavigation:

    def test_navigation_to_buns(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        driver.find_element(*TestLocators.FILLINGS_TAB).click()
        driver.find_element(*TestLocators.BUNS_TAB).click()

        assert driver.find_element(*TestLocators.BUNS_HEADER).is_displayed()

    def test_navigation_to_sauces(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        driver.find_element(*TestLocators.FILLINGS_TAB).click()
        driver.find_element(*TestLocators.SAUCES_TAB).click()

        assert driver.find_element(*TestLocators.SAUCES_HEADER).is_displayed()

    def test_navigation_to_fillings(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FORM_BURGER_TEXT
        ))

        driver.find_element(*TestLocators.FILLINGS_TAB).click()
        assert driver.find_element(*TestLocators.FILLINGS_HEADER).is_displayed()

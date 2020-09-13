from Base import BasePage
from selenium.webdriver.common.by import By


class DOU_page_locators:
    LOCATOR_JOBS_BUTTON = (By.XPATH, "//a[@href = 'https://jobs.dou.ua/']")
    LOCATOR_COMPANIES_BUTTON = (By.CLASS_NAME, "comp")
    LOCATOR_SEARCH_FIELD_BY_CLASS_NAME = (By.CLASS_NAME, "company")
    LOCATOR_SEARCH_FIELD_BY_PLACEHOLDER = (
        By.XPATH, "//input[@placeholder = 'Название компании, город или страна']")
    LOCATOR_SEARCH_FIELD_BY_CSS_SELECTOR = (
        By.CSS_SELECTOR, "input[name='name']")
    LOCATOR_SEARCH_BUTTON = (By.CLASS_NAME, "btn-search")
    LOCATOR_COMPANY_NAME = (By.CLASS_NAME, "cn-a")
    LOCATOR_CITY_LIST = (By.CLASS_NAME, "city")


class Search_company_page(BasePage):
    def click_jobs_button(self):
        return self.find_element(DOU_page_locators.LOCATOR_JOBS_BUTTON, time=2).click()

    def click_companies_button(self):
        return self.find_element(DOU_page_locators.LOCATOR_COMPANIES_BUTTON, time=2).click()

    def enter_word(self, word, locator):
        search_field = self.find_element(
            getattr(DOU_page_locators, 'LOCATOR_SEARCH_FIELD_BY_' + str(locator)), time=2)
        search_field.click()
        search_field.clear()
        search_field.send_keys(word)
        return search_field

    def click_search_button(self):
        return self.find_element(DOU_page_locators.LOCATOR_SEARCH_BUTTON, time=2).click()

    def search_company_name(self):
        elems = self.find_elements(
            DOU_page_locators.LOCATOR_COMPANY_NAME, time=2)
        elem_texts = [i.text for i in elems]
        return elem_texts

    def search_city_list(self):
        elems = self.find_elements(DOU_page_locators.LOCATOR_CITY_LIST, time=2)
        elem_texts = [i.text for i in elems]
        return elem_texts

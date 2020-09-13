import pytest
from selenium import webdriver
from Page import Search_company_page
from googletrans import Translator


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="resourses/chromedriver")
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(scope="function")
def translator():
    transl = Translator()
    return transl


@pytest.fixture(scope="session")
def get_to_companies_page(browser):
    companies_page = Search_company_page(browser)
    companies_page.go_to_site()
    companies_page.click_jobs_button()
    companies_page.click_companies_button()
    return companies_page

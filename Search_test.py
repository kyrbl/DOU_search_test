import pytest
import string
from selenium.common.exceptions import TimeoutException


@pytest.mark.parametrize("word, param_locator", [("Genesis","CLASS_NAME"), ("cOklum","CLASS_NAME"), ("!Genesis~","PLACEHOLDER"), ("Gen!esis","PLACEHOLDER"), ("Genеsіs", "CSS_SELECTOR"), ("Genesis11", "CSS_SELECTOR"), ("GENESIS", "CSS_SELECTOR"), ])
def test_company_search(get_to_companies_page, word, param_locator):
    get_to_companies_page.enter_word(word, param_locator)
    get_to_companies_page.click_search_button()
    try:
        companies = get_to_companies_page.search_company_name()
    except TimeoutException:
        pytest.fail("No such company!!!!")
    word = word.translate(str.maketrans(
        '', '', string.punctuation)).lower()
    for i in companies:
        assert word in i.lower()


@pytest.mark.parametrize("word, param_locator", [("Київ", "CSS_SELECTOR"), ("Киев", "CLASS_NAME"), ("Kiev", "CLASS_NAME"), ("Кровогорад", "PLACEHOLDER")])
def test_region_search(get_to_companies_page, word, param_locator, translator):
    get_to_companies_page.enter_word(word, param_locator)
    get_to_companies_page.click_search_button()
    try:
        regions = get_to_companies_page.search_city_list()
    except TimeoutException:
        pytest.fail("No such region!!!!")
    word = translator.translate(word)
    word = word.text.translate(str.maketrans(
        '', '', string.punctuation)).lower()

    for i in regions:
        i = translator.translate(i)

        assert word in i.text.translate(
            str.maketrans('', '', string.punctuation)).lower()

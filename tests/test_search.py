import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from playwright.sync_api import expect, Page
import allure

@allure.title("Search for phrase on DuckDuckGo")
@allure.description("This test attempts to search for a phrase on DuckDuckGo search engine")
@allure.tag("UI", "POSITIVE")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.webtest
def test_basic_duckduckgo_search(
    page: Page,
    search_page: DuckDuckGoSearchPage,
    result_page: DuckDuckGoResultPage) -> None:

    # Given the DuckDuckGo home page is displayed
    search_page.load()
    png_bytes = page.screenshot()
    allure.attach(
        png_bytes,
        name="Duck Duck Go Home Page loaded",
        attachment_type=allure.attachment_type.PNG
    )

    # When the user searches for a phrase
    search_page.search('React Native')

    # Then the search result query is the phrase
    expect(result_page.search_input).to_have_value('React Native')

    # And the search result links pertain to the phrase
    png_bytes = page.screenshot()
    allure.attach(
        png_bytes,
        name="Search results",
        attachment_type=allure.attachment_type.PNG
    )
    assert result_page.result_link_titles_contain_phrase('React Native')

    # And the search result title contains the phrase
    expect(page).to_have_title('React Native at DuckDuckGo')
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from playwright.sync_api import expect, Page

def test_basic_duckduckgo_search(
    page: Page,
    search_page: DuckDuckGoSearchPage,
    result_page: DuckDuckGoResultPage) -> None:

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for a phrase
    search_page.search('Symphony Solutions')

    # Then the search result query is the phrase
    expect(result_page.search_input).to_have_value('Symphony Solutions')

    # And the search result links pertain to the phrase
    assert result_page.result_link_titles_contain_phrase('Symphony')

    # And the search result title contains the phrase
    expect(page).to_have_title('Symphony Solutions at DuckDuckGo')
import pytest
from playwright.async_api import Page
from .utils.utils import goToPage, clickTab, getTitles, compareTitles, getElementsInRange 

@pytest.mark.anyio("asyncio")
async def testSolution(page: Page):
    await goToPage(page, "https://wfirma.pl")
    await clickTab(page, ".nav-link:text('Rozwiązania')")
    actualTitles = await getTitles(page, ".item-title")
    expectedTitles: list[str] = ['Fakturowanie i sprzedaż', 'Kadry i Płace', 'Program dla Biur Rachunkowych', 'Księgowość online', 'Magazyn', 'Pełna księgowość online']
    result = getElementsInRange(actualTitles, "4:10")
    compareTitles(result, expectedTitles)


# def test_tab_navigation(page: Page):
#     page.goto("https://wfirma.pl")
#     currentTab = page.locator('.nav-link:text("Rozwiązania")')
#     currentTab.click()
#     expected_titles = ['Fakturowanie i sprzedaż', 'Kadry i Płace', 'Program dla Biur Rachunkowych', 'Księgowość online', 'Magazyn', 'Pełna księgowość online']
#     actual_titles = page.locator(".item-title").all_text_contents()
#     actual_titles = [title.replace("\xa0", " ").strip() for title in actual_titles]
#     array_items = actual_titles[4:10]
#     assert array_items == expected_titles, f"Expected {expected_titles} but got {array_items}"

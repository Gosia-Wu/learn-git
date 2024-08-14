import pytest
from playwright.async_api import Page
from .utils.utils import goToPage, clickTab, getTitles, compareTitles, getElementsInRange

@pytest.mark.anyio("asyncio")
async def testHelp(page: Page):
    await goToPage(page, "https://wfirma.pl")
    await clickTab(page, f".nav-link:text('Pomoc')")
    actualTitles = await getTitles(page, ".item-title")
    expectedTitles: list[str] = ['Centrum Pomocy', 'Wsparcie przez Asystenta', 'Poradnik Przedsiębiorcy', 'Blog wFirma']
    result = getElementsInRange(actualTitles, "11:")
    compareTitles(result, expectedTitles)
   

# def test_help_navigation(page: Page):
#     page.goto("https://wfirma.pl")
#     currentTab = page.locator('.nav-link:text("Pomoc")')
#     currentTab.click()
#     expected_titles = ['Centrum Pomocy', 'Wsparcie przez Asystenta', 'Poradnik Przedsiębiorcy', 'Blog wFirma']
#     actual_titles = page.locator(".item-title").all_text_contents()
#     actual_titles = [title.replace("\xa0", " ").strip() for title in actual_titles]
#     array_items = actual_titles[11:]
#     assert array_items == expected_titles, f"Expected {expected_titles} but got {array_items}"
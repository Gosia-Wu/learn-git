from playwright.sync_api import Page, expect

# from test_.utils.utils import onSingleTabClick, goToTestPage

def test_tab_navigation(page: Page):
    # onSingleTabClick(page, "Dla kogo")
    # megaContainer = page.locator("#mega-menu > .menu-content")
    page.goto("https://wfirma.pl")
    currentTab = page.locator('.nav-link:text("Rozwiązania")')
    currentTab.click()
    expected_titles = ['Fakturowanie i sprzedaż', 'Kadry i Płace', 'Program dla Biur Rachunkowych', 'Księgowość online', 'Magazyn', 'Pełna księgowość online']
    actual_titles = page.locator(".item-title").all_text_contents()
    actual_titles = [title.replace("\xa0", " ").strip() for title in actual_titles]
    array_items = actual_titles[4:10]
    assert array_items == expected_titles, f"Expected {expected_titles} but got {array_items}"

   
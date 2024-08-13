from playwright.sync_api import Page, expect

# from test_.utils.utils import onSingleTabClick, goToTestPage

def test_navigation(page: Page):
    # onSingleTabClick(page, "Dla kogo")
    # megaContainer = page.locator("#mega-menu > .menu-content")
    page.goto("https://wfirma.pl")
    currentTab = page.locator(f"text=Dla kogo")
    currentTab.click()
    expected_titles = ['Samozatrudnieni', 'Małe firmy', "Spółki i NGO'sy"]
    actual_titles = page.locator(".item-title").all_text_contents()
    actual_titles = [title.replace("\xa0", " ").strip() for title in actual_titles]
    first_three_items = actual_titles[:3]
    assert first_three_items == expected_titles, f"Expected {expected_titles} but got {first_three_items}"

   
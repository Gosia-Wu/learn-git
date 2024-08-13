from playwright.sync_api import Page, expect

# from test_.utils.utils import onSingleTabClick, goToTestPage

def test_help_navigation(page: Page):
    # onSingleTabClick(page, "Dla kogo")
    # megaContainer = page.locator("#mega-menu > .menu-content")
    page.goto("https://wfirma.pl")
    currentTab = page.locator('.nav-link:text("Pomoc")')
    currentTab.click()
    expected_titles = ['Centrum Pomocy', 'Wsparcie przez Asystenta', 'Poradnik Przedsiębiorcy', 'Blog wFirma']
    actual_titles = page.locator(".item-title").all_text_contents()
    actual_titles = [title.replace("\xa0", " ").strip() for title in actual_titles]
    array_items = actual_titles[11:]
    assert array_items == expected_titles, f"Expected {expected_titles} but got {array_items}"

   
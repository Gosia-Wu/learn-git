from playwright.sync_api import Page, expect

def test_navigation(page: Page):
    page.goto("https://wfirma.pl")
    navTab = page.locator("text=Dla kogo")
    navTab.click()
    megaContainer = page.locator("#mega-menu")
    expect(megaContainer).to_contain_text("Samozatrudnieni")
    expect(megaContainer).to_contain_text("Małe firmy")
    expect(megaContainer).to_contain_text("Spółki i NGO'sy")
    expect(megaContainer).to_contain_text("Biura rachunkowe")
    
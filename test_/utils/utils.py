from playwright.sync_api import Page

def goToTestPage(page:Page, website):
    page.goto(website)

def onSingleTabClick(page: Page, tabName):
    currentTab = page.locator(f"text={tabName}")
    currentTab.click()
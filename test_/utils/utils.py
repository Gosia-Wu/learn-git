from playwright.async_api import Page

async def goToPage(page: Page, url: str):
    await page.goto(url)

async def clickTab(page: Page, tabName: str):
    currentTab = page.locator(f"text={tabName}")
    await currentTab.click()

async def getTitles(page: Page, selector: str):
    elements = page.locator(selector)
    titles = await elements.all_text_contents()
    return [title.replace("\xa0", " ").strip() for title in titles]

def compareTitles(actualElements: list[str], expectedElements: list[str], range):
     actualResult = actualElements[:range]
     assert actualResult == expectedElements, f"Expected {expectedElements} but got {actualResult}"


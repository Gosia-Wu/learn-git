from playwright.async_api import Page

async def goToPage(page: Page, url: str):
    await page.goto(url)

async def clickTab(page: Page, tabName: str):
    currentTab = page.locator(tabName)
    await currentTab.click()

async def getTitles(page: Page, selector: str):
    elements = page.locator(selector)
    titles = await elements.all_text_contents()
    return [title.replace("\xa0", " ").strip() for title in titles]

def compareTitles(actualElements: list[str], expectedElements: list[str]):
     actualResult = actualElements
     assert actualResult == expectedElements, f"Expected {expectedElements} but got {actualResult}"

def parseRange(rangeStr: str):
    # Rozbicie stringa na start i end
    startStr, endStr = rangeStr.split(":")
    start = int(startStr) if startStr else None
    end = int(endStr) if endStr else None
    return slice(start, end)

def getElementsInRange(elements: list[str], rangeStr: str) -> list[str]:
    # Parsowanie stringa i tworzenie obiektu slice
    elementSlice = parseRange(rangeStr)
    return elements[elementSlice]

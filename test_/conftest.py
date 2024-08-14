import pytest
from playwright.async_api import async_playwright, Browser, BrowserContext, Page, Playwright
from typing import AsyncGenerator

@pytest.fixture(scope="module")
async def playwright_instance() -> AsyncGenerator[Playwright, None]:
    async with async_playwright() as p:
        yield p

@pytest.fixture(scope="module")
async def browser(playwright_instance: Playwright) -> AsyncGenerator[Browser, None]:
    browser = await playwright_instance.chromium.launch(headless=False)
    yield browser
    await browser.close()

@pytest.fixture(scope="module")
async def context(browser: Browser) -> AsyncGenerator[BrowserContext, None]:
    context = await browser.new_context()
    yield context
    await context.close()

@pytest.fixture(scope="module")
async def page(context: BrowserContext) -> AsyncGenerator[Page, None]:
    page = await context.new_page()
    yield page
    await page.close()
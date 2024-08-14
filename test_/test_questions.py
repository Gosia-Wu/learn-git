import pytest
from playwright.async_api import Page
from .utils.utils import goToPage, clickTab, getTitles, compareTitles

@pytest.mark.anyio("asyncio")
async def testQuestions(page: Page):
    await goToPage(page, "https://wfirma.pl")
    await clickTab(page, f"text=Najczęstsze pytania:")
    actualTitles = await getTitles(page, "li > h4")
    expectedTitles: list[str] = ['Czy system jest łatwy w obsłudze?', 'Czy oprogramowanie pozwala na rozliczenie się z urzędem skarbowym i ZUS?', 'Chcę przenieść księgowość w trakcie roku - czy jest to możliwe?', 'Jak wystawić fakturę w walucie obcej?', 'Jak wprowadzić prywatny samochód do środków trwałych firmy?']
    compareTitles(actualTitles, expectedTitles)



# def test_query_navigation(page: Page):
#     page.goto("https://wfirma.pl")
#     faq = page.locator('text=Najczęstsze pytania:')
#     expected_questions = ['Czy system jest łatwy w obsłudze?', 'Czy oprogramowanie pozwala na rozliczenie się z urzędem skarbowym i ZUS?', 'Chcę przenieść księgowość w trakcie roku - czy jest to możliwe?', 'Jak wystawić fakturę w walucie obcej?', 'Jak wprowadzić prywatny samochód do środków trwałych firmy?']
#     actual_questions = page.locator("li > h4").all_text_contents()
#     actual_questions = [title.replace("\xa0", " ").strip() for title in actual_questions]
#     assert actual_questions == expected_questions, f"Expected {expected_questions} but got {actual_questions}"
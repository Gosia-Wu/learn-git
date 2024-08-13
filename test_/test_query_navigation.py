from playwright.sync_api import Page, expect

# from test_.utils.utils import onSingleTabClick, goToTestPage

def test_query_navigation(page: Page):
    # onSingleTabClick(page, "Dla kogo")
    # megaContainer = page.locator("#mega-menu > .menu-content")
    page.goto("https://wfirma.pl")
    faq = page.locator('text=Najczęstsze pytania:')
    expected_questions = ['Czy system jest łatwy w obsłudze?', 'Czy oprogramowanie pozwala na rozliczenie się z urzędem skarbowym i ZUS?', 'Chcę przenieść księgowość w trakcie roku - czy jest to możliwe?', 'Jak wystawić fakturę w walucie obcej?', 'Jak wprowadzić prywatny samochód do środków trwałych firmy?']
    actual_questions = page.locator("li > h4").all_text_contents()
    actual_questions = [title.replace("\xa0", " ").strip() for title in actual_questions]
    # array_items = actual_questions[11:]
    assert actual_questions == expected_questions, f"Expected {expected_questions} but got {actual_questions}"

   
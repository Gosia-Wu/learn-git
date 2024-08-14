import pytest
from playwright.async_api import Page
from .utils.utils import goToPage, clickTab, getTitles, compareTitles

# Funkcja po refaktoryzacji, rozbicie funkcji na pomniejsze funkcje, wyniesione do folderu utils (zbiór funkcji
# pomocniczych, reużywalnych):
# - goToPage
# - clickTab
# - getTitles
# - compareTitles


@pytest.mark.anyio("asyncio")
async def test_navigation(page: Page):
    await goToPage(page, "https://wfirma.pl")
    await clickTab(page, "Dla kogo")
    actualTitles = await getTitles(page, ".item-title")
    expected_titles: list[str] = ["Samozatrudnieni", "Małe firmy", "Spółki i NGO'sy"]
    compareTitles(actualTitles, expected_titles, 3)
   

# Funkcja testu przed refaktoryzacją

# def test_navigation(page: Page):
#     page.goto("https://wfirma.pl")
#     currentTab = page.locator(f"text=Dla kogo")
#     currentTab.click()
#     expected_titles = ['Samozatrudnieni', 'Małe firmy', "Spółki i NGO'sy"]
#     actual_titles = page.locator(".item-title").all_text_contents()
#     actual_titles = [title.replace("\xa0", " ").strip() for title in actual_titles]
#     first_three_items = actual_titles[:3]
#     assert first_three_items == expected_titles, f"Expected {expected_titles} but got {first_three_items}"

# 1. Wchodzimy na stronę używając page.goto przekazując adres strony.
# 2. Lokalizujemy zakładkę w nawigacji (menu) i ją klikamy.
# 3. Deklarujemy oczekiwane tytuły. Wyciągamy wszystkie tytuły pod menu w ramach klikniętej zakładki + obsługujemy
#    odpowiedni format tekstu (białe #  znaki -np. spacja, itp.).
# 4. Porównujemy oczekiwane tytuły z tytułami pobranymi ze strony. Oczekujemy, że wynik zwróci prawdę, czyli tablice
#    tytułów będą takie same.
def parse_range(range_str: str):

    # Rozbicie stringa na start i end
    start_str, end_str = range_str.split(":")
    start = int(start_str) if start_str else None
    end = int(end_str) if end_str else None
    return slice(start, end)

def get_elements_in_range(elements: List[str], range_str: str) -> List[str]:
    # Parsowanie stringa i tworzenie obiektu slice
    element_slice = parse_range(range_str)
    return elements[element_slice]

# Przykładowe użycie
titles = ["Title1", "Title2", "Title3", "Title4", "Title5"]
result = get_elements_in_range(titles, "2:4")
print(result)  # Wynik: ['Title3', 'Title4']

Jak to działa

    parse_range(range_str: str): Funkcja przyjmuje string w formacie "start:end", rozbija go na start i end, a następnie zwraca obiekt slice.
    get_elements_in_range(elements: List[str], range_str: str): Ta funkcja przyjmuje listę oraz string z zakresem, przekształca string na obiekt slice, a następnie używa go do wyciągnięcia odpowiednich elementów z listy.

Przykłady użycia

    Pobranie elementów od 3 do 4 (indeksy 2 i 3):

    result = get_elements_in_range(titles, "2:4")

    Pobranie pierwszych 3 elementów:

    result = get_elements_in_range(titles, ":3")

    Pobranie wszystkich elementów od 4 do końca:

    result = get_elements_in_range(titles, "4:")

Ogółem mówiąc: 

Choć Python nie obsługuje bezpośrednio indeksowania za pomocą stringów w formacie "start:end", możesz łatwo osiągnąć taki efekt, przekształcając string na obiekt slice za pomocą funkcji. Jest to elastyczne rozwiązanie, które pozwala na prostą manipulację listami na podstawie stringów z zakresem.
# Zadanie 20: Walidacja typów danych w funkcji

# Utwórz funkcję add_numbers, która przyjmuje dwa argumenty.
#  Funkcja powinna zwracać ich sumę, ale przed wykonaniem obliczeń sprawdź, 
#  czy oba argumenty są typu int lub float. Jeśli nie, funkcja powinna zwrócić błąd.

# tworzę funkcję
# number_1 = input("Type a number: ")
# number_2 = input("Type another number: ")
# jeśli użytkownik będzie wprowadzał dane poprzez input, to zawsze będzie to string, 
# inputy trzeba więc zawsze zamienić na integer lub float

def add_numbers(number_1, number_2):
    if (isinstance(number_1, (int,float)) & isinstance(number_2, (int,float))):
        sum = number_1 + number_2
        print("Suma wynosi:" + " " + str(sum))
    else:
        print("Błąd. Jeden albo oba ze skladników sumy nie są typu integer ani float")

add_numbers(10, 14)
add_numbers(5,"żelazo")
add_numbers(5.7, 14.2)
add_numbers("jabłko", "banan")
add_numbers(-1114, 578.3)
# Zadanie 16: Transformacja danych - listy do słowników

# Utwórz dwie listy: names = ["Ala", "Ola", "Ela"] oraz ages = [25, 30, 22].
# Stwórz słownik, gdzie kluczami będą imiona z listy names, a wartościami odpowiednie wartości
#  z listy ages.

# tworzę listy
names = ["Ala", "Ola", "Ela"]
ages = [25, 30, 22]

# korzystam z funkcji wbudowanej (built-in function): zip, ktora łączy w tuple, pary elementów z dwóch zbiorów
dictionary = dict(zip(names, ages))
print(dictionary)
# Zadanie 18: Przekształcanie tuple na słownik

# Utwórz tuple z parami klucz-wartość (np. ("name", "Gosia"), ("age", 22))
#  i przekształć je na słownik. Wydrukuj wynik.

# tworzę tuple
tuple_pair1 = ("name", "Gosia")
tuple_pair2 = ("age", 22)

# tworzę słownik za pomocą funkcji dict()
# do tej funkcji przekazuje listę krotek (tuples),
#  a ona automatycznie przekształci je w słownik, gdzie pierwszy element każdej krotki staje się kluczem, 
# a drugi wartością

dictionary = dict([tuple_pair1, tuple_pair2])
print(dictionary)
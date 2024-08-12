# Zadanie 14: Praca z setami - różnice i przecinania

# Utwórz dwa sety: set_a = {1, 2, 3, 4} oraz set_b = {3, 4, 5, 6}. 
# Wydrukuj różnicę między setami oraz ich przecięcie.

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Dla sprawdzenia drukuję oba sety
print(set_a)
print(set_b)

# Różnica między set_a i set_b
print(set_a.difference(set_b))
# albo
print(set_a - set_b)

# Różnica między set_b i set_a
print(set_b.difference(set_a))
#albo
print(set_b - set_a)

# Przecięcie (inaczej: część wspólna) set_a i set_b
print(set_a.intersection(set_b))
# ponizszy zapis powinien dać ten sam wynik, co linijka wyżej:
print(set_b.intersection(set_a))
# ponizszy zapis jest tożsamy z oboma wyżej:
print(set_a & set_b)
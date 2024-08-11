# Zadanie 17: Tworzenie funkcji z domyślnymi argumentami

# Utwórz funkcję greet, która przyjmuje jeden argument - imię. Funkcja powinna wydrukować powitanie. 
# Jeśli argument nie zostanie podany, funkcja powinna przyjąć wartość domyślną "Gosia".

# tworzę funkcję
def greet_function(name = "Gosia"):
    print("Hello" + " " + name + "!")

# wywoluję funkcję określając argument
greet_function("Łukasz")
greet_function("Karolina")

# wywoluję funkcję nie określając argumentu, wówczas powinna być zasosowana jego wartość domyślna
greet_function()
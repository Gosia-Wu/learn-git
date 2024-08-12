# Zadanie 19: List Comprehension

# Utwórz listę liczb od 0 do 10. Następnie stwórz nową listę zawierającą kwadraty tych liczb, 
# używając list comprehension. Wydrukuj nową listę.

# definiuję listę
NumbersList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# definiuje listę z wartościami do kwadratu
SquareNumberList = [pow(x,2) for x in NumbersList]
print(SquareNumberList)
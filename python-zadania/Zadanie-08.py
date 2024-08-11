# Zadanie 08: Sety
# Utwórz set z wartościami: 1, 2, 3, 4, 5. Dodaj wartość 6 do setu. Spróbuj dodać wartość 3 jeszcze raz.
#  Co się stanie?

SetOfNumbers = {1, 2, 3, 4, 5}
print(SetOfNumbers)

SetOfNumbers.add(6)
print(SetOfNumbers)

SetOfNumbers.add(3)
print(SetOfNumbers)

#Przy próbie dodania do set'u elementu, który już w nim istnieje, nowo dodany element jest ignorowany.
# Zadanie 12: Sprawdzanie kluczy w słowniku

# Sprawdź, czy w słowniku z zadania 06 istnieje klucz "city". 
# Jeśli tak, wydrukuj odpowiednią wiadomość.

slownikObywatel = {
    "name": "Barbara",
    "age": 27,
    "city": "Poznań"
}

if "city" in slownikObywatel:
    print ("Yes, 'city' is one of the keys in the 'slownikObywatel' dictionary")

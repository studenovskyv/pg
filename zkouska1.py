# Příklad 1: Práce s podmínkami a cykly
# Zadání:
# Napište funkci `process_numbers`, která přijme seznam celých čísel. 
# Funkce vrátí nový seznam, který obsahuje pouze čísla větší než 5, vynásobená 2.
# Pokud seznam obsahuje číslo 10, ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_numbers(numbers):
    # ZDE NAPIŠTE VÁŠ KÓD




    vysledek = []  # Vytvoříme prázdný seznam, kam budeme ukládat výsledky.

    for cislo in numbers:  # Pro každé číslo `num` v seznamu `numbers`:
        if cislo == 10:  # Pokud je číslo rovno 10:
            break  # Ukončíme zpracování seznamu.
        if cislo > 5:  # Pokud je číslo větší než 5:
            vysledek.append(cislo * 2)  # Přidáme číslo vynásobené 2 do výsledného seznamu.


    return vysledek  # Vrátíme výsledný seznam





# Pytest testy pro Příklad 1
def test_process_numbers():
    assert process_numbers([1, 6, 3, 10, 8]) == [12]
    assert process_numbers([7, 8, 10, 12]) == [14, 16]
    assert process_numbers([1, 2, 3, 4]) == []
    assert process_numbers([5, 6, 7, 15]) == [12, 14, 30]
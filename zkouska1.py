# Příklad 1: Práce s podmínkami a řetězci
# Zadání:
# Napište funkci `process_strings`, která přijme seznam řetězců. 
# Funkce vrátí nový seznam, který obsahuje pouze řetězce delší než 3 znaky, převedené na velká písmena.
# Pokud seznam obsahuje řetězec "STOP", ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_strings(strings):
    # ZDE NAPIŠTE VÁŠ KÓD



    result = []  # Vytvoříme prázdný seznam pro ukládání výsledků.
    
    for string in strings:  # Procházíme každý řetězec v seznamu.
        if string == "STOP":  # Pokud narazíme na řetězec "STOP":
            break  # Ukončíme smyčku.
        if len(string) > 3:  # Pokud délka řetězce je větší než 3 znaky:
            result.append(string.upper())  # Převedeme na velká písmena a přidáme do výsledku.
    
    return result  # Vrátíme výsledný seznam.
    




# Pytest testy pro Příklad 1
def test_process_strings():
    assert process_strings(["abc", "abcd", "STOP", "efgh"]) == ["ABCD"]
    assert process_strings(["hello", "world", "STOP", "python"]) == ["HELLO", "WORLD"]
    assert process_strings(["hi", "ok", "go"]) == []
    assert process_strings(["code", "test", "debug"]) == ["CODE", "TEST", "DEBUG"]

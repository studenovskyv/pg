def bin_to_dec(binarni_cislo):
    # Převod čísla na string
    binarni_cislo = str(binarni_cislo)
    
    # Ověření, že číslo obsahuje pouze 0 a 1
    if not all(char in "01" for char in binarni_cislo):
        raise ValueError("Vstup není platné binární číslo! Zadávejte pouze 0 a 1.")
    
    # Převod binárního čísla na decimální
    return int(binarni_cislo, 2)

# Testovací funkce
def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    print("Všechny testy prošly!")

# Spuštění testů
test_funkce()

# Ukázka použití
print(bin_to_dec("110101"))  # Výstup: 53
print(bin_to_dec(1110001))   # Výstup: 113
# bin_to_dec("102")  # Tohle vyvolá ValueError

# Definice funkce sudy_nebo_lichy
def sudy_nebo_lichy(cislo):
    # Kontrola, zda je číslo sudé nebo liché
    if cislo % 2 == 0:
        print(f"Číslo {cislo} je sudé")
    else:
        print(f"Číslo {cislo} je liché")

# Získání čísla od uživatele
try:
    cislo = int(input("Zadejte číslo: "))  # Převod vstupu na celé číslo
    sudy_nebo_lichy(cislo)
except ValueError:
    print("Zadejte prosím platné celé číslo.")  # Ošetření neplatného vstupu

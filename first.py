
def sudy_nebo_lichy(cislo):

    if cislo % 2 == 0:
        print(f"Číslo {cislo} je sudé")
    else:
        print(f"Číslo {cislo} je liché")

try:
    cislo = int(input("Zadejte číslo: "))  
    sudy_nebo_lichy(cislo)
except ValueError:
    print("Zadejte prosím platné celé číslo.")  

def je_prvocislo(cislo):
    
    if cislo < 2:
        return False
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    
    maximum = int(maximum)  # Zajistí, že maximum je celé číslo
    prvocisla = [cislo for cislo in range(2, maximum + 1) if je_prvocislo(cislo)]
    return prvocisla

if __name__ == "__main__":
    maximum = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(maximum)
    print(prvocisla)
def je_prvocislo(cislo):
    
    if cislo < 2:
        return False
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    
    maximum = int(maximum)  # Zajistí, že maximum je celé číslo
    prvocisla = [cislo for cislo in range(2, maximum + 1) if je_prvocislo(cislo)]
    return prvocisla

if __name__ == "__main__":
    maximum = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(maximum)
    print(prvocisla)

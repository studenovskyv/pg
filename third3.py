def je_prvocislo(cislo):
    """
    Funkce ověří, zda zadané číslo je nebo není prvočíslo a vrátí True nebo False.

    Prvočíslo je takové číslo větší než 1, které není dělitelné žádným jiným číslem kromě 1 a sebe sama.
    """
    if cislo < 2:
        return False
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    """
    Funkce spočítá všechna prvočísla v rozsahu 1 až maximum a vrátí je jako seznam.
    """
    maximum = int(maximum)  # Zajistí, že maximum je celé číslo
    prvocisla = [cislo for cislo in range(2, maximum + 1) if je_prvocislo(cislo)]
    return prvocisla

if __name__ == "__main__":
    maximum = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(maximum)
    print(prvocisla)
def je_prvocislo(cislo):
    """
    Funkce ověří, zda zadané číslo je nebo není prvočíslo a vrátí True nebo False.

    Prvočíslo je takové číslo větší než 1, které není dělitelné žádným jiným číslem kromě 1 a sebe sama.
    """
    if cislo < 2:
        return False
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    """
    Funkce spočítá všechna prvočísla v rozsahu 1 až maximum a vrátí je jako seznam.
    """
    maximum = int(maximum)  # Zajistí, že maximum je celé číslo
    prvocisla = [cislo for cislo in range(2, maximum + 1) if je_prvocislo(cislo)]
    return prvocisla

if __name__ == "__main__":
    maximum = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(maximum)
    print(prvocisla)

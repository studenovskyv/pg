def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    
    # Ověření, že pozice je na šachovnici
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False
    
    # Ověření, že cílová pozice není obsazena
    if cilova_pozice in obsazene_pozice:
        return False
    
    typ = figurka["typ"]
    startovni_pozice = figurka["pozice"]
    
    # Pěšec
    if typ == "pěšec":
        smer = 1  # Bílé figurky se pohybují nahoru (z nižších řádků na vyšší)
        if startovni_pozice[1] == cilova_pozice[1]:  # Pohyb rovně
            if cilova_pozice[0] == startovni_pozice[0] + smer and (cilova_pozice not in obsazene_pozice):
                return True
            if startovni_pozice[0] == 2 and cilova_pozice[0] == startovni_pozice[0] + 2 * smer:
                if (startovni_pozice[0] + 1, startovni_pozice[1]) not in obsazene_pozice:
                    return True
        return False
    
    # Jezdec
    elif typ == "jezdec":
        dx = abs(cilova_pozice[0] - startovni_pozice[0])
        dy = abs(cilova_pozice[1] - startovni_pozice[1])
        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
            return True
        return False
    
    # Věž
    elif typ == "věž":
        if startovni_pozice[0] == cilova_pozice[0] or startovni_pozice[1] == cilova_pozice[1]:  # Horizontální nebo vertikální tah
            if je_cesta_volna(startovni_pozice, cilova_pozice, obsazene_pozice):
                return True
        return False
    
    # Střelec
    elif typ == "střelec":
        if abs(cilova_pozice[0] - startovni_pozice[0]) == abs(cilova_pozice[1] - startovni_pozice[1]):  # Diagonální tah
            if je_cesta_volna(startovni_pozice, cilova_pozice, obsazene_pozice):
                return True
        return False
    
    # Dáma
    elif typ == "dáma":
        if (startovni_pozice[0] == cilova_pozice[0] or startovni_pozice[1] == cilova_pozice[1] or
            abs(cilova_pozice[0] - startovni_pozice[0]) == abs(cilova_pozice[1] - startovni_pozice[1])):  # Kombinace věže a střelce
            if je_cesta_volna(startovni_pozice, cilova_pozice, obsazene_pozice):
                return True
        return False
    
    # Král
    elif typ == "král":
        dx = abs(cilova_pozice[0] - startovni_pozice[0])
        dy = abs(cilova_pozice[1] - startovni_pozice[1])
        if dx <= 1 and dy <= 1:  # Může se hýbat o jedno pole ve všech směrech
            return True
        return False
    
    return False

def je_cesta_volna(start, cil, obsazene_pozice):
    """Pomocná funkce pro ověření, zda mezi startem a cílem není žádná figura."""
    # Horizontální pohyb
    if start[0] == cil[0]:
        radek = start[0]
        for sloupec v range(min(start[1], cil[1]) + 1, max(start[1], cil[1])):
            if (radek, sloupec) in obsazene_pozice:
                return False
    # Vertikální pohyb
    elif start[1] == cil[1]:
        sloupec = start[1]
        for radek in range(min(start[0], cil[0]) + 1, max(start[0], cil[0])):
            if (radek, sloupec) in obsazene_pozice:
                return False
    # Diagonální pohyb
    else:
        radek_smer = 1 if cil[0] > start[0] else -1
        sloupec_smer = 1 if cil[1] > start[1] else -1
        radek, sloupec = start[0] + radek_smer, start[1] + sloupec_smer
        while radek != cil[0] and sloupec != cil[1]:
            if (radek, sloupec) in obsazene_pozice:
                return False
            radek += radek_smer
            sloupec += sloupec_smer
    return True

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True

# second.py
def cislo_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    teens = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    
    cislo = int(cislo)  # Převod vstupu na číslo

    if cislo < 10:
        return jednotky[cislo]
    elif 10 <= cislo < 20:
        return teens[cislo - 10]
    elif 20 <= cislo < 100:
        desitka = cislo // 10
        jednotka = cislo % 10
        if jednotka == 0:
            return desitky[desitka]
        else:
            return f"{desitky[desitka]} {jednotky[jednotka]}"
    elif cislo == 100:
        return "sto"
    else:
        return "Číslo není v rozsahu 0 až 100"

# Testování funkce
if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)

# Příklad 2: Práce s externími daty a výpočty
# Zadání:
# Napište funkci `convert_to_czk`, která:
# 1. Přijme částku (`amount`) jako desetinné číslo a kód měny (`currency`) jako řetězec (např. "USD", "EUR").
# 2. Stáhne aktuální kurzovní lístek z URL:
#    http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
# 3. Načte příslušný kurz podle zadaného kódu měny a provede převod zadané částky na české koruny (CZK).
# 4. Funkce vrátí výslednou částku v CZK zaokrouhlenou na dvě desetinná místa.
# Pokud zadaná měna v kurzovním lístku neexistuje, vyhoďte výjimku `ValueError`.




import requests

def convert_to_czk(amount, currency):
    """
    Převádí zadanou částku z dané měny na české koruny podle kurzovního lístku ČNB.
    
    :param amount: Částka v cizí měně (desetinné číslo)
    :param currency: Kód měny (např. "USD", "EUR")
    :return: Převod na CZK (zaokrouhlený na dvě desetinná místa)
    :raises ValueError: Pokud měna neexistuje v kurzovním lístku
    """
    # URL kurzovního lístku ČNB
    url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"

    # Stažení dat z URL
    response = requests.get(url)
    if not response.ok:
        raise Exception("Chyba při stahování kurzovního lístku.")
    
    # Zpracování dat
    data = response.text.split("\n")  # Rozdělení obsahu na řádky
    exchange_rates = {}

    for line in data[2:]:  # Přeskakujeme první dva řádky
        if not line.strip():  # Pokud je řádek prázdný, přeskoč
            continue
        
        # Rozdělení řádku podle '|' a extrakce informací
        parts = line.split("|")
        if len(parts) < 5:  # Kontrola, zda má řádek správnou strukturu
            continue
        
        # Extrahování informací
        code = parts[3]  # Kód měny (např. "USD")
        amount_per_unit = float(parts[2])  # Množství (např. 1, 100)
        exchange_rate = float(parts[4].replace(",", "."))  # Kurz (převod z CZK)

        # Uložení do slovníku s klíčem `code`
        exchange_rates[code] = exchange_rate / amount_per_unit

    # Kontrola, zda měna existuje
    if currency not in exchange_rates:
        raise ValueError(f"Currency {currency} not found in the exchange rate list.")

    # Převod částky na CZK
    result = amount * exchange_rates[currency]
    return round(result, 2)






# Pytest testy pro Příklad 2
from unittest.mock import patch, MagicMock

def test_convert_to_czk():
    mock_response = """31.10.2025 #237
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|14,894
EMU|euro|1|EUR|25,480
USA|dolar|1|USD|23,000
Velká Británie|libra|1|GBP|29,745
"""
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, text=mock_response)

        assert convert_to_czk(100, "USD") == 2300.00
        assert convert_to_czk(50, "EUR") == 1274.00
        assert convert_to_czk(200, "AUD") == 2978.80
        
        try:
            convert_to_czk(100, "XYZ")
        except ValueError as e:
            assert str(e) == "Currency XYZ not found in the exchange rate list."

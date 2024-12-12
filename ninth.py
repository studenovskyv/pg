def dec_to_bin(cislo):
    # Funkce převede číslo na binární reprezentaci (cislo může být str i int).
    # Vrací výstup jako str.
    if isinstance(cislo, str):
        cislo = int(cislo)
    return bin(cislo)[2:]

def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"

test_bin_to_dec()

import sys
import requests
import re

def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne obsah zadané stránky a vrátí celé <a> tagy obsahující href.
    """
    try:
        # Stáhnutí obsahu stránky
        response = requests.get(url)
        # Kontrola, zda byl požadavek úspěšný
        if response.status_code == 200:
            # Dekódování obsahu stránky do textu
            content = response.text
            # Vyhledání všech <a> tagů obsahujících href pomocí regulárního výrazu
            a_tags = re.findall(r'<a\s+[^>]*href="[^"]*"[^>]*>.*?</a>', content, re.IGNORECASE)
            return a_tags
        else:
            raise ValueError(f"Server vrátil chybu s kódem {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Chyba při stahování URL: {e}")

if __name__ == "__main__":
    try:
        # Načtení URL z příkazového řádku
        url = sys.argv[1]
        a_tags = download_url_and_get_all_hrefs(url)
        # Výpis nalezených <a> tagů
        print("Nalezené odkazy:")
        for tag in a_tags:
            print(tag)
    except Exception as e:
        # Ošetření případné chyby
        print(f"Program skončil chybou: {e}")

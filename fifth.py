import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    """
    Načte prvních header_length bytů ze souboru a vrátí je.
    """
    try:
        with open(file_name, 'rb') as file:
            return file.read(header_length)
    except FileNotFoundError:
        print(f"Soubor {file_name} nebyl nalezen.")
        return None
    except IOError:
        print(f"Nastala chyba při čtení souboru {file_name}.")
        return None


def is_jpeg(file_name):
    """
    Zkontroluje, zda soubor má JPEG hlavičku.
    """
    header = read_header(file_name, len(jpeg_header))
    if header is None:
        return False
    return header.startswith(jpeg_header)


def is_gif(file_name):
    """
    Zkontroluje, zda soubor má GIF hlavičku.
    """
    header = read_header(file_name, len(gif_header1))
    if header is None:
        return False
    return header.startswith(gif_header1) or header.startswith(gif_header2)


def is_png(file_name):
    """
    Zkontroluje, zda soubor má PNG hlavičku.
    """
    header = read_header(file_name, len(png_header))
    if header is None:
        return False
    return header.startswith(png_header)


def print_file_type(file_name):
    """
    Vypíše typ souboru podle jeho hlavičky.
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    try:
        # Načte název souboru z příkazové řádky
        file_name = sys.argv[1]
        print_file_type(file_name)
    except IndexError:
        print("Nebyl zadán název souboru. Použití: python fifth.py <název_souboru>")
    except Exception as e:
        print(f"Nastala neočekávaná chyba: {e}")


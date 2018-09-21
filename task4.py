import re
from collections import defaultdict

from task3 import calc_symbol_frequency


def read_text(file_name: str) -> str:
    with open(file_name) as file:
        return file.read()


def guess_symbol(frequency_map: defaultdict, frequency: float) -> str:
    s = ''
    diff = 100.0
    for symbol, freq in frequency_map.items():
        if abs(frequency - freq) < diff:
            diff = abs(frequency - freq)
            s = symbol

    return s


def decipher(plain_text_filename: str, cipher_text_filename: str):
    plain_text = read_text(plain_text_filename)
    plain_text = re.findall('\w', plain_text.lower())
    plain_text = ''.join(plain_text)

    symbol_frequency = calc_symbol_frequency(plain_text)

    cipher_text = read_text(cipher_text_filename)
    cipher_text = re.findall('\w', cipher_text.lower())
    cipher_text = ''.join(cipher_text)
    cipher_symbol_frequency = calc_symbol_frequency(cipher_text)
    frequency_map = {v: k for k, v in cipher_symbol_frequency.items()}

    decipher_text = ''
    for symbol in cipher_text:
        if symbol_frequency.get(symbol):
            freq = symbol_frequency[symbol]
            s = guess_symbol(symbol_frequency, cipher_symbol_frequency[symbol])
            decipher_text += s
        else:
            decipher_text += symbol





    


if __name__ == "__main__":
    plain_text_filename = 'tolstoi.txt'
    cipher_text_filename = "tolstoi.enc"

    decipher_text = decipher(plain_text_filename, cipher_text_filename)
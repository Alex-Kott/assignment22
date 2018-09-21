
import re
from collections import defaultdict


def calc_symbol_frequency(text: str) -> defaultdict:
    symbol_counter = defaultdict(int)
    for s in text:
        symbol_counter[s] += 1

    symbol_frequency = defaultdict(float)
    for k, v in symbol_counter.items():
        symbol_frequency[k] = v / (len(text) / 100)

    return symbol_frequency


def main(file_name: str):
    with open(file_name) as file:
        text = file.read()

    text = re.findall('\w', text.lower())
    text = ''.join(text)

    symbol_frequency = calc_symbol_frequency(text)

    for k, v in symbol_frequency.items():
        print(f'{k}: {v}%')


if __name__ == "__main__":
    file_name = "tolstoi.txt"
    main(file_name)
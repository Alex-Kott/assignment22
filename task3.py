
import re
from collections import defaultdict


def main(file_name: str):
    with open(file_name) as file:
        text = file.read()

    text = text.lower()
    text = re.findall('\w', text)
    text = ''.join(text)

    symbol_counter = defaultdict(int)
    for s in text:
        symbol_counter[s] += 1

    print('symbols: ', len(text))

    for k, v in symbol_counter.items():
        print(k,v)

    symbol_frequency = defaultdict(float)
    for k, v in symbol_counter.items():
        symbol_frequency[k] = v / (len(text) / 100)

    for k, v in symbol_frequency.items():
        print(k, v)



if __name__ == "__main__":
    file_name = "tolstoi.txt"
    main(file_name)
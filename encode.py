from get_e import get_e
from GlobalVariables import *


def encode(text):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = get_e(p, phi)
    result = []
    for char in text:
        t = alphabet_dict[char] + 1
        c = (t ** e) % n
        result.append(str(c))
    return ' '.join(result)
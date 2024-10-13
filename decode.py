from GlobalVariables import  *
from get_e import get_e
from get_d import get_d


def decode(text):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = get_e(p, phi)
    d = get_d(e, phi)
    encoded = text.split()
    result = []
    for c in encoded:
        t = (int(c) ** d) % n
        result.append(alphabet_list[t - 1])
    return ''.join(result)
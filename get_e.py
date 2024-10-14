import math


def get_e(p, phi):
    for e in reversed(range(p)):
        for i in range(2, (e // 2) + 1):
            if (e % i) == 0:
                break
        else:
            if math.gcd(e, phi) == 1:
                return int(e)
    else:
        raise ValueError("No valid value was found for e.")
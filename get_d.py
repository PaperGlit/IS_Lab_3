def get_d(e, phi):
    k = 1
    while True:
        d = ((k * phi) + 1) / e
        if d.is_integer():
            return int(d)
        k += 1
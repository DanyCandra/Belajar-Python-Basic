def suaraAyam():
    print('Kukuruyuk')

def hargaAyam():
    print('1 Kilo Ayam Adalah Rp. 20.000')

def beliAyam(kg):
    suaraAyam()
    hargaAyam()
    total=kg*20000
    print('Beli Ayam ',kg,' kg adalah Rp.',total)

beliAyam(2)
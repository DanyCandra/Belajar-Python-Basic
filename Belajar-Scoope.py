namaKucing='Gomes'
makananKucing='Wiskas'

def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing=namaBaru
    #print('Saya rubah nama kucing menjadi',namaKucing)

def kasihMakanKucing(makanan,nama):
    global  namaKucing,makananKucing
    namaKucing=nama
    makananKucing=makanan


rubahNamaKucing('Ketie')
kasihMakanKucing(makanan='Universal',nama='Alex')
print('nama kucing saya adalah',namaKucing,'dan makan',makananKucing)
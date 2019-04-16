from builtins import object

#BELAJAR class
#BELAJAR Private Variable
#Belajar __init__ method
#Belajar class variable

class mahasiswa():
    nama='nama'
    nim='nim'
    __nilai=0
    jurusan ='Ekonomi'
    jumlah_mahasiswa=0

    def __init__(self,input_nama,input_nim):
        self.nama=input_nama
        self.nim=input_nim
        mahasiswa.jumlah_mahasiswa += 1

    def belajar(self,kondisi):
        print(self.nama,'sedang belajar',kondisi)

    def tidur(self,kondisi):
        print(self.nama,'sedang tidur',kondisi)

    def uts(self,input_nilai):
        self.__nilai+=input_nilai

    def uas(self,input_nilai):
        self.__nilai+=input_nilai

    def chek_status(self):
        if self.__nilai >= 50:
            print(self.nama,'lulus')
        else:
            print(self.nama, 'tidak lulus')


otong=mahasiswa('otong','13317001')
otong.jurusan='Ekonomi Syariah'
otong.kegemaran='Menari'

print(mahasiswa.jurusan)
print(otong.jurusan)
print(otong.kegemaran)

print(otong.jumlah_mahasiswa)


otong.uas(10)
otong.uts(90)
otong.chek_status()

print(otong.__dict__)




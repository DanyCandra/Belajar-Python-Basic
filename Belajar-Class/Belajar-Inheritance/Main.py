class Ojek():

    def __init__(self,nama,transmisi,daerah):
        self.nama=nama
        self.transmisi=transmisi
        self.daerah=daerah

    def check_id_abang(self):
        print('nama:',self.nama,'\nmotor:',self.transmisi,'\ndaerah:',self.daerah)

class Gojek(Ojek):

    #Override
    def check_id_abang(self):
        print('Cek Aplikasi')



ojek1=Ojek('dany','manual','gejayan')
ojek2=Gojek('candra','matic','terban')

ojek1.check_id_abang()
ojek2.check_id_abang()

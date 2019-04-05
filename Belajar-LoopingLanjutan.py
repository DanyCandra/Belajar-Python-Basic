nama_band=['Payung Teduh',
           'Dialog Dini Hari',
           'Mr.SOnjaya',
           'Parahyena']

daftar_agu=['Akad',
      'Rumahku',
      'Sang Filsuf',
      'Sindoro']

#i=0
#for band in nama_band:
    #print('no',i,'|',band)
    #i+=1
#enumarate
for i,band in enumerate(nama_band):
    print('no',i,'|',band)

#zip untuk menggabungkan list

for band,lagu in zip(nama_band,daftar_agu):
    print(band,'menyanyikan lagu',lagu)

print(100*'=')

#set
playlist={'baby',
          'ada apa dengan cinta',
          'cenat cenut',
          'jaran goyang'}

for lagu in sorted(playlist):
    print(lagu)

#dictionary
playlist1={"payung teduh" : "akad",
          "4 21":"zona nyaman",
          "Dialog":"Rumahku"
           }

for i in playlist1.values():
    print(i)
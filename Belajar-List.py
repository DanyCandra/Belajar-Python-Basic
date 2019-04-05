data=[1,4,9,16,25,36,49,64]

#akses list
subdata1=data[-3]
subdata2=data[2:4]
subdata3=data[:4]

data2=[100,200,300,400,500,600,700,800]
#tmbah data
data3=data+data2
#merubah isi list
data2[2]=350
#mengkopi data
a=data[:]
a[4]=90
#merubah kontek dengan slicing
data[3:5]=[11,12]

#print(a)
#print(data)

#list dalam list
x=[data,data2]
#print(x)

#akses list multidimensi
y=x[0][2]
#print(y)

#menambah member
data.append(3)
print(data)

#mengetahui panjang
panjang=len(data)

print(panjang)


#input output

#membuat file text

"""
w = write mode/ mode menulis dan menghapus file lama
r = read only / hanya bisa baca
a = appending /menambah data di akhir baris
r+ = write and read mode
"""

#membuat file
file=open("data.txt","w")

file.write("Data text yang digunakan oleh python")
file.write("\nini baris ke dua")
file.write("\nini baris ke tiga")
file.write("\nini baris ke empat")
file.close() #setiap buat harus di close

#membaca file text
file2=open("data.txt",'r')
#print(file2.read())

print(file2.readline())

#menmbah baris
file3=open("data.txt","a")
file3.write("\nMenambah Baris dari Append")
file3.close()
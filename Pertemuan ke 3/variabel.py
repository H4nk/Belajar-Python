nama = "Harry Setya Hadi"
print(nama)      # print string lengkap
print(nama[0])   # print karakter pertama
print(nama[-1])  # print karakter terakhir
print(nama[2:4]) # print dari indeks 4 - 6
print(nama[:6])  # print dari indeks 0 - 3

x = 10
print(x, "tipenya adalah ", type(x))
x = 5.5
print(x, "tipenya adalah ", type(x))
x = 1+27j
print(x, "tipenya adalah ",type(x))


#LIST

a = [0,1,2,3,4,5,6,7,8,9]
print("a[2] = ", a[2])
print("a[0:3] = ", a[0:3])
print("a[5:] = ", a[5:]) 

#tuple

buah = ("Durian", "Pisang", "Jeruk","Anggur")
print(buah)      # print list lengkap
print(buah[0])   # print list pertama
print(buah[-1])  # print list terakhir
print(buah[1:3]) # print dari list  1 - 2
print(buah[:3])  # print dari indeks 0 - 2


#Set

# set integer 
my_set = {1,2,3} 
print(my_set) 

# set dengan menggunakan fungsi set() 
my_set = set([1,2,3]) 
print(my_set) 

# set data campuran 
my_set = {1, 2.0, "Python", (3,4,5)} 
print(my_set) 

# bila kita mengisi duplikasi, set akan menghilangkan salah satu 
# output: {1,2,3} 
my_set = {1,2,2,3,3,3} 
print(my_set) 

# set tidak bisa berisi anggota list 
# contoh berikut akan muncul error TypeError 
#my_set = {1,2,[3,4,5]} 

#dictoranry

mobil = {"merek": "Mitsubishi","jenis": "SL","tahun": 1982}

x = mobil.keys() #dict_keys
print(x)
print(mobil["merek"]) #tampilkan data merek
print(mobil["jenis"]) #tampilkan data jenis
print(mobil["tahun"]) #tampilkan data tahun

#print(x[Merek])
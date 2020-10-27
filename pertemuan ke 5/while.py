# while biasa
a = 1
while a < 6:
    print(a)
    a +=1
# while + break
a = 1
while a < 10:
    print(a)
    if(a==6):
        break
    a +=1

# while + continue
a = 0
while a < 10:
    a +=1
    if a == 6:
        continue
    print(a)
#while + else 
a = 1
while a < 10:
    print(a)
    a +=1
else:
    print("Nilai variabel A besar sama dari 10")
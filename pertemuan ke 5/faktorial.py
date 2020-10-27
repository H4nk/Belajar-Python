def TowerOfHanoi(n , awal, tujuan, bantu):
        if n==1:
                print ("Pindahkan Disk 1 Dari Tower",awal,"Ke Tower",tujuan)
                return
        TowerOfHanoi(n-1, awal, bantu, tujuan)
        print ("Pindahkan Disk",n,"Dari Tower",awal,"Ke Tower",tujuan)
        TowerOfHanoi(n-1, bantu, tujuan, awal)
n = 3
TowerOfHanoi(n,'A','B','C')
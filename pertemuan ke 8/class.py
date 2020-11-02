class Mahasiswa:
    def __init__(self, nama, bp):
        self.nama = nama
        self.bp = str(bp)
    def mhs(self):
        print("Perkenalkan nama Saya " + self.nama)
        print("Nomor BP saya adalah " + self.bp)

cek = Mahasiswa("Harry Setya Hadi", 1234)
cek.mhs()
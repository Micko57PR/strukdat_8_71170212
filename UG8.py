class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    def __init__(self):
        self._antre = [None]
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError('Gaada Antrean')
        else:
            antre = self._antre[0]
            for i in range(self._size - 1):
                self._antre[i] = self._antre[i + 1]
            self._antre[self._size - 1] = None
            self._size -= 1
            return antre.getNamaPelanggan()
        
    def enqueue(self, namaPelanggan):
        if self._size == len(self._antre):
            self.resize(2 * len(self._antre))
        node = NodePelanggan(namaPelanggan)
        self._antre[self._size] = node
        self._size += 1
        
    def resize(self, cap):
        old_antre = self._antre
        self._antre = [None] * cap
        for i in range(self._size):
            self._antre[i] = old_antre[i]
        for i in range(self._size, cap):
            self._antre[i] = "kosong"
        
    def printAll(self):
        print('=== Kasir ===')
        if self.is_empty():
            print('Kosong')
        else:
            for i in range(self._size):
                print(f"{i+1}. {self._antre[i].getNamaPelanggan()}")
        print()
        
# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniff")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

print("### Melakukan Resize ###")
tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

print("### Pelanggan", tempatKasir.dequeue() ,"Selesai Membayar ###")
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

print("### Pelanggan", tempatKasir.dequeue(), " Selesai Membayar ###")
tempatKasir.printAll()



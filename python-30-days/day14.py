# ============================================
# DAY 15 - MAGIC METHODS
# ============================================

# Magic (Dunder) methods nedir?
# Basinda ve sonunda __ olan ozel metodlardir.
# Python objeleri nasil davranacak onu belirler.


# ============================================
# 1️⃣ __str__ ve __repr__
# ============================================

class Kitap:

    def __init__(self, isim, yazar, sayfa):
        self.isim = isim
        self.yazar = yazar
        self.sayfa = sayfa

    def __str__(self):
        return f"{self.isim} - {self.yazar}"

    def __repr__(self):
        return f"Kitap('{self.isim}', '{self.yazar}', {self.sayfa})"


k1 = Kitap("Python 101", "Ercan", 300)

print(k1)        # __str__ calisir
print(repr(k1))  # __repr__ calisir


# ============================================
# 2️⃣ __len__
# ============================================

class Sepet:

    def __init__(self):
        self.urunler = []

    def urun_ekle(self, urun):
        self.urunler.append(urun)

    def __len__(self):
        return len(self.urunler)


sepet = Sepet()
sepet.urun_ekle("Laptop")
sepet.urun_ekle("Mouse")

print("Sepetteki urun sayisi:", len(sepet))


# ============================================
# 3️⃣ Operator Overloading (__add__)
# ============================================

class Vektor:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vektor(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"


v1 = Vektor(2, 3)
v2 = Vektor(4, 5)

v3 = v1 + v2

print(v3)


# ============================================
# 4️⃣ Mini Uygulama
# ============================================

class Ogrenci:

    def __init__(self, isim, notlar):
        self.isim = isim
        self.notlar = notlar

    def __len__(self):
        return len(self.notlar)

    def ortalama(self):
        return sum(self.notlar) / len(self.notlar)

    def __str__(self):
        return f"{self.isim} - Ortalama: {self.ortalama():.2f}"


ogr = Ogrenci("Ercan", [80, 90, 100])
print(ogr)
print("Not sayisi:", len(ogr))
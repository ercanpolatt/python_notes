# ============================================
# DAY 14 - INHERITANCE & POLYMORPHISM
# ============================================

# Inheritance nedir?
# Bir sinifin baska bir siniftan ozellik ve davranis miras almasi.

# ============================================
# 1️⃣ Parent Class
# ============================================

class Hayvan:

    def __init__(self, isim):
        self.isim = isim

    def ses_cikar(self):
        print("Hayvan ses cikardi")


# ============================================
# 2️⃣ Child Class
# ============================================

class Kopek(Hayvan):

    def ses_cikar(self):
        print(f"{self.isim} havladi 🐶")


class Kedi(Hayvan):

    def ses_cikar(self):
        print(f"{self.isim} miyavladi 🐱")


# ============================================
# 3️⃣ Nesne Olusturma
# ============================================

kopek1 = Kopek("Karabas")
kedi1 = Kedi("Minnos")

kopek1.ses_cikar()
kedi1.ses_cikar()


# ============================================
# 4️⃣ super() Kullanimi
# ============================================

class Calisan:

    def __init__(self, isim, maas):
        self.isim = isim
        self.maas = maas

    def bilgi(self):
        print(f"Isim: {self.isim}, Maas: {self.maas}")


class Yazilimci(Calisan):

    def __init__(self, isim, maas, dil):
        super().__init__(isim, maas)  # Parent constructor
        self.dil = dil

    def bilgi(self):
        super().bilgi()
        print(f"Kullandigi Dil: {self.dil}")


y1 = Yazilimci("Ercan", 50000, "Python")
y1.bilgi()


# ============================================
# 5️⃣ Polymorphism
# ============================================

hayvanlar = [Kopek("Rex"), Kedi("Pamuk")]

for hayvan in hayvanlar:
    hayvan.ses_cikar()  # Aynı method, farkli davranis
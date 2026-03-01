# ============================================
# DAY 12 - OBJECT ORIENTED PROGRAMMING
# ============================================

# Class nedir?
# Gercek hayattaki bir varligin kod icindeki sablonudur.

# ============================================
# 1️⃣ Basit Class Tanimi
# ============================================

class Araba:

    # Constructor method (kurucu metod)
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    # Method (sinif icindeki fonksiyon)
    def bilgileri_goster(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Yil: {self.yil}")

    def calistir(self):
        print(f"{self.marka} calisti 🚗")


# ============================================
# 2️⃣ Nesne Olusturma (Object)
# ============================================

araba1 = Araba("Toyota", "Corolla", 2022)
araba2 = Araba("BMW", "M3", 2023)

araba1.bilgileri_goster()
araba1.calistir()

print("------")

araba2.bilgileri_goster()


# ============================================
# 3️⃣ Ozellik Degistirme
# ============================================

araba1.yil = 2024
print("Guncel yil:", araba1.yil)


# ============================================
# 4️⃣ Ornek - Banka Hesabi
# ============================================

class BankaHesabi:

    def __init__(self, isim, bakiye=0):
        self.isim = isim
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"{miktar} TL yatirildi.")

    def para_cek(self, miktar):
        if miktar > self.bakiye:
            print("Yetersiz bakiye!")
        else:
            self.bakiye -= miktar
            print(f"{miktar} TL cekildi.")

    def bakiye_goster(self):
        print(f"Guncel bakiye: {self.bakiye} TL")


# ============================================
# 5️⃣ Nesne Kullanimi
# ============================================

hesap1 = BankaHesabi("Ercan", 1000)

hesap1.bakiye_goster()
hesap1.para_yatir(500)
hesap1.para_cek(300)
hesap1.bakiye_goster()
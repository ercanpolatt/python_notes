# ============================================
# DAY 13 - ENCAPSULATION
# ============================================

# Encapsulation nedir?
# Bir sinif icindeki veriyi disaridan dogrudan degistirmeyi engellemek.
# Veriyi kontrollu sekilde yonetmek.

# ============================================
# 1️⃣ Private Degisken
# ============================================

class Kisi:

    def __init__(self, isim, yas):
        self.isim = isim
        self.__yas = yas   # __ ile private yapilir

    def bilgileri_goster(self):
        print(f"Isim: {self.isim}")
        print(f"Yas: {self.__yas}")


kisi1 = Kisi("Ercan", 25)
kisi1.bilgileri_goster()

# print(kisi1.__yas)  # ❌ HATA (disaridan erisemezsin)


# ============================================
# 2️⃣ Getter ve Setter
# ============================================

class BankaHesabi:

    def __init__(self, isim, bakiye):
        self.isim = isim
        self.__bakiye = bakiye

    # Getter
    def bakiye_goster(self):
        return self.__bakiye

    # Setter
    def para_yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
        else:
            print("Gecersiz miktar")

    def para_cek(self, miktar):
        if 0 < miktar <= self.__bakiye:
            self.__bakiye -= miktar
        else:
            print("Yetersiz bakiye veya hatali miktar")


hesap = BankaHesabi("Ercan", 1000)

print("Bakiye:", hesap.bakiye_goster())
hesap.para_yatir(500)
hesap.para_cek(200)
print("Guncel bakiye:", hesap.bakiye_goster())


# ============================================
# 3️⃣ property Kullanimi (Pythonic Yontem)
# ============================================

class Urun:

    def __init__(self, isim, fiyat):
        self.isim = isim
        self.__fiyat = fiyat

    @property
    def fiyat(self):
        return self.__fiyat

    @fiyat.setter
    def fiyat(self, yeni_fiyat):
        if yeni_fiyat > 0:
            self.__fiyat = yeni_fiyat
        else:
            print("Fiyat negatif olamaz")


urun = Urun("Laptop", 20000)

print("Fiyat:", urun.fiyat)

urun.fiyat = 25000
print("Yeni fiyat:", urun.fiyat)

# urun.fiyat = -100  # Kontrol devrede
# ============================================
# DAY 6 - LISTELER (LISTS)
# ============================================

# Liste nedir?
# Birden fazla veriyi tek bir degisken icinde tutmamizi saglar.
# [] koseli parantez ile olusturulur.

sayilar = [1, 2, 3, 4, 5]
isimler = ["Ali", "Ercan", "Ayse"]
karisik = [1, "Python", True, 3.14]

print(sayilar)
print(isimler)
print(karisik)

# ============================================
# Index mantigi
# ============================================

# Python index 0'dan baslar
print(isimler[0])  # Ali
print(isimler[1])  # Ercan

# Son elemana erismek
print(isimler[-1])

# ============================================
# Liste eleman degistirme
# ============================================

sayilar[0] = 100
print(sayilar)

# ============================================
# Listeye eleman ekleme
# ============================================

sayilar.append(6)     # sona ekler
print(sayilar)

sayilar.insert(1, 50) # belirtilen indexe ekler
print(sayilar)

# ============================================
# Listeden eleman silme
# ============================================

sayilar.remove(50)  # deger ile siler
print(sayilar)

sayilar.pop()       # son elemani siler
print(sayilar)

# ============================================
# Liste uzunlugu
# ============================================

print(len(sayilar))

# ============================================
# Liste icinde dongu
# ============================================

for isim in isimler:
    print(f"Merhaba {isim}")

# ============================================
# Liste icinde kontrol
# ============================================

if "Ercan" in isimler:
    print("Listede var")

# ============================================
# Liste toplama
# ============================================

sayilar = [10, 20, 30, 40]

toplam = 0
for sayi in sayilar:
    toplam += sayi

print("Toplam:", toplam)

# ============================================
# Mini Egzersiz
# ============================================

# 1) Bos bir liste olustur
# 2) Kullanicidan 5 sayi al
# 3) Listeye ekle
# 4) En buyuk sayiyi yazdir

# ============================================
# DAY 7 - ADVANCED COLLECTIONS
# ============================================

# ============================================
# 1️⃣ Nested Lists (Ic Ice Listeler)
# ============================================

# Bir listenin icinde baska listeler olabilir
ogrenciler = [
    ["Ali", 80],
    ["Ercan", 95],
    ["Ayse", 70]
]

print(ogrenciler)

# Belirli bir elemana erisme
print(ogrenciler[1])      # ["Ercan", 95]
print(ogrenciler[1][0])   # Ercan
print(ogrenciler[1][1])   # 95

# Dongu ile gezme
for ogrenci in ogrenciler:
    print(f"Isim: {ogrenci[0]}, Not: {ogrenci[1]}")

# ============================================
# 2️⃣ List Comprehension
# ============================================

# Klasik yontem
sayilar = [1, 2, 3, 4, 5]
kareler = []

for s in sayilar:
    kareler.append(s ** 2)

print(kareler)

# Pythonic yontem (🔥)
kareler2 = [s ** 2 for s in sayilar]
print(kareler2)

# Sartli list comprehension
ciftler = [s for s in sayilar if s % 2 == 0]
print(ciftler)

# Ornek:
# 1-20 arasindaki 3'e bolunen sayilar
bolunenler = [i for i in range(1, 21) if i % 3 == 0]
print(bolunenler)

# ============================================
# 3️⃣ Tuple (Degistirilemez Listeler)
# ============================================

# Tuple () ile tanimlanir
renkler = ("kirmizi", "mavi", "yesil")

print(renkler)
print(renkler[0])

# Tuple degistirilemez (immutability)
# renkler[0] = "sari"  # ❌ HATA

# Tuple genelde:
# - Sabit veriler
# - Performans
# - Guvenli veri tasima icin kullanilir

# ============================================
# 4️⃣ Set (Tekrarsiz Veri)
# ============================================

# Set {} ile tanimlanir
sayilar = {1, 2, 3, 3, 4, 4, 5}
print(sayilar)  # Tekrar edenler silinir

# Eleman ekleme
sayilar.add(10)
print(sayilar)

# Set icinde kontrol (cok hizlidir)
print(3 in sayilar)

# Iki set arasindaki fark
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a - b)  # a'da olup b'de olmayanlar
print(a | b)  # birlesim
print(a & b)  # kesisim

# ============================================
# 🧪 Mini Uygulama
# ============================================

# 1) Kullanicidan 5 sehir al
# 2) Tekrarlari kaldir
# 3) Alfabetik sirala
# 4) Liste olarak yazdir

# Ipucu:
# - set()
# - sorted()
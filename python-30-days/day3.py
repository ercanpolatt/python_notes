# ============================================
# DAY 3 - KOSULLAR
# ============================================

yas = 18

if yas >= 18:
    print("Resitsin")
else:
    print("Resit degilsin")

# elif kullanimi
not_ort = 75

if not_ort >= 85:
    print("AA")
elif not_ort >= 70:
    print("BB")
elif not_ort >= 50:
    print("CC")
else:
    print("Kaldi")

# Kullanicidan sayi alip tek mi cift mi kontrol etme

sayi = int(input("Bir sayi gir: "))

if sayi % 2 == 0:
    print("Cift")
else:
    print("Tek")

# Mini egzersiz:
# 1) Kullanici sifre girsin
# 2) Dogruysa "Giris basarili" yazdir
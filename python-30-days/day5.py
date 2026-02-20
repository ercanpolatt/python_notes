# ============================================
# DAY 5 - FONKSIYONLAR
# ============================================

# Fonksiyon tanimlama

def selamla():
    print("Merhaba")

selamla()

# Parametreli fonksiyon

def topla(a, b):
    return a + b

sonuc = topla(5, 3)
print(sonuc)

# Varsayilan parametre

def selam_ver(isim="Misafir"):
    print(f"Merhaba {isim}")

selam_ver()
selam_ver("Ercan")

# Mini proje:
# 1) Kullanicidan 2 sayi al
# 2) Toplama, cikarma, carpma, bolme yapan fonksiyonlar yaz
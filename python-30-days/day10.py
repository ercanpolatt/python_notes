# ============================================
# DAY 10 - EXCEPTION HANDLING
# ============================================

# Exception nedir?
# Program calisirken olusan hatalara exception denir.
# Ornek: string'i int'e cevirme hatasi

# ============================================
# 1️⃣ Basit try-except
# ============================================

try:
    sayi = int(input("Bir sayi gir: "))
    print("Girdigin sayi:", sayi)
except:
    print("Hata! Lutfen sayi gir.")

# ============================================
# 2️⃣ Spesifik hata yakalama
# ============================================

try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Sifira bolme hatasi!")
except ValueError:
    print("Tip hatasi!")

# ============================================
# 3️⃣ finally blogu
# ============================================

try:
    dosya = open("ornek.txt", "r")
except FileNotFoundError:
    print("Dosya bulunamadi.")
finally:
    print("Islem tamamlandi.")

# ============================================
# 4️⃣ else blogu
# ============================================

try:
    x = int(input("Bir sayi gir: "))
except ValueError:
    print("Hatali giris.")
else:
    print("Basarili giris:", x)

# ============================================
# 5️⃣ Kendi hatani olusturma (raise)
# ============================================

yas = int(input("Yasini gir: "))

if yas < 0:
    raise ValueError("Yas negatif olamaz!")

print("Yas kaydedildi.")

# ============================================
# 🧪 MINI PROJE - Guclu Hesap Makinesi
# ============================================

while True:
    try:
        print("\n1- Toplama")
        print("2- Cikarma")
        print("3- Carpma")
        print("4- Bolme")
        print("5- Cikis")

        secim = input("Secim: ")

        if secim == "5":
            print("Program kapatildi.")
            break

        a = float(input("Birinci sayi: "))
        b = float(input("Ikinci sayi: "))

        if secim == "1":
            print("Sonuc:", a + b)
        elif secim == "2":
            print("Sonuc:", a - b)
        elif secim == "3":
            print("Sonuc:", a * b)
        elif secim == "4":
            print("Sonuc:", a / b)
        else:
            print("Gecersiz secim.")

    except ValueError:
        print("Lutfen sayisal deger gir.")
    except ZeroDivisionError:
        print("Sifira bolme yapamazsin.")
    except Exception as e:
        print("Beklenmeyen hata:", e)
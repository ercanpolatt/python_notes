# ============================================
# DAY 9 - DOSYA ISLEMLERI
# ============================================

# Dosya acma formatı:
# open("dosya_adi", "mod")

# Modlar:
# "r"  -> read (okuma)
# "w"  -> write (yazma, eskiyi siler)
# "a"  -> append (sona ekler)
# "x"  -> create (yeni dosya olusturur)

# ============================================
# 1️⃣ Dosyaya Yazma
# ============================================

file = open("notlar.txt", "w")
file.write("Python ogreniyorum\n")
file.write("Bugun dosya islemlerini ogrendim\n")
file.close()

print("Dosyaya yazildi.")

# ============================================
# 2️⃣ Dosyayi Okuma
# ============================================

file = open("notlar.txt", "r")
icerik = file.read()
print("Dosya icerigi:")
print(icerik)
file.close()

# ============================================
# 3️⃣ Append (Sona Ekleme)
# ============================================

file = open("notlar.txt", "a")
file.write("Bu satir sonradan eklendi\n")
file.close()

# ============================================
# 4️⃣ with kullanimi (ONERILEN)
# ============================================

# with kullanildiginda close() yazmana gerek yoktur
with open("notlar.txt", "r") as file:
    print("With ile okuma:")
    print(file.read())

# ============================================
# 5️⃣ Satir Satir Okuma
# ============================================

with open("notlar.txt", "r") as file:
    for satir in file:
        print("Satir:", satir.strip())

# ============================================
# 🧪 MINI PROJE - Not Defteri Uygulamasi
# ============================================

while True:
    print("\n1- Not Ekle")
    print("2- Notlari Goruntule")
    print("3- Cikis")

    secim = input("Secim yap: ")

    if secim == "1":
        not_metni = input("Notunu yaz: ")
        with open("notes.txt", "a") as file:
            file.write(not_metni + "\n")
        print("Not kaydedildi.")

    elif secim == "2":
        try:
            with open("notes.txt", "r") as file:
                print("\nKayitli Notlar:")
                print(file.read())
        except FileNotFoundError:
            print("Henuz not yok.")

    elif secim == "3":
        print("Program kapatildi.")
        break

    else:
        print("Gecersiz secim.")
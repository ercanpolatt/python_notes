# ============================================
# DAY 8 - DICTIONARY (DICT)
# ============================================

# Dictionary nedir?
# Anahtar (key) - Deger (value) mantigiyla calisir.
# {} suslu parantez ile tanimlanir.

kullanici = {
    "isim": "Ercan",
    "yas": 25,
    "email": "ercan@mail.com",
    "aktif": True
}

print(kullanici)

# ============================================
# Degere erisme
# ============================================

print(kullanici["isim"])
print(kullanici["email"])

# get() kullanimi (guvenli erisim)
print(kullanici.get("yas"))
print(kullanici.get("telefon"))  # None doner, hata vermez

# ============================================
# Deger guncelleme
# ============================================

kullanici["yas"] = 30
print(kullanici)

# ============================================
# Yeni key ekleme
# ============================================

kullanici["sehir"] = "Bursa"
print(kullanici)

# ============================================
# Eleman silme
# ============================================

kullanici.pop("aktif")
print(kullanici)

# ============================================
# Dictionary icinde dongu
# ============================================

# Sadece keyler
for key in kullanici:
    print(key)

# Key - value birlikte
for key, value in kullanici.items():
    print(f"{key} : {value}")

# ============================================
# Nested Dictionary
# ============================================

kullanicilar = {
    "user1": {
        "isim": "Ali",
        "yas": 22
    },
    "user2": {
        "isim": "Ercan",
        "yas": 25
    }
}

print(kullanicilar["user2"]["isim"])

# ============================================
# 🧪 Mini Proje - Basit Kullanici Sistemi
# ============================================

users = {}

for i in range(2):
    username = input("Kullanici adi: ")
    password = input("Sifre: ")

    users[username] = {
        "password": password
    }

print(users)

# Giris kontrolu
login_user = input("Giris icin kullanici adi: ")
login_pass = input("Sifre: ")

if login_user in users and users[login_user]["password"] == login_pass:
    print("Giris basarili")
else:
    print("Hatali giris")
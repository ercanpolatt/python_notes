# ============================================
# DAY 4 - DONGULER
# ============================================

# for dongusu
for i in range(5):
    print(i)

# 1'den 10'a kadar yazdir
for i in range(1, 11):
    print(i)

# while dongusu
sayac = 0

while sayac < 5:
    print("Calisiyor...")
    sayac += 1

# break ve continue

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Mini egzersiz:
# 1) 1-100 arasi cift sayilari yazdir
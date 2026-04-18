# ============================================
# DAY 16 - ITERATORS & GENERATORS
# ============================================

# ============================================
# 1️⃣ Iterator Nedir?
# ============================================

# Liste aslinda iterable'dir
sayilar = [1, 2, 3]

iterator = iter(sayilar)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # StopIteration hatasi verir


# ============================================
# 2️⃣ Kendi Iteratorumuzu Yazalim
# ============================================

class Sayac:

    def __init__(self, max_sayi):
        self.max = max_sayi
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration


sayac = Sayac(5)

for i in sayac:
    print(i)


# ============================================
# 3️⃣ Generator Nedir?
# ============================================

# Generator fonksiyonlari yield ile calisir

def sayi_uret(max_sayi):
    i = 0
    while i < max_sayi:
        i += 1
        yield i


gen = sayi_uret(5)

for sayi in gen:
    print(sayi)


# ============================================
# 4️⃣ Generator vs Liste
# ============================================

# Liste (tum veriyi bellekte tutar)
liste = [i for i in range(1000000)]

# Generator (tek tek uretir)
gen = (i for i in range(1000000))


# ============================================
# 5️⃣ Mini Uygulama
# ============================================

# Fibonacci generator

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fibonacci(10):
    print(num)
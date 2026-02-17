# my_list = [1,3,"a"]
# print(type(my_list))
# my_tuple = (1,3,"a")
# print(type(my_tuple))
# my_set = {1,3,"a"}
# print(type(my_set))
# my_dict = {"a":1,"b":3}
# print(type(my_dict))

# my_superhero = input("enter superhero: ")
# my_superhero_list = ["Spider Man","Iron Man","Thor","Black Widow"]
# if my_superhero in my_superhero_list:
#     print(":)")
# else:
#     print(":(")

# from random import randint


# liste = [10,20,30,40,50,60,70,]

# for l in liste:
#     if l%6==0:
#         print(l)

# my_tuple_list = [(0,1,2),(3,4,5),(6,7,8),(9,10,11)]
# len(my_tuple_list)
# #4
# for (x,y,z) in my_tuple_list:
#     print(x)
# # 0
# 3
# 6
# 9


# my_dictionary = {"k1":100,"k2":200,"k3":300}

# # my_dictionary.items()
# # dicitems([('k1', 100), ('k2', 200), ('k3', 300)])
# # for (key,value) in my_dictionary.items():
# #     print(value)
# # 100
# # 200
# # 300
# for num in my_dictionary.values():
#     print(num)
# # 100
# # 200
# # 300

# print(list(range(10)))

# #enumerate

# my_list = [20,30,40,50,60]
# for element in enumerate(my_list):
#     print(element)
# (0, 20)
# (1, 30)
# (2, 40)
# (3, 50)
# (4, 60)
# for (ix,value) in enumerate(my_list):
#     print(value)
# 20
# 30
# 40
# 50
# 60
# #random
# from random import randint
# randint(0,100)

# my_list = [10,20,30,40,50,60,70]
# randint(0,len(my_list))
# my_list[randint(0,len(my_list)-1)]


# #zip
# food_list = ["apple","banana","melon"]
# calories_list = [100,150,200]
# day_list = ["monday","tuesday","wednesday"]
# zipped_list = list(zip(food_list,calories_list,day_list))
# type(zipped_list)
# list
# zipped_list
# [('apple', 100, 'monday'),
#  ('banana', 150, 'tuesday'),
#  ('melon', 200, 'wednesday')]
# new_list = []
# my_string = "metallica"

# for element in my_string:
#     new_list.append(element)



#4) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız
from random import randint


my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}
# cevap
if "c" in my_dictionary.values():
    print("c harfi sözlüğün değerlerinde geçiyor")
else:
    print("c harfi sözlüğün değerlerinde geçmiyor")

#5) Aşağıdaki sözlükte, anahtarlar içinde a harfinin geçip geçmediğini gösteren bir if koşulu yazınız
my_other_dictionary = {"b":203,"c":"a","a":400,"d":"f"}
# cevap
for key in my_other_dictionary.keys():
    if "a" in key:
        print("a harfi sözlüğün anahtarlarında geçiyor")
        break
#6) Aşağıdaki listedeki sayılardan sadece çift sayı olanları yazdıran bir kod yazınız.
my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]
# cevap
for num in my_numbers:
    if num % 2 == 0:
        print(num)
# cevap
#7) Aşağıdaki listedeki sayılar bir dairenin yarı çapını vermektedir. 
#Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2 * pi * r)  Pi 3.14 alınabilir.
r_list = [3,2,5,8,4,6,9,12]
for r in r_list:
    circumference = 2 * 3.14 * r
    print(circumference)
# cevap
# cevap
# cevap
#8) Aşağıdaki listede isim - yaş eşleşmelerinin bulunduğu yapılar mevcuttur.
# Sadece yaşların olduğu yeni ve ayrı bir liste oluşturunuz.
age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]
age_list = []
for (key,age) in age_name_list:
    age_list.append(age)
print(age_list)
# cevap
# cevap
#9) Aşağıdaki müzik gruplarından birini rastgele yazdıran bir kod yazınız
metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]
# cevap
# cevapS
print(metal_list[randint(0,len(metal_list)-1)])
#10) Aşağıdaki kodun çıktısı ne olacaktır?
number_list = [5,7,18,21,20,10,405,24]
[num % 2 == 0 for num in number_list]

# cevap
# cevap
# cevap
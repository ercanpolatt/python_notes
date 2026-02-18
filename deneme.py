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

#deneme

def divideNumber(number):
    return number / 2

myList = [3,5,7,10,20,30]

for num in myList:
    print(divideNumber(num))
# a = 4
# print(isinstance(a, int))


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
a = []
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
# print("Убрали элемент1", data_structure)
# # data_structure.pop()
# print()
# print("Убрали элемент2", data_structure)
# data_structure.pop()
# print()
# print("Убрали элемент3", data_structure)
# data_structure.pop()
# print()
# print("Убрали элемент4", data_structure)
# data_structure.pop()
# print()
# print("Убрали элемент", data_structure)

# # повторяющееся вытаскивание из общего списка
# print()
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
# print("Убрали элемент1", data_structure)
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
# print("Убрали элемент1", data_structure)
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
# print("Убрали элемент1", data_structure)
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
# print("Убрали элемент1", data_structure)

# #повторяющееся вытаскивание из общего списка
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
#
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
#
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
#
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
#
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)



# #повторяющееся вытаскивание из общего списка
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
# last_1 = list(last).pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last_1)
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
#
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
#
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
#
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)
#повторяющееся вытаскивание из общего списка
#
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)                                                     # ((), [{(2, 'Urban', ('Urban2', 35))}])
# last_1 = list(last).pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last_1)                                                   # [{(2, 'Urban', ('Urban2', 35))}]
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)                                                      # Hello
# last_1 = list(last).pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last_1)                                                    # o
# print()
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)                                                       # (6, {'cube': 7, 'drum': 8})
# last_1 = list(last).pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last_1)                                                    # {'cube': 7, 'drum': 8}
# print()
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)                                                       # {'a': 4, 'b': 5}
# last_1 = list(last).pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last_1)                                                    # b
# print()
# print()
# last = data_structure.pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last)                                                      # [1, 2, 3]
# last_1 = list(last).pop()  # ытащили последний, и его надо разобрать
# print("Оставили", last_1)                                                    # 3
# print()



last = data_structure.pop()  # ытащили последний, и его надо разобрать
print("Оставили", last)                                                     # ((), [{(2, 'Urban', ('Urban2', 35))}])
last_1 = list(last).pop()  # ытащили последний, и его надо разобрать
print("Оставили", last_1)                                                   # [{(2, 'Urban', ('Urban2', 35))}]
last_2= list(last_1).pop()  # ытащили последний, и его надо разобрать
print("Оставили", last_2)                                                   # [{(2, 'Urban', ('Urban2', 35))}]

print()
print()

last = data_structure.pop()  # ытащили последний, и его надо разобрать
print("Оставили", last)                                                      # Hello
last_1 = list(last).pop()  # ытащили последний, и его надо разобрать
print("Оставили", last_1)                                                   # o
last_2= list(last_1).pop()  # ытащили последний, и его надо разобрать
print("Оставили", last_2)

print()
print()

last = data_structure.pop()  # ытащили последний, и его надо разобрать
print("Оставили", last)                                                       # (6, {'cube': 7, 'drum': 8})
last_1 = list(last).pop()  # ытащили последний, и его надо разобрать
print("Оставили", last_1)                                                    # {'cube': 7, 'drum': 8}
last_2= list(last_1).pop()  # ытащили последний, и его надо разобрать
print("Оставили", last_2)

print()
print()

last = data_structure.pop()  # ытащили последний, и его надо разобрать
print("Оставили", last)                                                       # {'a': 4, 'b': 5}
last_1 = list(last).pop()  # ытащили последний, и его надо разобрать
print("Оставили", last_1)                                                    # b
last_2= list(last_1).pop()  # ытащили последний, и его надо разобрать
print("Оставили", last_2)

print()
print()

last = data_structure.pop()  # ытащили последний, и его надо разобрать
print("Оставили", last)                                                      # [1, 2, 3]
last_1 = list(last).pop()  # ытащили последний, и его надо разобрать
print("Оставили", last_1)                                                    # 3
last_2= list(str(last_1)).pop()  # ытащили последний, и его надо разобрать
print("Оставили", last_2)

print()

# #  3 модуль, урок "Произвольное числог параметров"
# #  https://urban-university.ru/members/courses/course999421818026/20231008-0000proizvolnoe-cislo-parametrov-490467350029
#
# def test_func(*params):
#     print('Тип:', type(params))
#     print('Аргумент:', params)
#
#
# test_func(1, 2, 3, 4)
# print()

#
# def summator(txt, *values, type='sum'):  # сумма чисел
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt} {s} {type}'
#
#
# print(summator("Сумма чисел: ", 2, 3, 4, type='summator'))
# print()


# def info(*types, names_="Den", **values):
#     print('Тип:', type(values))
#     print('Аргумент:', values)
#     for key, value in values.items():
#         print(key, value)
#     print(types)
#
# info(1, 2, 3, 4, names_='Denis', name= 'Den', cource="Python", cources="It")

# нахождение суммы чисел, суммы квадратов, суммы кубов, тюе эта ф-я будет принимать какую-то степень этих чисел
# n - степень, *args -какое то колво произвольных параметров и txt - именованный парамент текст.

# def my_sum(n, *args, txt="Сумма чисел"):
#     s = 0  # создадим переменную с 0, к которому будем приплюсовывать
#     for i in range(len(args)):  # здесь используем длину, так как args передаются в виде кортежа
#         s += args[i] ** n  # мы будем брать из наших args, возводить его а степень n и прибавлять к нашей переменной s
#     print(txt + ":", s)
# my_sum(1, 1,2,3,4,5)
# my_sum(2, 1,2,3,4,5, txt='Сумма квадратов') # Сумма квадратов, n - степень 2
# my_sum(3, 1,2,3,4,5, txt='Сумма кубов') # Сумма кубов, n - степень 3

# Самостоятельная работа. Задача "Однокоренные":

def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():  # с нижним регистром
            same_words.append(i.lower())  # переводим в нижний и добавляем в список
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)


def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():  # с нижним регистром
            same_words.append(i)  #  добавляем в список
        if i.lower() in root_word.lower():  # с нижним регистром
            same_words.append(i)  #  добавляем в список
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

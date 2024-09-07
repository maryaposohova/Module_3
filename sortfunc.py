# Пузырьковая сортировка

""" Пуз сортировка работает таким образом, что у нас проверяются элементы так: сначала беруться первые 2, сравниваются
между собой, и если' один эл больше или меньше другого(в зависимости от того, что вы пропишите в условиях) они будут
меняться местами. Но после того, как мы пробежимся по списку, нам нужно будет пробегаться еще раз. и кол во таких
повторений, чтобы убедиться в том, что список отсортирован, может увеличиваься очень сильно(если он очень большой).
Сложность алгоритма O(n^2), т.е. сложность очень сильно зависит от кол ва элементов. Мы можем создать отимизацию,
создать переменноую, чтобы посмотреть произошла ли смена мест во время итерации(swapped = True), чтобы потом не
запускать снова цикл для перебора этих же чисел."""

'''ДАльше мы можем запустить цикл, кот будет основан на этой переменной(вайл, а внутри фор). Он будет повторять энное
кол во переборов, до тех пор, пока элементы будут меняться местами, как только они перстанут меняться местами, 
соответственно цикл вайл остановится и следующие итерации для цикла фор запускаться не будут.'''

'''Единицу в длине в цикле фор  вычли для того. чтобы избежать ошибок, связанных с обращением к несуществующему элементу,
например, если мы будем обращаться по индексу, мы помним, что в списке мы можем взять элемент по его индексу, и когла 
мы находимся на предпосдеднем и последнем элементе, если не сделать эту минус один, то мвы получим ошибку. 
Дальше нам просто нужно проверить, если наш элемент из списка (i) болше, чем элемент i + 1? (т.е. мы берем два соседних 
элемента), и меняем их местами.
И если после сравнения эта смена произошла, поменяли, то мы этот флаг swapped = True 
устанавливаем в тру. Это позволит нам перейти на следующую итерацию. 
А если этого не произойдет, у нас как только цикл фор отработает, мы пробежимся по все элементам, и если не было замен, 
- значение сваппед установится в фолс, и мы заново не сможем запустить. Это явл. некой оптимизацией добавление вот этих 
swapped.'''

nums = [5, 6, 2, 1, 3, 4]


def bubble_sort(ls):  # создаем ф в кот будем циклом пробегаться по определенному массиву
    swapped = True  # переменная флаг для контроля, произошла ли смена мест
    while swapped:  # запускаем цикл вайл
        swapped = False  # и переменную выставляет в фолс
        for i in range(
                len(ls) - 1):  # запускаем фор, кот. будет повторяться столько раз, сколько элементов в нашем списке, но вычитая 1
            if ls[i] > ls[i + 1]:  # проверяем на наличие в последних элементах
                ls[i], ls[i + 1] = ls[i + 1], ls[i]  # меняем местами
                swapped = True  # если смена произошла, флан устанавливаем в тру, и цикл по перебору снова запускается


# bubble_sort(nums)
# print(nums)

# Сортировка выборкой.
''' Принцип работы - мы как бы создаем один массив внутр другого. 
 Т.е. у нас будет отсортированная часть и неотсортированная. И перебирать мы будем элементы в неотсортированной части.
    !!! Нам понадобятся вложеннын циклы.
 Предположим, что первым попадется самый маленький, устанавливаем  lower = i 
 И дальше мы должны пройтись по неотсортированной части
 Для этого нам нужен еще один цикл j, но который будет запускаться с i + 1, т.е. со следующих элементов и там мы будем
 эти элементы в неотсортированной части и будем сравнивать их с индексом самого маленького значения  lowest.
 Т.е. если в списке элемент j будет меньше, чем элемент lowest, то мы говорит, что у нас самый маленький элемент 
 будет новым как бы, мы ему даем значение j.
    А после нашего цикла нужно взять элемент с индексом i , затем элемент с индексом lowest и поменять их местами.
'''

def selection_sort(ls):
    for i in range(len(ls)): # 1 цикл i, будет запускатьяс в диапазоне, равнов кол ву эл-в  в списке. И равно будет кол-ву отсортированных значений.
        lowest = i    # индекс самого маленького элемента, на него будем опираться
        for j in range(i + 1, len(ls)):    # запускаем второй цикл со след элементов
            if ls[j] < ls[lowest]:  # сравниваем элементы с индексом lowest
                lowest = j         #  даем значение j
        ls[i], ls[lowest] = ls[lowest], ls[i]     # меняем местами сравненные элементы


selection_sort(nums)
print(nums)
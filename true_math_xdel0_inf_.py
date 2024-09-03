# при делении на 0 результат бесконечность


from math import inf


def divide(first, second):
    if second == 0:
        return inf
    return first / second


# print(divide(10, 0))

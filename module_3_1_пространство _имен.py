# Задача "Счётчик вызовов":

calls = 0

def calls_():
    global calls
    calls = calls + 1
    # print(calls)


def string_info(string):
    calls_()
    str_lower = string.lower()
    str_upper = string.upper()
    str_ = str(len(str_lower))
    return f'{str_}, {str_lower}, {str_upper}'


def is_contains(string, list_to_search):
    calls_()
    string_lower = string.lower()
    return string_lower in (i.lower() for i in list_to_search)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

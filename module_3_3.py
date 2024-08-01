#1.Функция с параметрами по умолчанию:

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2, 'остров', True)
print_params(2, 'остров', 1)
print_params(2, 'game', [1, 2, 3])

#2.Распаковка параметров:
values_list = [11, 'victory', True]
values_dict = {'a': 33, 'b': True, 'c': 'the best'}

print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:

values_list_2 = ['friends', 1990]
print_params(*values_list_2, 42)


#Примечание
def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)
    print(list_my)


append_to_list('Julia', None)

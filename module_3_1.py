def count_calls():
    global calls
    calls = calls + 1
    return


def string_info(stroka):
    otdacha = []
    otdacha.append(len(stroka))
    otdacha.append(stroka.upper())
    otdacha.append(stroka.lower())
    otdacha = tuple(otdacha)
    count_calls()
    return otdacha


def is_contains(contains, my_list):
    x = 'FALSE'
    for i in range(len(my_list)):
        if type(my_list[i]) != list:
            if contains.lower() == my_list[i].lower():
                x = 'TRUE'
                count_calls()
                return x
        else:
            z = my_list[i]
            for j in range(len(z)):
                if contains.lower() == z[j].lower():
                    x = 'TRUE'
                    return x
    count_calls()
    return x


calls = 0


print(string_info('БульБулЯтоР'))
print(string_info('Транжира'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('Urban', ['Вертолет', 'Автожир', ['Дерижабль', 'Самолет']]))
print(calls)


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


# def is_contains:


calls = 0
string = 'ygUYLltqyueLHG986jhjhk'
contains = 'БульБулЯтоР'
spisok = ['Вертолет', 'Автожир', 'Бульбулятор', 'Самолет']

print(string_info(string))
print(calls)
a = ['cycle', ['recycling', 'cyclic']]
print(len(a))
print(len(a[1]))

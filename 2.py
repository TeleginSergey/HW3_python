
#первое число Морса-Туэ
arr = [0]

def morsa():
    #счётчик чисел на данный момент
    count = 0
    #пока не больше заданного кол-ва чисел(если идельно подходит, т.е. инверсию делаем полностью всего списка, а не тольок часть)
    while count < n:
        count += 1
        for i in range(len(arr)):
            #если длина = заданному число, то вывод(выполняем инверсию только часть сейчас имеющегося списка)
            if n == len(arr):
                return arr
            #если 0, то добавляем 1 в конец
            if arr[i] == 0:
                arr.append(1)
            #если 1, то добавляем 0 в конец
            else:
                arr.append(0)
    return arr
#кол-во цифр в выводе
n = int(input())

print(*morsa())
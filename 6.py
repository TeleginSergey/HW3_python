#Вхрдные данные(кол-во строк и символов в них)
n = int(input())
#двумерный список, где будут храниться входные данные
mas = []
#входные данные
for i in range(n):
    arr = list(map(int, input().split()))
    mas.append(arr)

def IsSymmetric():
    #создадим новый массив, для того чтобы потом сравнить его с изначальным
    mas_clone = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            #если массив симметричный, то если столбцы превратить в строки, то будет то же самое
            mas_clone[i].append(mas[j][i])
    #сравниваем массивы
    if mas_clone == mas:
        return 'YES'
    return 'NO'




print(IsSymmetric())
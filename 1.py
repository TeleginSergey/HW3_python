
def can_eat(kon, fig):
    #входные данные
    x1, y1 = kon
    x2, y2 = fig
    #конь ходит либо (по оси х на 2 и по оси y на 1), либр (по оси х на 1 и по оси y на 2)
    if (abs(x1 - x2) == 1 and abs(y1-y2) == 2) or (abs(x1 - x2) == 2 and abs(y1-y2) == 1):
        return True
    return False

result = can_eat((2, 1), (4, 2))

print("result = ", result)

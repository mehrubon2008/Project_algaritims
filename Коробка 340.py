"""
Коробки 340
(Время: 1 сек. Память: 16 Мб Сложность: 19%)
На столе лежат коробка размера A1 × B1 × C1 и коробка размера A2 × B2 × C2. Выясните можно ли одну из этих коробок положить в другую,
 если разрешены повороты коробок вокруг любого ребра на угол 90 градусов.

Входные данные
Первая строка входного файла содержит три целых числа A1, B1 и C1. Вторая строка входного файла содержит три целых числа A2, B2 и C2.
 Все числа положительны и не превосходят 1000.

Выходные данные
Если коробки одинаковы, выведите "Boxes are equal". Если первая коробка может быть положена во вторую, выведите "The first box is smaller than the second one".
 Если вторая коробка может быть положена в первую, выведите "The first box is larger than the second one". Иначе, выведите "Boxes are incomparable".
"""


def main():
    line = list(map(int, input().split()))
    a = []
    b = []
    for i in range(3):
        a.append(int(line[i]))

    line = list(map(int, input().split()))
    for i in range(3):
        b.append(int(line[i]))

    a.sort()
    b.sort()
    k = True
    count = 0
    if a[0] > b[0]:
        if a[1] >= b[1]:
            if a[2] >= b[2]:
                ans = "The first box is larger than the second one"
            else:
                ans = "Boxes are incomparable"
        else:
            ans = "Boxes are incomparable"
    else:
        if a[0] < b[0]:
            if a[1] <= b[1]:
                if a[2] <= b[2]:
                    ans = "The first box is smaller than the second one"
                else:
                    ans = "Boxes are incomparable"
            else:
                ans = "Boxes are incomparable"
        else:
            if a[1] > b[1]:
                if a[2] >= b[2]:
                    ans = "The first box is larger than the second one"
                else:
                    ans = "Boxes are incomparable"
            else:
                if a[1] < b[1]:
                    if a[2] <= b[2]:
                        ans = "The first box is smaller than the second one"
                    else:
                        ans = "Boxes are incomparable"
                else:
                    if a[2] > b[2]:
                        ans = "The first box is larger than the second one"
                    else:
                        if a[2] < b[2]:
                            ans = "The first box is smaller than the second one"
                        else:
                            ans = "Boxes are equal"
    print(ans)


if __name__ == '__main__':
    main()

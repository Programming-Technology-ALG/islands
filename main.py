# Храним массив размера [2][n]
# в 1 строке храним предыдущий шаг
# на 1 итерации когда встречаем землю - ставим ей номер
# если земли связаны, то всему острову ставим один и тот же номер
# когда мы видим, что у номера больше нет соседей, увеличиваем количество островов
# как это выглядит на практике
#   вот тест
#   #00#0
#   ####0
#   0000#
#   ##0#0
#   ##### (ред.)
# 1 итерация
#   10020
# 2 итерация:
#   10010
#   11110
# 3 итерация:
#   11110
#   00002
# увеличиваем количество островов
# 4 итерация:
#   00002
#   33040
# увеличиваем количество островов
# 5 итерация:
#   33030
#   33333
# увеличиваем количество островов


# def max_arr() -> int:
#     max_el = -1
#     for ind in range(N):
#         if array[0][ind] != '0':
#             max_el = max(max_el, array[0][ind])
#     return max(max_el, num - 1)


N = int(input())
array = [[0 for _ in range(N)] for _ in range(2)]
num = 1
array[0] = list(input())
for j in range(N):
    if array[0][j] == 'x':
        array[0][j] = num
        num += 1
        if j + 1 < N:
            if array[0][j + 1] == 'x':
                array[0][j + 1] = array[0][j]
            else:
                j += 1
for _ in range(N - 1):  # Считываю остальные строки в array[1]
    array[1] = list(input())
    if array[1] == ['0' for _ in range(N)]:
        break
    for j in range(N):
        temp_arr = []
        temp_num = num
        for p in range(j, N):
            if array[1][p] == 'x':
                temp_arr.append(p)
            else:
                break
        if len(temp_arr) != 0:
            for index in temp_arr:
                if array[0][index] != '0':
                    temp_num = min(array[0][index], temp_num)
                if array[0][index] == num - 1:
                    num -= 1
            for index in temp_arr:
                array[1][index] = temp_num
            if temp_num == num:
                num += 1
    array[0] = array[1]  # Переставляю строку на уровень выше

# print(max_arr())
print(num - 1)

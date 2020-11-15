# ==========================
# ======= GENERATOR ========
import random
import sys


def generate():
    k = random.randint(100, 250)
    print(k)
    for i in range(k):
        output = ""
        j = 0
        while j < k:
            if j < k and round(random.random()) == 1:
                output += '0'
                j += 1
            if j < k and round(random.random()) == 1:
                output += 'x'
                j += 1
        print(output)
    print("-> ")
    return


# generate()
# sys.exit(0)

# ======= GENERATOR ========
# ==========================


#
#
# def max_arr(ar) -> int:
#     max_el = -1
#     for ind in ar:
#         if array[0][ind] != '0':
#             max_el = max(max_el, array[0][ind])
#     return max_el
#
#
# def min_arr(ar) -> int:
#     min_el = 999999999
#     for ind in ar:
#         min_el = min(min_el, array[1][ind])
#     return min_el
#
#
# N = int(input())
# array = [[0 for _ in range(N)] for _ in range(2)]
# serial_number = 1
# count = 0
# array[0] = list(input())
# while array[0] == ['0' for _ in range(N)] and N > 1:
#     array[0] = list(input())
#     N -= 1
# for j in range(N):
#     temp_arr = []
#     for p in range(j, N):
#         if array[0][p] == 'x':
#             temp_arr.append(p)
#         else:
#             break
#     for index in temp_arr:
#         array[0][index] = serial_number
#     if len(temp_arr) != 0:
#         serial_number += 1
#
# for _ in range(N - 1):  # Считываю остальные строки в array[1]
#     array[1] = list(input())
#     if array[1] == ['0' for _ in range(N)]:
#         break
#     for j in range(N):
#         temp_arr = []
#         temp_num = serial_number
#         for p in range(j, N):
#             if array[1][p] == 'x':
#                 temp_arr.append(p)
#             else:
#                 break
#         if len(temp_arr) != 0:
#             for index in temp_arr:
#                 if array[0][index] != '0':
#                     temp_num = min(array[0][index], temp_num)
#                 if array[0][index] == serial_number - 1:
#                     serial_number -= 1
#             for index in temp_arr:
#                 array[1][index] = temp_num
#             if temp_num == serial_number:
#                 serial_number += 1
#         #
#         # count = count_branch(temp_arr)
#         # if count > 1:
#         #     for g in range(N):
#         #         if array[1][g] != '0':
#         #             if array[1][g] > max_arr(temp_arr):
#         #                 array[1][g] -= count
#         #
#         # ту ду
#         #
#         # if count > 1:
#         #     if max_arr(temp_arr) + 1 == serial_number: # максимум из верхних элементов + 1 раверн нам(значит с него был переход к новому нам)
#         #         serial_number = min_arr(temp_arr) + 1
#         #
#         # должно быть условие на случай объединения верхних веток
#         # при объединении элементов строки 1 объекдинять и строку выше, запоминая максимум из них
#         # если максимум из них был + 1 равен хоть какому- нибудь элементу, то вычитаем из всех независимых номеров разницу = макс - обновл значение ячейки макс
#     array[0] = array[1]  # Переставляю строку на уровень выше
#
# print(serial_number - 1)


def countChange(count, max, min) -> int:
    for index in range(N):
        if array[0][index] == max:
            array[0][index] = min
        if array[1][index] == max:
            array[1][index] = min
    count += 1
    return count


def refactor(index_i: int) -> None:
    for index_j in range(N):
        if array[index_i][index_j] == 'x':
            array[index_i][index_j] = 0
        else:
            array[index_i][index_j] = -1
    return


serial_number = 0
change_counter = 0
N = int(input())
array = [[0 for _ in range(N)] for _ in range(2)]

array[0] = list(input())  # Считываю первую строку
if array[0] != ['0' for _ in range(N)]:
    refactor(0)
    for i in range(N):
        if array[0][i] == 0:
            array[0][i] = serial_number + 1
            if i > 0:
                if array[0][i - 1] > 0:
                    array[0][i] = array[0][i - 1]
            if array[0][i] == serial_number + 1:
                serial_number += 1

for _ in range(N - 1):  # Считываю оставшиеся строки
    array[1] = list(input())
    if array[1] == ['0' for _ in range(N)]:
        continue
    refactor(1)
    for i in range(N):
        if array[1][i] == 0:
            if i > 0 and 0 < array[0][i] != array[1][i - 1] > 0:
                array[1][i] = min(array[0][i], array[1][i - 1])
                change_counter = countChange(change_counter, max(array[0][i], array[1][i - 1]), array[1][i])
            elif array[0][i] > 0:
                array[1][i] = array[0][i]
            elif i > 0 and array[1][i - 1] > 0:
                array[1][i] = array[1][i - 1]
            else:
                serial_number += 1
                array[1][i] = serial_number
    array[0] = array[1]

print(serial_number - change_counter)

# ==========================
# ======= GENERATOR ========

# import random
# import sys
#
#
# def generate():
#     k = random.randint(100, 250)
#     print(k)
#     for i in range(k):
#         output = ""
#         j = 0
#         while j < k:
#             if j < k and round(random.random()) == 1:
#                 output += '0'
#                 j += 1
#             if j < k and round(random.random()) == 1:
#                 output += 'x'
#                 j += 1
#         print(output)
#     print("-> ")
#     return


# generate()

# ======= GENERATOR ========
# ==========================


def countChange(count, max_ser, min_ser) -> int:
    for index in range(N):
        if array[0][index] == max_ser:
            array[0][index] = min_ser
        if array[1][index] == max_ser:
            array[1][index] = min_ser
    count += 1
    return count


serial_number: int = 0
change_counter: int = 0
N = int(input())
empty_list = ['0' for _ in range(N)]
array = [empty_list for _ in range(2)]

array[0] = list(input())  # Считываю первую строку
if array[0] != empty_list:
    for i in range(N):
        if array[0][i] == 'x':
            array[0][i] = serial_number + 1
            if i > 0 and '0' != array[0][i - 1] != 'x':
                array[0][i] = array[0][i - 1]
            if array[0][i] == serial_number + 1:
                serial_number += 1

for _ in range(N - 1):  # Считываю оставшиеся строки
    array[1] = list(input())
    for i in range(N):
        if array[1][i] == 'x':
            if i > 0 and 'x' != array[0][i] != '0' and 'x' != array[1][i - 1] != '0' and array[0][i] != array[1][i - 1]:
                array[1][i] = min(array[0][i], array[1][i - 1])
                change_counter = countChange(change_counter, max(array[0][i], array[1][i - 1]), array[1][i])
            elif 'x' != array[0][i] != '0':
                array[1][i] = array[0][i]
            elif i > 0 and 'x' != array[1][i - 1] != '0':
                array[1][i] = array[1][i - 1]
            else:
                serial_number += 1
                array[1][i] = serial_number
    array[0] = array[1]

print(serial_number - change_counter)

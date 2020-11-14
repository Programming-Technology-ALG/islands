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
r = N - 1
while array[0] == ['0' for _ in range(N)] and N > 0:
    array[0] = list(input())
    N -= 1
for j in range(N):
    temp_arr = []
    for p in range(j, N):
        if array[0][p] == 'x':
            temp_arr.append(p)
        else:
            break
    for index in temp_arr:
        array[0][index] = num
    if len(temp_arr) != 0:
        num += 1
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

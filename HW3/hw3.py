from random import randint

M = 0
while not M:
    user_input = input('Input any number > 5: ')
    if int(user_input) > 5 and user_input.isdigit():
        M = int(user_input)
    else:
        print('you need input number > 5. Try again!')

matrix = [[randint(1, 50) for _ in range(M)] for _ in range(M)]

list_sum = [0] * len(matrix[0])
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        list_sum[j] += matrix[i][j]


def sorting(mtx, sum_list):
    for k in range(len(sum_list) - 1):
        flag = True
        for d in range(len(sum_list) - 1 - k):
            if sum_list[d] > sum_list[d + 1]:
                sum_list[d], sum_list[d + 1] = sum_list[d + 1], sum_list[d]
                for o in range(len(mtx)):
                    mtx[o][d], mtx[o][d + 1] = mtx[o][d + 1], mtx[o][d]
                flag = False
        if flag:
            break

    for k in range(len(mtx)):
        for d in range(len(mtx) - 1):
            flag = True
            for o in range(len(mtx) - 1 - d):
                if mtx[o][k] > mtx[o + 1][k] if k % 2 else mtx[o][k] < mtx[o + 1][k]:
                    mtx[o][k], mtx[o + 1][k] = mtx[o + 1][k], mtx[o][k]
                    flag = False

            if flag:
                break


def output_result(mtx, sum_list):
    for k in range(len(mtx)):
        for d in range(len(mtx[k])):
            print(f'{mtx[k][d]:>6}', end='')
        print()
    print()

    for h in range(len(sum_list)):
        print(f'{sum_list[h]:>6}', end='')
    print()


print('Before sorting:')
output_result(matrix, list_sum)
sorting(matrix, list_sum)
print('After sorting:')
output_result(matrix, list_sum)

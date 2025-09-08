# arr = [1, 2, 3, 4]
#
# for i in range(1 << len(arr)):
#     for idx in range(len(arr)):
#         if i & (1 << idx):
#             print(arr[idx], end=' ')
#         print()
#
# print('----------------------------')


arr = ['A', 'B', 'C']
n = len(arr)


def get_sub(tar):
    print(f'target = {tar}', end=' / ')

    for i in range(len(arr)):
        if tar & 0x1:
            print(arr[i], end=' ')
        tar >>= 1


for target in range(1 << n):
    get_sub(target)
    print()
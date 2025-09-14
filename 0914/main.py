# arr = range(1,11)
# N = len(arr)

# def find_subsets(k, current_subset):
#     if sum(current_subset) > 10:
#         return

#     if k == N:
#         if k == N:
#             if sum(current_subset) == 10:
#                 print(*current_subset)
#         return

#     find_subsets(k+1, current_subset + [arr[k]])
#     find_subsets(k+1, current_subset)

# find_subsets(0, [])

arr = [1,2,3]
N = len(arr)

def dfs(k, subset):
    if k == N:
        print(subset)
        return
    
    dfs(k + 1, subset + [arr[k]])
    dfs(k + 1, subset)

dfs(0, [])
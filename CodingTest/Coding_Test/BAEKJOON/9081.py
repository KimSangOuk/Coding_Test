import sys
input = sys.stdin.readline

def next_permutation(arr):
    n = len(arr)
    i = n - 2

    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i == -1:
        return None

    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]

    arr = arr[:i + 1] + arr[i + 1:][::-1]

    return arr

for _ in range(int(input())):
    arr = list(input().strip())
    result = next_permutation(arr)
    if result:
        print("".join(result))
    else:
        print("".join(arr))

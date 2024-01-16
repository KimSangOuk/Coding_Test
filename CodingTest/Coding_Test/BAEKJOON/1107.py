# 풀이시간 1시간 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 리모컨을 입력하는 수 범위 내에서 모든 수에서 입력가능한 수로부터의 변화값 중 최솟값이나 처음 100부터의 값의 변화값 중에 최소값을 찾아 출력하는 브루트 포스 알고리즘 문제

import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))

min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break

        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)
from collections import deque

def solution(prices):
  answer = []
  prices = deque(prices)
  while prices:
    k = prices.popleft()

    count = 0
    for i in prices:
      if k > i:
        count += 1
        break
      count += 1

    answer.append(count)

  return answer

print(solution([1,2,3,2,3])) # [4,3,1,1,0]
print(solution([2,1,3,4,5])) # [1,3,2,1,0]
print(solution([2,4,5,4,1])) # [3,2,1,1,0]
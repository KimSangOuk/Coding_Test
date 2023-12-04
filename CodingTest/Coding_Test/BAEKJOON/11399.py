# 풀이시간 11분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 일단 사람의 수가 1000명 보다 작거나 같기 때문에 O(N^2)까지의 알고리즘을 사용할 수 있다는 것을 알았다.
# 그리고 풀면서 시간 순으로 정렬한 현재까지의 합과 현재의 사람이 걸리는 시간을 구하면 되는 규칙이 나왔기에 그리디 알고리즘으로 간단히 풀 수 있었다.

n=int(input())
arr=list(map(int,input().split()))
arr.sort()

result=0
sum=0
for i in arr:
  sum+=i
  result+=sum

print(result)
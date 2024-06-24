# 풀이시간 40분/60분 시간제한 10초 메모리제한 128MB
# 2회차 풀이
# 하나의 행씩 퀸을 두어가며 그 경우가 서로 공격할 수 없는지 따져가는 문제이다. dfs로 모든 경우를 탐색하는 완전탐색 문제라고 할 수 있다.

def queen_possible(now):
  num=len(now)

  last=now[-1]
  
  for i in range(0,num-1):
    if abs(last-now[i])==abs((num-1)-i):
      return False
  return True

def dfs(deep):
  global count
  if deep!=0 and not queen_possible(now):
    return False
  if deep==n:
    if queen_possible(now):
      count+=1
  else:
    for i in range(0,n):
      if i not in now:
        now.append(i)
        dfs(deep+1)
        now.pop()

count=0
now=[]
n=int(input())
dfs(0)
print(count)

# 풀이시간 120분/60분 시간제한 10초 메모리제한 128MB
# 1회차 정답 but 풀이시간 너무 오래 걸림
# 처음에 단순히 각 칸에서 순열이나 조합을 써서 풀려고 하였으나 만약 최대 수인 15일 경우 15! 가 발생하기 때문에 너무 큰 숫자가 되어 메모리제한이나 시간초과가 걸린다는 것을 알았다. 여기서 시간을 먼저 많이 썼다.
# 그래서 생각한 것이 조합이나 순열을 구현해서 각 경우를 따로 다 저장하지 않고 풀어야 메모리제한에 걸리지 않겠다고 생각했다. 그래서 순열을 재귀함수로 만들기로 마음먹었다. 그렇게 진행하던 중, 각 수가 겹치지 않게 구현하는데 까지는 성공시켰다. 하지만 여기서도 시간초과가 발생하였다. 그래서 대각선이 이루어지지 않게까지 해야겠다는 생각이 들었다.
# 그래서 추가 될때마다 다른 것들과 대각선을 이루는지 검사하는 함수를 만들기로 하고 각 수가 추가되는 부분에 이 check함수를 넣기로 하였다. 이렇게 재귀함수를 구현하고 각 조건을 만족시키는 경우까지 만들어내는데 2시간이 걸렸다.

# 일단 조합이나 순열을 쓸 때, 메모리제한이 10이상으로 넘어가면 생길 만하다는 것을 깨달았다. 수가 말도 안되게 커지기 때문에 이 점을 유의하고 있어야한다는 것을 배웠다.
# 두번째는, 순열을 구현하는 방법과 이것에 조건을 붙이는 방법에 대해 어느 정도 배웠다. 좋은 경험이 될 것 같다.
# 다시 한번 풀어 보기로 하였다.

# n=int(input())
# count=0

# def permu(arr,n):
#   global count
#   if len(arr)==n:
#     # print(arr)
#     # result=check(arr,n)
#     # if result:
#     count+=1
#     return
#   for i in range(n):
#     if i not in arr:
#       arr.append(i)
#       if check(arr,len(arr)):
#         permu(arr,n)
#       arr.remove(i)
      

# def check(arr,n):
#   new=arr[-1]
#   for i in range(n-1):
#     if abs(arr[i]-new)==abs(i-(n-1)):
#       return False
#   return True

# permu([],n)
# print(count)
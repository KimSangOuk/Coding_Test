# - 각 호실의 앞자리는 나누어 떨어질 경우 높이 자체가 되고 그렇지 않을 경우, 나누었을 때 나머지 값과 같아진다. 또한 뒷의 2자리는 나눈 값과 +1을 한 값으로 나누어진다.
# - 풀이시간 : 10분

for _ in range(int(input())):
  h,w,n=map(int,input().split())
  f=n%h
  b=n//h+1
  if n%h==0:
      print(str(h)+str(n//h).zfill(2))
  else:
      print(str(f)+str(b).zfill(2))
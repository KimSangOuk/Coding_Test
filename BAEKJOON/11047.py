# '이것이 취업을 위한 코딩테스트다' '3-1.py'의 동전문제와 유사

n,k=map(int,input().split())
coin=[]
for i in range(n):
  coin.append(int(input()))

coin.sort(reverse=True)
count=0
for i in coin:
  count+=k//i
  k=k%i

print(count)
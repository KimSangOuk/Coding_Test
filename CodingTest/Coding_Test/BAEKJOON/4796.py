# 풀이시간 8분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 단순히 전체에서 연속된 날짜를 나누고 그 나눈 값에 사용일을 곱하고 나머지 날짜를 더해주면 되는 문제이다.

tc=0
while True:
  tc+=1
  l,p,v=map(int,input().split())
  if l==0 and p==0 and v==0:
    break
  if v%p>l:
    k=l
  else:
    k=v%p
  print("Case "+str(tc)+": "+str(v//p*l+k))
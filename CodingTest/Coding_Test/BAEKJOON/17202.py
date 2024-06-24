# 풀이시간 10분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 문자열을 앞에서부터 차례대로 줄여가면서 저장해나가면 된다.

a=input()
b=input()

new_str=""
for i in range(len(a)):
  new_str+=(a[i]+b[i])

while True:
  if len(new_str)==2:
    print(new_str)
    break
  s=""
  for i in range(0,len(new_str)-1):
    s+=str(int(new_str[i])+int(new_str[i+1]))[-1]
  new_str=s
  # print(new_str)

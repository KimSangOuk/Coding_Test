# 풀이시간 8분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 사람의 수랑 컵홀더의 수중 작은 수를 출력하면 되는 문제이다. 컵홀더의 수 같은 경우는 문자열을 앞에서 부터 탐색하며 'S'일 때와 'L'일 때의 인덱스를 조정하면서 세어가면 된다.

n=int(input())

s=input()
count=1
index=0
while True:
  if index==n:
    break
  if s[index]=='S':
    index+=1
  else:
    index+=2

  count+=1

print(min(count,n))
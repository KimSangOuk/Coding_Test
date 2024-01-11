# 풀이시간 7분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 단순하게 가장 큰 상태일 떄의 a와 b, 가장 작은 상태일 때의 a,b를 구해서 각자를 더해주면 되는 문제이다.

a,b=map(int,input().split())

min_a=""
min_b=""
max_a=""
max_b=""
for i in range(len(str(a))):
  if str(a)[i]=='6':
    min_a+="5"
    max_a+='6'
  elif str(a)[i]=='5':
    max_a+='6'
    min_a+='5'
  else:
    min_a+=str(a)[i]
    max_a+=str(a)[i]

for i in range(len(str(b))):
  if str(b)[i]=='6':
    min_b+="5"
    max_b+='6'
  elif str(b)[i]=='5':
    max_b+='6'
    min_b+='5'
  else:
    min_b+=str(b)[i]
    max_b+=str(b)[i]

print(int(min_a)+int(min_b),int(max_a)+int(max_b))
# 풀이시간 2시간 시간제한 2초 메모리제한 256MB
# 1회차 정답 - 시간이 너무 오래 걸려서 다시 한번 풀어보기
# 각 알파벳의 위치와 갯수에 따른 가치에 따라 알파벳에 숫자를 부여하고 그 부여한 숫자로 답을 구해내는 문제이다. 그렇기 때문에 가치가 큰 순서대로 숫자를 부여한다는 뜻에서 그리디라고 할 수 있다.

n=int(input())
array=[]
digit=[dict() for _ in range(26)]
# 각 알파벳을 자리수에 몇개씩 있는지 파악
for _ in range(n):
  s=input()
  array.append(s)
  for i in range(len(s)):
    if 8-(len(s)-i) not in digit[int(ord(s[i])-ord('A'))]:
      digit[int(ord(s[i])-ord('A'))][8-(len(s)-i)]=1
    else:
      digit[int(ord(s[i])-ord('A'))][8-(len(s)-i)]+=1

# 그 자리수를 고려해서 그 수의 크기 가치 파악
start=9
match=dict()
rank=[]
for i in range(26):
  if len(digit[i])>0:
    tmp=0
    for j in range(0,8):
      if j in digit[i]:
        tmp+=(digit[i][j])*(10**(7-j))
    rank.append((int(tmp),i))

# 그 크기가치를 기준으로 알파벳을 정렬
rank.sort(reverse=True)

# 정렬된 크기가치에 따라 숫자에 알파벳 부여
start=9
for r in range(len(rank)):
  if rank[r][1] not in match:
    match[rank[r][1]]=start
    start-=1      

# 알파벳과 숫자를 매칭하여 합의 값을 구해냄
answer=[]
for i in range(n):
  s_to_int=""
  for j in range(len(array[i])):
    s_to_int+=str(match[ord(array[i][j])-ord('A')])
  answer.append(int(s_to_int))

print(sum(answer))

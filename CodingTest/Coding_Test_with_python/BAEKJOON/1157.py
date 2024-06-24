# 풀이시간 10분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 각 문자를 대문자로 변경해서 숫자를 세고 그 숫자가 가장 많은 문자를 답으로 저장해나가면 되는 문제이다. 그 답이 2개 이상이면 ?를 아니면 답을 그대로 출력하면 된다.

s=input()
count=[0]*(ord('Z')-ord('A')+1)

for i in s.upper():
    count[ord(i)-ord('A')]+=1

max_value=-1
answer=[]
for i in range(0,ord('Z')-ord('A')+1):
    if count[i]>max_value:
        max_value=count[i]
        answer=[]
        answer.append(chr(ord('A')+i))
    elif count[i]==max_value:
        answer.append(chr(ord('A')+i))

if len(answer)>1:
    print('?')
else:
    print(*answer)
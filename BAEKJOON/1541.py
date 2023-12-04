# 풀이시간 30분 시간초과 2초 메모리제한 128MB
# 1회차 정답
# 시간과 입력조건을 보았을 때, 딱히 다중문이 너무 많이만 아니면 적당한 정도인 알고리즘으로 쓰면 될 것 같았다.
# 예제의 식들을 분석해 보았을 때, '-'가 한번 나타난 이후부터는 쭉 다 수를 빼주면 된다는 것을 깨달았다.
# 현시점에서 빼냐 더하냐만 알면되기 때문에 '-'가 나타난 시점만 캐치하면 되는 그리디 알고리즘이다.

s=input()
num=""
mode=False
result=0
for i in range(len(s)):
  if s[i].isdigit():
    num+=s[i]

  if i==len(s)-1 or s[i]=='-' or s[i]=='+':
    if mode==True:
      result-=int(num)
    else:
      result+=int(num)
    num=""

  if s[i]=='-':
    mode=True

print(result)
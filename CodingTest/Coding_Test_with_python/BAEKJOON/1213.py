# 각 알파벳을 세어서 팬린드롬을 순서대로 넣고 홀수인 알파벳이 여러개이면 팬린드롬이 불가능하다고 출력하는 식으로 접근하였다. 먼저 알파벳의 각 갯수를 세고 팬린드롬 가능 여부부터 판단하였다. 다음 팬린드롬 중 가장 알파벳 순으로 빠른 팬린드롬을 출력하는 것이기 때문에 알파벳을 하나씩 갯수의 반씩 붙여서 팬린드롬의 앞부분을 만들고 홀수인 알파벳이 존재할 경우 중간에 하나 붙여주었다.
# 풀이시간 : 25분

s=list(input())
s.sort()
arr=[0]*26
for i in range(len(s)):
    arr[ord(s[i])-ord('A')]+=1
cnt=0
one_s_index=-1
for i in range(26):
    if arr[i]%2!=0:
        one_s_index=i
        cnt+=1
front_s=''
for i in range(26):
    front_s+=chr(ord('A')+i)*(arr[i]//2)

if one_s_index!=-1:
    answer=front_s+chr(ord('A')+one_s_index)+front_s[::-1]
else:
    answer=front_s+front_s[::-1]

if cnt>1:
    print("I'm Sorry Hansoo")
else:
    print(answer)
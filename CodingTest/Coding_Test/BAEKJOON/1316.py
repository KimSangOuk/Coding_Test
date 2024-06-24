# - 바뀌는 순간만 고려해서 바뀌고 난 철자가 현재 내가 지금까지 확인안된 철자라면 추가하고 확인된 철자라면 그룹 단어가 아니게 된다. 또한 바뀌기 전 철자는 확인을 확인하는 집합에 넣어서 후에 확인이 가능하게 한다.
# - 풀이시간 : 10분

n=int(input())
answer=0
for i in range(n):
    s=input()
    ischecked=set()
    group_word_check=True
    for j in range(0,len(s)-1):
        if s[j]!=s[j+1]:
            ischecked.add(s[j])
            if s[j+1] in ischecked:
                group_word_check=False
                break
    if group_word_check:
        answer+=1
print(answer)
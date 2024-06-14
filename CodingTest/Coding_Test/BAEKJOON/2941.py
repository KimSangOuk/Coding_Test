# - set()에 크로아티아 알파벳으로 변환될 수 있는 모든 경우의 수를 넣어놓고 문자의 인덱스를 앞에서 뒤로 각 변환되는 문자열 길이 만큼 앞으로 가게 하면서 변환될 때마다 갯수에 +1을 해주면 된다. 해당이 되지 않는 알파벳은 +1 처리해주면 된다.
# - 풀이 시간 : 5분

cro_alpha=set(['c=','c-','dz=','d-','lj','nj','s=','z='])
s=input()
index=0
answer=0
while index<len(s):
    if s[index:index+1] in cro_alpha:
        answer+=1
        index+=1
    elif s[index:index+2] in cro_alpha:
        answer+=1
        index+=2
    elif s[index:index+3] in cro_alpha:
        answer+=1
        index+=3
    else:
        answer+=1
        index+=1
print(answer)
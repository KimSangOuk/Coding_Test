# - 처음에는 .과 'X'모두 세면서 더하려고 하다가 글자가 하나일 때도 있고 변환될 때랑 끝날 때랑 조건이 너무 까다로워 져서 그냥 50자 이길래 X만 세고 X자리 수에 따라 바꿔넣기로 전략을 바꾸었다.
# - X자리를 앞에서부터 확인하면서 갯수를 파악하고 4개 이상이면 A를 넣고 나머지 2자리가 남으면 B를 넣는식으로 하였다. 그 이외의 경우는 불가능하기 때문에 -1을 출력하기 위해 따로 변수를 두어 처리하였다.
# - 풀이시간 : 30분

s=list(input())
cnt=0
start_index=-1
possible=True
prev=''
answer=''
for i in range(len(s)):
    if s[i]=='X' and start_index==-1:
        start_index=i
        cnt+=1
    elif start_index!=-1 and (i==len(s)-1 or s[i+1]=='.') and s[i]=='X':
        cnt+=1
        a_cnt,b_cnt=0,0
        if cnt>=4 and cnt%2==0:
            a_cnt=cnt//4*4
            b_cnt=cnt-a_cnt
        elif cnt<4 and cnt%2==0:
            b_cnt=2
        else:
            possible=False
            break
        for j in range(start_index,start_index+a_cnt):
            s[j]='A'
        for j in range(start_index+a_cnt,start_index+a_cnt+b_cnt):
            s[j]='B'
        cnt=0
        start_index=-1
    elif start_index!=-1 and s[i]=='X':
        cnt+=1

if 'X' in s:
    possible=False

if possible:
    print(''.join(s))
else:
    print(-1)
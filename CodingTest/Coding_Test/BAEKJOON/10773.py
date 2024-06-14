# - 처음에는 문자열로 접근했다가 2자리가 넘어가면 문자열의 길이를 따로 기록해야되서 배열에 숫자를 넣기로 하였다. 0일 경우 빼고 0이 아닐 경우 넣은다음 총 합을 구하면 된다.
# - 풀이시간 : 10분

n=int(input())
input_s=[]
for i in range(n):
    k=int(input())
    if k!=0:
        input_s.append(k)
    else:
        input_s.pop()
print(sum(input_s))
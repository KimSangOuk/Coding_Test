# - 각 1~30까지의 모든 번호를 set()에 넣어놓고 호명대는 되로 지워서 남는 2명을 정렬해서 출력하였다.
# - 풀이시간 : 3분

num_list=set([i for i in range(1,31)])

for i in range(28):
    num_list.remove(int(input()))
num_list=list(num_list)
num_list.sort()
for i in range(2):
    print(num_list[i])
# - 아침밥을 안먹었더니 머리가 안돌아간다...
# - 전체 배열에서 k만큼 인덱스를 늘리며 진행을 하되 없어지는 원소를 고려해서 전체 길이와 인덱스를 한칸 앞으로 조절해주어야 한다. 배열을 넘어가는 인덱스의 경우는 나머지 연산을 통해 전체 길이 내로 조절을 해준다.
# - 마지막 출력할 때, 배열에 str을 붙인다고 그대로 문자로 바뀌는건 처음 알았다...
# - 풀이시간 : 30분

n,k=map(int,input().split())
arr=[i for i in range(1,n+1)]
start=-1
answer=[]
while len(arr)>0:
    start+=k
    start=start%n
    answer.append(arr[start])
    arr.pop(start)
    n-=1
    start-=1

print("<"+str(answer)[1:-1]+">")
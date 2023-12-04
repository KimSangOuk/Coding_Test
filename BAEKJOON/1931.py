# 풀이시간 16분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 일단 N이 100,000 이하이기 때문에 최대 O(nlogn) 시간복잡도를 이용하는 알고리즘 사용
# 딱 예시를 보았을 때, 정렬을 사용해야될꺼 같은데 현시점에 다음 회의를 바로 찾고 싶음. 여기서 그리디 알고리즘을 적용할 수 있겠구나 느꼈고, 바로 다음 회의의 조건은 바로 끝시점이 최대한 빠른 회의를 많이 넣으면 된다. 이러면 최대 갯수를 구할 수 있겠구나 느껴서 정렬해보고 넣어보니 바로 맞아떨어짐.

n=int(input())
arr=[]
for _ in range(n):
  start,end=map(int,input().split())
  arr.append((start,end))

arr.sort(key=lambda x:(x[1],x[0]))

end=arr[0][1]
count=1

for i in range(1,len(arr)):
  if arr[i][0]<end:
    continue
  else:
    end=arr[i][1]
    count+=1

print(count)
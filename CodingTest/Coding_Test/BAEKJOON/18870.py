# 풀이시간 10분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 각 수 마다 중복을 없애고 순서대로 인덱스를 달면 그 앞에 있는 수의 갯수와 같기 때문에, dict형태로 저장해 둔 다음, 원래 있던 배열에 그 번호를 적용시켜 출력하면 된다.

n=int(input())

array=list(map(int,input().split()))
set_arr=list(set(array))
set_arr.sort()
count_dict=dict()
for i in range(len(set_arr)):
  count_dict[set_arr[i]]=i

for i in array:
  print(count_dict[i],end=' ')
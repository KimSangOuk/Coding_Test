# 풀이시간 75분/60 시간제한 2초 메모리제한 128MB
# 1회차 정답 - 풀이시간 60분 내로 줄일 수 있지 않을까 해서 한번 더 풀어보기
# 문제를 처음 접근하면서 사람 수가 목표점이 될만 하기 때문에 각 놀이기구를 타면서 사람수를 구할만한 조건들을 살펴보았다. 이 때, 각 놀이기구가 타는 시간이 있기 때문에 일정시간당 놀이기구가 몇 회씩 돌아가는지 구할 수 있었고, 그 돌아간 횟수는 즉, 인원수를 나타낼 수 있을 거라는 생각이 들었다. 그렇기 때문에 특정시간일 때, 놀이기구의 걸리는 시간으로 나누어보았고, 이 때 나눴을 때, 특정 놀이기구를 탄 인원수가 몫으로 나오고 타기 이미 시작한 인원이 있을 경우에는 나머지가 나온다는 결론에 도달하였다. 그렇기 때문에, 범위를 시간이 될 수 있는 범위인 0부터 한 놀이기구를 최대 운행 시간 30*최대 인원 수로 해놓고 특정시간마다 놀이기구를 탄 인원을 구해서 전체 인원보다 적을 경우, 즉, 완전히 모든 인원이 탄 경우에는 어떤 순서로 탔는지 모르기 때문에 모든 인원보다 작아지는 최대 경우를 구해서 답으로 저장했고, 이때, 나누어 떨어지는 놀이기구는 바로 인원들이 탈 수 있는 비어있는 기구이므로 저장해두었다. 그리고 답으로 전체 인원에서 현재까지 탄 인원을 빼고 남은 인원 중 놀이기구를 빠른 순서부터 탄다고 생각하고 그 번째에 있는 놀이기구의 번호를 출력하면 된다.

import copy

n,m=map(int,input().split())
ride_times=list(map(int,input().split()))

def binary_search(ride_times,child,start,end):
  left_num=0
  left_rides=[]
  while start<=end:
    mid=(start+end)//2
    arr=[]
    num=0
    for i in range(len(ride_times)):
      num+=mid//ride_times[i]
      if mid%ride_times[i]>0:
        num+=1
      elif mid%ride_times[i]==0:
        arr.append(i+1)
    if num<child:
      left_rides=copy.deepcopy(arr)
      left_num=child-num
      start=mid+1
    else:
      end=mid-1
  return left_rides[left_num-1]

print(binary_search(ride_times,n,0,30*int(2e9)))
    
      
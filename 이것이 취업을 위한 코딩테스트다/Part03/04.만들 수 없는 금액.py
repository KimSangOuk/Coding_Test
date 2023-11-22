# 풀이 시간 - 40분/30분 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 시간이 초과했고 더 효율적인 알고리즘이 존재함
# 일단 그리디 풀면서 정렬 후 앞에서부터 원하는 숫자가 아니라 하나씩 비교하면서 맞춰나가서 그리디구나 싶었지만 더 그리디 스러운 방법 궁극의 목표 수치를 두고 하는 방법을 찾음. 한가지 깨달음.
# 화폐 단위가 1,000,000 이하길래 일단 O(N^2)이하의 방법을 쓰면 된다고 생각함
# 굳이 하나씩 화폐를 훑으면서 찾지 않아도 목표 수치를 업데이트 시키며 원하는 것만 추구하는 것도 한가지 그리디스러운 방법인 것을 각인함.

# 2회차 풀이


# 1회차 풀이
n=int(input())
arr=list(map(int,input().split()))

arr.sort()

can_num=0 # 목표 수치로 두고
for i in range(0,len(arr)-1):
  if arr[i]+can_num>=arr[i+1]: # 여기서는 만들 수 없는 상한선을 보는거고, 그냥 더 만들 수 있는 숫자랑 비교하는게 효율적
    can_num=arr[i]+can_num
  else:
    if can_num!=0: # 목표 수치로 안두니까 한번 더 비교가 되는거임
      can_num=arr[i]+can_num
    break

print(can_num+1)

# 답안지
# n=int(input())
# arr=list(map(int,input().split()))

# arr.sort()

# target=1 # 우리가 만들 숫자 - 바로 ㅈㄴ 그리디해
# for i in arr:
#   if target<i: # 우리가 만들 숫자보다 i가 크면 못만들면 브레이크 작거나 같으면 다음목표 전진가능
#     break
#   target+=i
# # 결국 target-1까지는 만들 수 있으니 target을 목표로 하는거다
# print(target)
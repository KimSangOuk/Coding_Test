# 풀이시간 초과/60분 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 시간 초과 및 풀이방법에 접근하지 못함
# 각 높이 구간 별로 갯수를 구하고 이를 이요해야 한다는 것도 알고 있었고, 각 석순과 종유석을 정렬하면 갯수를 구하는데 유리하지 않을까라는 생각도 했지만 결국 각 구간에서 모든 종유석을 지나가는 완전탐색말고는 갯수를 구할 아이디어를 얻지 못했다. 왜 갯수를 구할 아이디어, 즉 정렬 했을 때, 각 구간의 시작 이후가 앞으로 부딪치는 갯수가 된다고 생각하지 못했는가? 먼저 이진탐색을 각자 수행할 생각을 하지 못했다. 왜 각자 수행할 생각을 하지 못했는가? 종유석과 석순의 구간별 부딪치는 갯수의 합이 전체 부딪치는 갯수의 합이지만, 한 구간에서 두개의 모든 것이 나타나기 때문에 나눌 수 없다고 생각했다. 하나의 2차원 배열이라고 생각했고, 종류나 필요에 따라 나누면 안된다고 1차적인 생각을 가지고 있었던 거 같다. 나눠서 합칠 생각을 하지 못했다. 왜? 묶어서 하나로 보는 습관이 있어서 종류가 다르다면 나누어서 해를 구한다음 합친다는 아이디어를 가지고 있었어야 했다.

n,h=map(int,input().split())

array=[]
for _ in range(n):
  array.append(int(input()))

def binary_search(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    count=0
    for i in range(0,len(array)):
      if array[i]%2==0:
        if mid<array[i]:
          count+=1
      else:
        if h-array[i]>mid:
          count+=1
    print(count,target,mid)
    if count<=target:
      target=min(count,target)
      result=mid
      end=mid-1
    else:
      start=mid+1
  return result

print(binary_search(array,n,0,n))

n, h = map(int, input().split())

down = []
up = []
for i in range(n):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))

down.sort()
up.sort()

min_count = n
range_count = 0

# 답안지
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


for i in range(1, h + 1):
    down_count = len(down) - binary_search(down, i - 0.5, 0, len(down) - 1)
    top_count = len(up) - binary_search(up, h - i + 0.5, 0, len(up) - 1)

    if min_count == down_count + top_count:
        range_count += 1
    elif min_count > down_count + top_count: # 현재 범위가 새로운 최소 값이면
        range_count = 1
        min_count = down_count + top_count

print(min_count, range_count)
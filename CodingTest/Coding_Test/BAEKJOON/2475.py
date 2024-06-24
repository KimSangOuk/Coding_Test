arr=list(input().split())
total=0
for i in range(len(arr)):
    total+=int(arr[i])*int(arr[i])
print(total%10)
# 각 수를 배열로 받아서 제곱한 수의 합을 구한 후, 10으로 나눈 나머지를 출력한다.
# 풀이시간 : 3분
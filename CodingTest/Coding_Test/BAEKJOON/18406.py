# 이것이 취업을 위한 코딩테스트다 part03 '07. 럭키 스트레이트'와 동일

left_sum=0
right_sum=0

num=input()
length=len(num)
half=length//2
for i in range(0,half):
  left_sum+=int(num[i])

for i in range(half,length):
  right_sum+=int(num[i])

if left_sum==right_sum:
  print("LUCKY")
else:
  print("READY")
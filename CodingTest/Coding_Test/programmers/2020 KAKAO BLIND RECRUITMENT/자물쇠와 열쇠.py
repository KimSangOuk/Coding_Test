# 이것이 취업을 위한 코딩테스트다 part03 '10. 문자열 압축'과 동일

def check_all(lock,lock_size,key_size):
  for i in range(key_size-1,key_size+lock_size-1):
    for j in range(key_size-1,key_size+lock_size-1):
      if lock[i][j]!=1:
        return False

  return True

def rotate_key(key):
  key_size=len(key)
  new_key=[[0]*key_size for i in range(key_size)]

  for i in range(key_size):
    for j in range(key_size):
      new_key[j][key_size-1-i]=key[i][j]
  return new_key

def solution(key, lock):
  answer = True

  key_size=len(key)
  lock_size=len(lock)
  new_lock=[[0]*(lock_size+(key_size)*2-2) for i in range(lock_size+key_size*2-2)]

  for i in range(key_size-1,key_size-1+lock_size):
    for j in range(key_size-1,key_size-1+lock_size):
      new_lock[i][j]=lock[i-key_size+1][j-key_size+1]

  for _ in range(4):
    key=rotate_key(key)

    for j in range(0,key_size+lock_size-1):
      for k in range(0,key_size+lock_size-1):
        for a in range(key_size):
          for b in range(key_size):
            new_lock[j+a][k+b]+=key[a][b]

        # for c in range(len(new_lock)):
        #   for d in range(len(new_lock)):
        #     print(new_lock[c][d],end=" ")
        #   print()

        if check_all(new_lock,lock_size,key_size):
          return True

        for a in range(key_size):
          for b in range(key_size):
            new_lock[j+a][k+b]-=key[a][b]


  return False
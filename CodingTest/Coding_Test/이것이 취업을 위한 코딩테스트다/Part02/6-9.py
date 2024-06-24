array=[('바나나',2),('사과',5),('당근',3)]

def sorting(data):
  return data[1]

result=sorted(array,key=sorting)
print(result)
{ pkgs }: {
  deps = [
    pkgs.n,k=map(int,input().split())graph=[]for i in range(n):  graph.append(list(map(int,sys.stdin.readline().split())))queue=deque()new_arr=[]for i in range(n):  for j in range(n):    if graph[i][j]!=0:      new_arr.append((graph[i][j],i,j))queue.append(new_arr)s,x_a,y_a=map(int,sys.stdin.readline().split())dx=[0,-1,0,1]dy=[-1,0,1,0]for ms in range(s):  arr=queue.popleft()  new_arr=[]  for d,x,y in arr:    for i in range(4):      nx=x+dx[i]      ny=y+dy[i]      if nx>=0 and nx<n and ny>=0 and ny<n and graph[nx][ny]==0:        graph[nx][ny]=d        new_arr.append((d,nx,ny))  new_arr.sort()  queue.append(new_arr)  # for i in range(n):  #   print(graph[i])print(graph[x_a-1][y_a-1])
  ];
}
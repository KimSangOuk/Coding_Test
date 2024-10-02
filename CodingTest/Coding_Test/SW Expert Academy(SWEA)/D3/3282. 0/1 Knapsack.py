def knapsack(k,wt,val,n):
  global dp
  for i in range(n+1):
      for j in range(k+1):
          if i==0 or j==0:
              dp[i][j]=0
          elif wt[i-1]<=j:
              dp[i][j]=max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
          else:
              dp[i][j]=dp[i-1][j]
  return dp[n][k]

for tc in range(1,int(input())+1):
  n,k=map(int,input().split())
  wt=[]
  val=[]
  for i in range(n):
      w,v=map(int,input().split())
      wt.append(w)
      val.append(v)
  dp=[[0]*(k+1) for _ in range(n+1)]
  print("#"+str(tc)+" "+str(knapsack(k,wt,val,n)))

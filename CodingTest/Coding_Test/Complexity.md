시간복잡도
ex)
N=1,000,000,000 / O(logN)
N=10,000,000 / O(N)
N=100,000 / O(NlogN)
N=2,000 / O(N^2)
N=500 / O(N^3)

공간복잡도
int a[1000]=4KB
int a[1000000]=4MB
int a[1000][1000]=16MB
1,000만 단위 넘어가지 않도록 주의

시간 측정
import time
time.time()
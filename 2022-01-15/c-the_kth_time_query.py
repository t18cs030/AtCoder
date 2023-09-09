N,Q = map(int,input().split())
A = list(map(int, input().split()))
d={}

for i in range(N):
    d.setdefault(A[i],[]).append(i+1)

for i in range(Q):
    x,k=(map(int, input().split()))
    if x not in d or len(d[x])<k:
        print(-1)
    else:
        print(d[x][k-1])


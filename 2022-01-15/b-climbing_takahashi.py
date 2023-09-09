N = int(input())
stages = list(map(int, input().split()))

takahashi = stages[0]
for i in range(N):
    if i == N-1:
        break
    if stages[i] < stages[i+1]:
        takahashi = stages[i+1]
    else:
        break

print(takahashi)
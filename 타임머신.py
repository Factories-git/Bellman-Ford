import sys

input = sys.stdin.readline
n,m = map(int, input().split())
edges = []
distance = [float('inf')] * (n+1)

for i in range(m):
    s,e,t = map(int, input().split())
    edges.append([s,e,t])

distance[1] = 0

for i in range(n-1):
    for s,e,t in edges:
        if distance[s] != float('inf') and distance[e] > distance[s] + t:
            distance[e] = distance[s] + t

mCycle = False

for s,e,t in edges:
    if distance[s] != float('inf') and distance[e] > distance[s] + t:
        mCycle = True

if not mCycle:
    for i in range(2, n+1):
        if distance[i] != float('inf'):
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)
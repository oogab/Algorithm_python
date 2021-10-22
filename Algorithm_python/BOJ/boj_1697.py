from collections import deque

dist = [-1]*100001

n, k = map(int, input().split())
q = deque()

q.append(n)
dist[n] = 0

while q:
    s = q.popleft()
    if s == k:
        break
    
    n1 = s-1
    if n1 >= 0:
        if dist[n1] == -1:
            q.append(n1)
            dist[n1] = dist[s]+1

    n2 = s+1
    if n2 <= 100000:
        if dist[n2] == -1:
            q.append(n2)
            dist[n2] = dist[s]+1

    n3 = s*2
    if n3 <= 100000:
        if dist[n3] == -1:
            q.append(n3)
            dist[n3] = dist[s]+1

print(dist[k])
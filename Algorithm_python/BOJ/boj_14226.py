from collections import deque

d = int(input())

s, c = 1, 0
q = deque()
dist = [[0 for _ in range(1001)] for _ in range(1001)]

q.append((s, c))

while q:
    os, oc = q.popleft()
    if os == d:
        break

    ns1, nc1 = os-1, oc
    if ns1 < 0:
        continue
    if dist[ns1][nc1] == 0:
        q.append((ns1, nc1))
        dist[ns1][nc1] = dist[os][oc]+1

    ns2, nc2 = os, os
    if dist[ns2][nc2] == 0:
        q.append((ns2, nc2))
        dist[ns2][nc2] = dist[os][oc]+1

    if oc != 0:
        ns3, nc3 = os+oc, oc
        if ns3 > 1000:
            continue
        if dist[ns3][nc3] == 0:
            q.append((ns3, nc3))
            dist[ns3][nc3] = dist[os][oc]+1

print(dist[os][oc])
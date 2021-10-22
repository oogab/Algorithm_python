from collections import deque
from functools import reduce

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = tuple(map(int,input().split()))
a = [list(map(int,input().split())) for _ in range(n)]
check = [[False]*m for _ in range(n)]
d = [[-1]*m for _ in range(n)]
noz = True

q = deque()

for i in range(n):
	for j in range(m):
		if a[i][j] == 1:
			q.append((i, j))
			check[i][j] = True
			d[i][j] = 0
		elif a[i][j] == 0:
			noz = False

if noz:
	print(0)
else:
	while q:
		x, y = q.popleft()
		for k in range(4):
			nx, ny = x+dx[k], y+dy[k]
			if 0 <= nx < n and 0 <= ny < m:
				if a[nx][ny] == 0 and check[nx][ny] == False:
					q.append((nx, ny))
					check[nx][ny] = True
					d[nx][ny] = d[x][y] + 1

	ans = max([max(row) for row in d])
	for i in range(n):
		for j in range(m):
			if a[i][j] == 0 and d[i][j] == -1:
				ans = -1
	
	print(ans)
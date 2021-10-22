from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    check[i][j] = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1 and check[nx][ny] == 0:
                    q.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1

n, m = tuple(map(int, input().split(' ')))
a = [list(map(int,input())) for _ in range(n)]
check = [[0]*m for _ in range(n)]

bfs(0, 0)
print(check[n-1][m-1])
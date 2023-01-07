from collections import deque
import sys; input = sys.stdin.readline

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    q = deque()
    q.append([sz,sy,sx])
    vis[sz][sy][sx] = 1

    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c and vis[nz][ny][nx] == 0:
                if board[nz][ny][nx] == "." or board[nz][ny][nx] == "E":
                    dp[nz][ny][nx] = dp[z][y][x] + 1
                    vis[nz][ny][nx] = 1
                    q.append([nz,ny,nx])


while True:
    l, r, c = map(int, input().split())
    if l == 0:
        break

    board = [[] * r for i in range(l)]
    vis = [[[0] * c for i in range(r)] for i in range(l)]
    dp = [[[0] * c for i in range(r)] for i in range(l)]

    for i in range(l):
        for j in range(r):
            board[i].append(list(map(str, input().strip())))
        # 층으로 입력받기 때문에 개행 처리
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if board[i][j][k] == "S":
                    # 행 열 층
                    sx, sy, sz = k, j, i
                elif board[i][j][k] == "E":
                    ex, ey, ez = k, j, i

    bfs()

    if dp[ez][ey][ex] == 0:
        print("Trapped!")
    else:
        print(f"Escaped in {dp[ez][ey][ex]} minute(s).")

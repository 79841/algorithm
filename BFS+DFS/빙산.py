import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

iceberg = [list(map(int, input().split())) for _ in range(N)]

def melt_iceberg(iceberg):
    melting_iceberg = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    iceberg_count = 0
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0 and visited[i][j] == 0:
                deq = deque()
                iceberg_count += 1
                if iceberg_count > 1:
                    return iceberg_count, melting_iceberg
                deq.append([i, j])
                visited.append([i, j])
                while deq:
                    y, x = deq.pop()
                    visited[y][x] = 1

                    dy = [1, -1, 0, 0]
                    dx = [0, 0, 1, -1]
                    melting_count = 0

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if not (nx > -1 and nx < M and ny > -1 and ny < N):
                            continue
                        
                        if iceberg[ny][nx] == 0:
                            melting_count += 1
                        if iceberg[ny][nx] > 0 and visited[ny][nx] == 0:
                            deq.append([ny, nx])
                    if iceberg[y][x] - melting_count > 0:
                        melting_iceberg[y][x] = iceberg[y][x] - melting_count
                    else:
                        melting_iceberg[y][x] = 0
    return iceberg_count, melting_iceberg


years = -1
possible = False
while True:
    count, iceberg = melt_iceberg(iceberg)

    years += 1
    if count > 1:
        print(years)
        break
    elif count < 1:
        print(0)
        break



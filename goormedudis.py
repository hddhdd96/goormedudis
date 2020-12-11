#https://level.goorm.io/exam/43082/%EC%B5%9C%EB%8B%A8-%EA%B1%B0%EB%A6%AC-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

import sys

N = int(sys.stdin.readline())

n_list = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

next_pos = [[0, 0]]

while next_pos:
    x, y = next_pos.pop(0)
    value = n_list[x][y]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N:
            continue

        new_value = n_list[new_x][new_y]

        if new_value != 1:
            continue

        if new_value == 1 or value + 1 < new_value:
            n_list[new_x][new_y] = value + 1
            next_pos.append([new_x, new_y])

print(n_list[N - 1][N - 1])
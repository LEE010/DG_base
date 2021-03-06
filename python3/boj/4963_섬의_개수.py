'''
섬의 개수 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	30971	15515	11149	49.173%
문제
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.



한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

예제 입력 1 
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
예제 출력 1 
0
1
1
3
1
9
출처
ICPC > Regionals > Asia Pacific > Japan > Japan Domestic Contest > 2009 Japan Domestic Contest B번

문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: j4bez
링크
TJU Online Judge
'''
from sys import stdin
readline = stdin.readline

OFFSET = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def search(board, i, j, visited):
    q = [(i, j)]

    while q:
        ci, cj = q.pop(0)

        for wi, wj in OFFSET:
            ni, nj = ci+wi, cj+wj
            if 0 <= ni < H and 0 <= nj < W and board[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))


while True:
    W, H = map(int, readline().split())

    if W == 0 and H == 0:
        break

    board = [list(map(int, readline().split())) for _ in range(H)]
    visited = [[False for _ in range(W)] for _ in range(H)]
    cnt = 0

    for i in range(H):
        for j in range(W):
            if not visited[i][j] and board[i][j]:
                cnt += 1
                visited[i][j] = True
                search(board, i, j, visited)
    print(cnt)

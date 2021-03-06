'''
2048 (Easy) 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	40087	10481	5877	23.919%
문제
2048 게임은 4×4 크기의 보드에서 혼자 즐기는 재미있는 게임이다. 이 링크를 누르면 게임을 해볼 수 있다.

이 게임에서 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다. 이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다. 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다. (실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)

		
<그림 1>	<그림 2>	<그림 3>
<그림 1>의 경우에서 위로 블록을 이동시키면 <그림 2>의 상태가 된다. 여기서, 왼쪽으로 블록을 이동시키면 <그림 3>의 상태가 된다.

			
<그림 4>	<그림 5>	<그림 6>	<그림 7>
<그림 4>의 상태에서 블록을 오른쪽으로 이동시키면 <그림 5>가 되고, 여기서 다시 위로 블록을 이동시키면 <그림 6>이 된다. 여기서 오른쪽으로 블록을 이동시켜 <그림 7>을 만들 수 있다.

	
<그림 8>	<그림 9>
<그림 8>의 상태에서 왼쪽으로 블록을 옮기면 어떻게 될까? 2가 충돌하기 때문에, 4로 합쳐지게 되고 <그림 9>의 상태가 된다.

			
<그림 10>	<그림 11>	<그림 12>	<그림 13>
<그림 10>에서 위로 블록을 이동시키면 <그림 11>의 상태가 된다. 

<그림 12>의 경우에 위로 블록을 이동시키면 <그림 13>의 상태가 되는데, 그 이유는 한 번의 이동에서 이미 합쳐진 블록은 또 합쳐질 수 없기 때문이다.

	
<그림 14>	<그림 15>
마지막으로, 똑같은 수가 세 개가 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다. 예를 들어, 위로 이동시키는 경우에는 위쪽에 있는 블록이 먼저 합쳐지게 된다. <그림 14>의 경우에 위로 이동하면 <그림 15>를 만든다.

이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다. 보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다. 0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다. 블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.

출력
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.

예제 입력 1 
3
2 2 2
4 4 4
8 8 8
예제 출력 1 
16
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: clrmt noorycode
문제의 오타를 찾은 사람: doju
'''
from sys import stdin
from itertools import chain
from copy import deepcopy

COUNT = 5
readline = stdin.readline


def shift_up(board, j):
    global SIZE

    for i in range(SIZE-1):
        if board[i][j] == 0:
            for k in range(i+1, SIZE):
                if board[k][j] != 0:
                    board[i][j] = board[k][j]
                    board[k][j] = 0
                    break
            else:
                break


def merge_up(board, j):
    global SIZE

    for i in range(SIZE-1):
        if board[i][j] != 0 and board[i][j] == board[i+1][j]:
            board[i][j] *= 2
            board[i+1][j] = 0


def up(board):
    global SIZE
    for j in range(SIZE):
        shift_up(board, j)
        merge_up(board, j)
        shift_up(board, j)


def shift_down(board, j):
    for i in range(SIZE-1, 0, -1):
        if board[i][j] == 0:
            for k in range(i-1, -1, -1):
                if board[k][j] != 0:
                    board[i][j] = board[k][j]
                    board[k][j] = 0
                    break
            else:
                break


def merge_down(board, j):
    global SIZE

    for i in range(SIZE-1, 0, -1):
        if board[i][j] != 0 and board[i][j] == board[i-1][j]:
            board[i][j] *= 2
            board[i-1][j] = 0


def down(board):
    global SIZE
    for j in range(SIZE):
        shift_down(board, j)
        merge_down(board, j)
        shift_down(board, j)


def shift_left(board, i):
    global SIZE
    for j in range(SIZE-1):
        if board[i][j] == 0:
            for k in range(j+1, SIZE):
                if board[i][k] != 0:
                    board[i][j] = board[i][k]
                    board[i][k] = 0
                    break
            else:
                break


def merge_left(board, i):
    global SIZE

    for j in range(SIZE-1):
        if board[i][j] != 0 and board[i][j] == board[i][j+1]:
            board[i][j] *= 2
            board[i][j+1] = 0


def left(board):
    global SIZE

    for i in range(SIZE):
        shift_left(board, i)
        merge_left(board, i)
        shift_left(board, i)


def shift_right(board, i):
    global SIZE
    for j in range(SIZE-1, 0, -1):
        if board[i][j] == 0:
            for k in range(j-1, -1, -1):
                if board[i][k] != 0:
                    board[i][j] = board[i][k]
                    board[i][k] = 0
                    break
            else:
                break


def merge_right(board, i):
    global SIZE

    for j in range(SIZE-1, 0, -1):
        if board[i][j] != 0 and board[i][j] == board[i][j-1]:
            board[i][j] *= 2
            board[i][j-1] = 0


def right(board):
    global SIZE

    for i in range(SIZE):
        shift_right(board, i)
        merge_right(board, i)
        shift_right(board, i)


def merge(board, cnt):
    if cnt == 0:
        print('*'*10)
        for b in board:
            print(' '.join(map(str, b)))
        print('*'*10)
        return max(chain(*board))

    offset = [up, down, left, right]
    cur_cnt = cnt - 1
    res = 0

    for pos in offset:
        copied_board = deepcopy(board)
        pos(copied_board)
        res = max(res, merge(copied_board, cur_cnt))
    return res


if __name__ == "__main__":
    global SIZE
    SIZE = int(readline())
    board = [list(map(int, readline().split())) for _ in range(SIZE)]
    result = merge(board, COUNT)
    print(result)

'''
test case
3
2 2 2
4 4 4 
8 8 8 

=> 16

3
2 2 2
2 2 2
2 2 2

=>8

10
16 16 8 32 32 0 0 8 8 8
16 0 0 0 0 8 0 0 0 16
0 0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

=>64

5
2 2 4 8 16
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
2 2 4 8 16

=>64

2
16 0 
0 0

=> 16



7
2 2 2 2 2 2 2
2 0 2 2 2 2 2
2 0 2 2 2 2 2
2 0 2 2 2 2 2
2 2 2 0 2 2 2 
2 2 2 2 2 2 0
2 2 2 2 2 2 0

=> 32



10
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0 
64 64 128 0 0 0 0 0 0 0
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0 
64 64 128 0 0 0 0 0 0 0
128 32 2 4 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0

=> 1024



20
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024
1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024 1024

=>32768


3
2 2 4
0 0 0
0 0 0

=> 8

2
8 16
16 8

=>16

4
8 16 0 0
0 0 16 8
0 0 0 0
0 0 0 0

=>32

4

0 0 0 0
4 0 0 0
8 32 4 0
8 8 4 0

->64

10
8 8 4 16 32 0 0 8 8 8
8 8 4 0 0 8 0 0 0 0
16 0 0 16 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 16
0 0 0 0 0 0 0 0 0 2

=>128

10
0 0 0 0 0 32 8 64 8 16
0 0 0 0 0 0 0 16 8 16
0 0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

=> 128

1
16

=> 16

2
8 16
16 8

=>16

4
2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2

=>32

'''

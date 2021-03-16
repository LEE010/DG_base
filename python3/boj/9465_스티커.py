'''
스티커 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	32820	16630	10877	48.967%
문제
상근이의 여동생 상냥이는 문방구에서 스티커 2n개를 구매했다. 스티커는 그림 (a)와 같이 2행 n열로 배치되어 있다. 상냥이는 스티커를 이용해 책상을 꾸미려고 한다.

상냥이가 구매한 스티커의 품질은 매우 좋지 않다. 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다. 즉, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.



모든 스티커를 붙일 수 없게된 상냥이는 각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내려고 한다. 먼저, 그림 (b)와 같이 각 스티커에 점수를 매겼다. 상냥이가 뗄 수 있는 스티커의 점수의 최댓값을 구하는 프로그램을 작성하시오. 즉, 2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합을 구해야 한다.

위의 그림의 경우에 점수가 50, 50, 100, 60인 스티커를 고르면, 점수는 260이 되고 이 것이 최대 점수이다. 가장 높은 점수를 가지는 두 스티커 (100과 70)은 변을 공유하기 때문에, 동시에 뗄 수 없다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 n (1 ≤ n ≤ 100,000)이 주어진다. 다음 두 줄에는 n개의 정수가 주어지며, 각 정수는 그 위치에 해당하는 스티커의 점수이다. 연속하는 두 정수 사이에는 빈 칸이 하나 있다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다. 

출력
각 테스트 케이스 마다, 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값을 출력한다.

예제 입력 1 
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
예제 출력 1 
260
290
출처
ICPC > Regionals > Asia Pacific > Korea > Asia Regional - Daejeon 2013 K번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: jh05013

'''

from sys import stdin

ROW = 2


def readline():
    return stdin.readline()


def dp(mem, i, j):
    if 0 <= i < len(mem) and 0 <= j < ROW:
        return mem[i][j]
    return 0


def solution(n, arrs):
    # dp(x,y) = max(
    #   dp(x-1, !y) + arr[x][y],
    #   dp(x-2, y) + arr[x][y],
    #   dp(x-2, !y) + arr[x][y],
    # )
    mem = [[0 for _ in range(ROW)] for _ in range(n)]

    for i in range(n):
        for j in range(ROW):
            mem[i][j] = arrs[j][i] + \
                max(dp(mem, i-1, not j), dp(mem, i-2, not j), dp(mem, i-2, j))

    return max(mem[-1])


if __name__ == "__main__":
    N = int(readline())

    for _ in range(N):
        n = int(readline())
        stickers = [list(map(int, readline().split())) for _ in range(ROW)]
        print(solution(n, stickers))

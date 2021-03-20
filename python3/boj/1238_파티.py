'''
파티 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	16739	7798	5123	44.939%
문제
N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.

어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다. 이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.

각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다. 하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.

이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다. N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X가 공백으로 구분되어 입력된다. 두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한 소요시간 Ti가 들어온다. 시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.

모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.

출력
첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력한다.

예제 입력 1 
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
예제 출력 1 
10
출처
Olympiad > USA Computing Olympiad > 2006-2007 Season > USACO February 2007 Contest > Silver 3번

문제를 번역한 사람: author6
빠진 조건을 찾은 사람: his130
링크
PKU Judge Online
TJU Online Judge

'''
from sys import stdin
from heapq import heappop, heappush


def readline(): return map(int, stdin.readline().split())


def search(graph, x):
    D = [float('inf') for _ in range(len(graph))]
    hq = [(0, x)]

    D[x] = 0

    while hq:
        cost, cur = heappop(hq)

        for nxt, nxt_cost in graph[cur]:
            total_cost = cost + nxt_cost

            if D[nxt] > total_cost:
                heappush(hq, (total_cost, nxt))
                D[nxt] = total_cost

    return D


if __name__ == '__main__':
    N, M, X = readline()

    forward_graph = [[] for _ in range(N+1)]
    backward_graph = [[] for _ in range(N+1)]

    for _ in range(M):
        s, e, t = readline()
        forward_graph[s].append((e, t))
        backward_graph[e].append((s, t))

    foward = search(forward_graph, X)
    backward = search(backward_graph, X)

    print(max(map(sum, zip(foward[1:], backward[1:]))))

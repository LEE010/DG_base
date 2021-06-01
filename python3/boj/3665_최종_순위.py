'''
최종 순위 출처다국어분류
 
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	5487	2074	1444	36.100%
문제
올해 ACM-ICPC 대전 인터넷 예선에는 총 n개의 팀이 참가했다. 팀은 1번부터 n번까지 번호가 매겨져 있다. 놀랍게도 올해 참가하는 팀은 작년에 참가했던 팀과 동일하다.

올해는 인터넷 예선 본부에서는 최종 순위를 발표하지 않기로 했다. 그 대신에 작년에 비해서 상대적인 순위가 바뀐 팀의 목록만 발표하려고 한다. (작년에는 순위를 발표했다) 예를 들어, 작년에 팀 13이 팀 6 보다 순위가 높았는데, 올해 팀 6이 팀 13보다 순위가 높다면, (6, 13)을 발표할 것이다.

창영이는 이 정보만을 가지고 올해 최종 순위를 만들어보려고 한다. 작년 순위와 상대적인 순위가 바뀐 모든 팀의 목록이 주어졌을 때, 올해 순위를 만드는 프로그램을 작성하시오. 하지만, 본부에서 발표한 정보를 가지고 확실한 올해 순위를 만들 수 없는 경우가 있을 수도 있고, 일관성이 없는 잘못된 정보일 수도 있다. 이 두 경우도 모두 찾아내야 한다.

입력
첫째 줄에는 테스트 케이스의 개수가 주어진다. 테스트 케이스는 100개를 넘지 않는다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

팀의 수 n을 포함하고 있는 한 줄. (2 ≤ n ≤ 500)
n개의 정수 ti를 포함하고 있는 한 줄. (1 ≤ ti ≤ n) ti는 작년에 i등을 한 팀의 번호이다. 1등이 가장 성적이 높은 팀이다. 모든 ti는 서로 다르다.
상대적인 등수가 바뀐 쌍의 수 m (0 ≤ m ≤ 25000)
두 정수 ai와 bi를 포함하고 있는 m줄. (1 ≤ ai < bi ≤ n) 상대적인 등수가 바뀐 두 팀이 주어진다. 같은 쌍이 여러 번 발표되는 경우는 없다.
출력
각 테스트 케이스에 대해서 다음을 출력한다.

n개의 정수를 한 줄에 출력한다. 출력하는 숫자는 올해 순위이며, 1등팀부터 순서대로 출력한다. 만약, 확실한 순위를 찾을 수 없다면 "?"를 출력한다. 데이터에 일관성이 없어서 순위를 정할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.
예제 입력 1 
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
예제 출력 1 
5 3 2 4 1
2 3 1
IMPOSSIBLE
출처


ICPC > Regionals > Europe > Northwestern European Regional Contest > NWERC 2010 E번

문제의 오타를 찾은 사람: anjupiter, mendou12, plzrun
문제를 번역한 사람: baekjoon
어색한 표현을 찾은 사람: zmtn94
'''
from sys import stdin
from collections import deque

readline = stdin.readline

T = int(readline())

for _ in range(T):
    N = int(readline())
    graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    indegree = [0 for _ in range(N + 1)]
    ranks = list(map(int, readline().split()))

    for i in range(N):
        for j in range(i + 1, N):
            graph[ranks[i]][ranks[j]] = True
            indegree[ranks[j]] += 1

    for _ in range(int(readline())):
        a, b = map(int, readline().split())

        if not graph[a][b]:
            a, b = b, a

        graph[a][b] = False
        graph[b][a] = True

        indegree[a] += 1
        indegree[b] -= 1

    res = []
    q = deque(i for i in range(1, N + 1) if not indegree[i])

    for n in range(N):
        if not q:
            print('IMPOSSIBLE')
            break
        if len(q) > 1:
            print('?')
            break

        cur = q.popleft()
        res.append(cur)

        for i in range(1, N + 1):
            if graph[cur][i]:
                indegree[i] -= 1
                if not indegree[i]:
                    q.append(i)
    else:
        print(*res)
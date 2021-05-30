'''
줄 세우기 스페셜 저지분류
 
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	21755	11939	7765	53.127%
문제
N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)이 주어진다. M은 키를 비교한 회수이다. 다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

학생들의 번호는 1번부터 N번이다.

출력
첫째 줄에 학생들을 키 순서대로 줄을 세운 결과를 출력한다. 답이 여러 가지인 경우에는 아무거나 출력한다.

예제 입력 1 
3 2
1 3
2 3
예제 출력 1 
1 2 3
예제 입력 2 
4 2
4 2
3 1
예제 출력 2 
4 2 3 1
출처
빠진 조건을 찾은 사람: indioindio
'''
from sys import stdin
from collections import deque

readline = stdin.readline

N, M = map(int, readline().split())
graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
res = []

for _ in range(M):
    a, b = map(int, readline().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque([i for i in range(1, N + 1) if indegree[i] == 0])

while q:
    v = q.popleft()
    res.append(v)

    for n in graph[v]:
        indegree[n] -= 1

        if indegree[n] == 0:
            q.append(n)

print(' '.join(map(str, res)))
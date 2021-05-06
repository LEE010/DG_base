'''
순회강연 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	3527	1181	908	34.869%
문제
한 저명한 학자에게 n(0 ≤ n ≤ 10,000)개의 대학에서 강연 요청을 해 왔다. 각 대학에서는 d(1 ≤ d ≤ 10,000)일 안에 와서 강연을 해 주면 p(1 ≤ p ≤ 10,000)만큼의 강연료를 지불하겠다고 알려왔다. 각 대학에서 제시하는 d와 p값은 서로 다를 수도 있다. 이 학자는 이를 바탕으로, 가장 많은 돈을 벌 수 있도록 순회강연을 하려 한다. 강연의 특성상, 이 학자는 하루에 최대 한 곳에서만 강연을 할 수 있다.

예를 들어 네 대학에서 제시한 p값이 각각 50, 10, 20, 30이고, d값이 차례로 2, 1, 2, 1 이라고 하자. 이럴 때에는 첫째 날에 4번 대학에서 강연을 하고, 둘째 날에 1번 대학에서 강연을 하면 80만큼의 돈을 벌 수 있다.

입력
첫째 줄에 정수 n이 주어진다. 다음 n개의 줄에는 각 대학에서 제시한 p값과 d값이 주어진다.

출력
첫째 줄에 최대로 벌 수 있는 돈을 출력한다.

예제 입력 1 
7
20 1
2 1
10 3
100 2
8 2
5 20
50 10

예제 출력 1 
185

---
3
1 1
10 2
10 2

20
---
5
20 1
2 1
10 3
100 2
8 2

130

출처
ICPC > Regionals > Europe > Southeastern European Regional Contest > SEERC 2003 D번

링크
ACM-ICPC Live Archive
PKU Judge Online
ZJU Online Judge
TJU Online Judge
'''
from sys import stdin
from heapq import heappop, heappush

readline = stdin.readline

N = int(readline())
pays = [[] for _ in range(10001)]

for _ in range(N):
    p, d = map(int, readline().split())
    pays[d].append(p)

hq = []
res = 0
for i in range(10000, 0, -1):
    for pay in pays[i]:
        heappush(hq, -pay)

    if hq:
        res -= heappop(hq)

print(res)

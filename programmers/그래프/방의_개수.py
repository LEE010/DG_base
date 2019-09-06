'''
방의 개수
문제 설명
원점(0,0)에서 시작해서 아래처럼 숫자가 적힌 방향으로 이동하며 선을 긋습니다.

스크린샷 2018-09-06 오후 4.55.33.png

ex) 1일때는 오른쪽 위로 이동

그림을 그릴 때, 사방이 막히면 방하나로 샙니다.
이동하는 방향이 담긴 배열 arrows가 매개변수로 주어질 때,
방의 갯수를 return 하도록 solution 함수를 작성하세요.

제한사항
배열 arrows의 크기는 1 이상 100,000 이하 입니다.
arrows의 원소는 0 이상 7 이하 입니다.
방은 다른 방으로 둘러 싸여질 수 있습니다.
입출력 예
arrows	return
[6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]	3
입출력 예 설명
스크린샷 2018-09-06 오후 5.08.09.png

(0,0) 부터 시작해서 6(왼쪽) 으로 3번 이동합니다. 그 이후 주어진 arrows 를 따라 그립니다.
삼각형 (1), 큰 사각형(1), 평행사변형(1) = 3
출처
'''
arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]

keys = {0:(0,1),1:(1,1),2:(1,0),3:(1,-1),4:(0,-1),5:(-1,-1),6:(-1,0),7:(-1,1)}
a = set([1,2,3])
a.remove(2)
a
def solution(arrows):
    def search(pos,visited):
        print('현위치:',pos,'방문지:',visited)

        if len(visited) > 2:
            if visited[-1] == (0,0):
                return visited
            elif visited[-2] == pos:
                return 0

        print('목적지:',graph[pos])
        for next in graph[pos]-set(visited[-2:]):
            res = search(next,visited+[pos])
            print(res)
            if res:
                rooms.append(res)
            # break
        return

    loc = (0,0)
    graph = {}
    for arrow in arrows:
        next = tuple(map(sum,zip(loc,keys[arrow])))
        try:
            graph[loc].add(next)
        except KeyError:
            graph[loc] = set([next])
        try:
            graph[next].add(loc)
        except KeyError:
            graph[next] = set([loc])
        loc = next
    graph
    rooms = []
    search((0,0),[])

    for room in rooms:
        print(room)
    return len(rooms)
graph[-1,0]
solution(arrows)

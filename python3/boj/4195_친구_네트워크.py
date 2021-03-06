'''
친구 네트워크 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
3 초	256 MB	22122	5385	3210	25.025%
문제
민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

출력
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

예제 입력 1 
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
예제 출력 1 
2
3
4
2
2
4
출처
Contest > Waterloo's local Programming Contests > 27 September, 2008 C번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: chinjja, jh05013
어색한 표현을 찾은 사람: stilltime
링크
HDU Online Judge
'''
from sys import stdin
from collections import deque

readline = stdin.readline


def union(a, b):
    x = find(a)
    y = find(b)

    if x != y:
        social[y] = x
        size[x] += size[y]


def find(a):
    if social[a] == a:
        return a
    social[a] = find(social[a])
    return social[a]


F = int(readline())

for _ in range(F):
    social = {}
    size = {}

    for i in range(int(readline())):
        a, b = readline().split()

        if a not in social:
            social[a] = a
            size[a] = 1

        if b not in social:
            social[b] = b
            size[b] = 1

        union(a, b)
        print(size[find(a)])

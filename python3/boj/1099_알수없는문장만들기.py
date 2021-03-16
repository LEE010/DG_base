'''
알 수 없는 문장 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	1418	394	245	28.790%
문제
형택이와 그의 친구들은 자꾸 다른 사람들이 대화를 엿듣는 것이 짜증났다. 따라서, 새로운 언어를 만들었다.

이 언어에는 단어가 N개 있다. 그리고 이 언어의 문장은 단어를 공백없이 붙여쓴 것이다. 이 문장에서 각 단어는 0번 또는 그 이상 나타날 수 있다. 이 언어가 형택스러운 이유는 (특별한 이유는) 단어에 쓰여 있는 문자의 순서를 바꿔도 되기 때문이다. 이때, 원래 단어의 위치와 다른 위치에 있는 문자의 개수 만큼이 그 순서를 바꾼 단어를 만드는 비용이다. 예를 들어, abc란 단어가 있을 때, abc는 비용 0으로 만들 수 있고, acb, cba, bac는 비용 2로 바꿀 수 있고, bca, cab는 비용 3으로 바꿀 수 있다.

따라서, 한 문장을 여러 가지 방법으로 해석할 수 있다. 이때 비용의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 문장이 주어진다. 문장의 길이는 최대 50이다. 둘째 줄에 단어의 개수 N이 주어지며, N은 50보다 작거나 같은 자연수이다. 셋째 줄부터 N개의 줄에 각 단어가 주어진다. 단어의 길이는 최대 50이다. 문장과 단어는 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 문제의 정답을 출력한다. 만약 문장을 해석할 수 없다면 -1을 출력한다.

예제 입력 1 
neotowheret
4
one
two
three
there
예제 출력 1 
8
출처
문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: hun3555
빠진 조건을 찾은 사람: kesakiyo
'''

from sys import stdin


def readline():
    return stdin.readline()


def calc(wordPos):
    res = 0

    for i in range(1,len(wordPos)):
        if wordPos[i-1]+1 != wordPos[i]:
            res += 1
    
    return res


def dfs(wordMap, word, i, used):
    if len(used) == len(word):
        return calc(used)

    res = float('inf')

    for w in wordMap[word[i]]:
        used.append(w)
        res = min(res, dfs(wordMap, word, i+1, used))
        used.pop()

    return res


if __name__ == "__main__":
    base = readline().strip()
    N = int(readline())

    words = [readline().strip() for _ in range(N)]
    charMap = {}

    for i, c in enumerate(base):
        if c not in charMap:
            charMap[c] = [i]
        else:
            charMap[c].append(i)

    total = 0

    for word in words:
        temp = dfs(charMap, word, 0, [])
        print(temp)
        total += dfs(charMap, word, 0, [])

    print(total)

'''
문제 설명
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
입출력 예
name	return
JEROEN	56
JAN	23
출처

※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.
'''
def cc(c):
    if c < 'N':
        answer = ord(c) - 65
    elif c > 'M':
        answer = 91 - ord(c)
    return answer

def search(string,pos):
    next = float('inf')

    for j in (-1,1):
        count = 0
        while string[pos+(j*count)] == 'A':
            count += 1
        if abs(next) >= count:
            next = (count) * j

    return next

def solution(name):
    answer = 0
    if name.count('A') == 0:
        for c in name:
            answer += cc(c)
        answer += len(name) -1
    else:
        name_lst = list(name)
        A = ['A' for _ in range(len(name))]
        pos = 0
        while name_lst != A:
            print(name_lst)
            next = search(name_lst,pos)
            answer += cc(name_lst[pos+next])
            name_lst[pos+next] = 'A'
            answer += abs(next)
            pos += next

    return answer

name = 'ABAAAAAAAAABB'
solution(name)

name = 'JEROEN'
solution(name)

name = 'JAN'
solution(name)

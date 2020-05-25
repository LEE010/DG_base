'''
소트인사이드
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	21559	12747	11019	60.408%
문제
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

입력
첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

예제 입력 1
2143
예제 출력 1
4321
출처
문제를 번역한 사람: baekjoon
빠진 조건을 찾은 사람: bvba djm03178
'''
from sys import stdin
N = stdin.readline().strip()
nums = list(map(int,N))
nums.sort(reverse=True)
print(''.join(map(str,nums)))

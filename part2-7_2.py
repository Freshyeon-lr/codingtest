# part 2. 주요 알고리즘 이론과 실전 문제
# - chapter 7. 이진 탐색
# - 예제 7-2. 부품 찾기
'''
import sys

def explore(array, n, start, end):
    while start<=end:
        mid = (start + end) // 2
        if array[mid] < n:
            start = mid
        elif array[mid] > n:
            end = mid
        else:
            return mid
len_array = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
len_n = int(sys.stdin.readline())
n = list(map(int,sys.stdin.readline().split()))

result = explore(array, n, 0, len_array-1)
'''

n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
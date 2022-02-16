# part 2. 주요 알고리즘 이론과 실전 문제
# - chapter 8. 다이나믹 프로그래밍
# - 예제 8-3. 개미 전사*

n = int(input())
array = list(map(int, input().split()))

d = [0]*100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])
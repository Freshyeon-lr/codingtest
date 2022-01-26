# part 2. 주요 알고리즘 이론과 실전 문제
# - Chapter 6. 정렬 알고리즘
# - 예제 6-4. 두 배열의 원소 교체

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

count = 0
for i in range(n):
    if b[-(i+1)] > a[i]:
        a[i] = b[-(i+1)]
        count += 1
    if count == k:
        break

print(sum(a))


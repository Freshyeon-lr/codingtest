# part 2. 주요 알고리즘 이론과 실전 문제
# - chapter 7. 이진 탐색
# - 예제 7-3. 떡볶이 떡 만들기*

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
print(result)
# part 2. 주요 알고리즘 이론과 실전 문제
# - chapter 8. 다이나믹 프로그래밍
# - 예제 8-2. 1로 만들기*

x = int(input())
d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)
print(d[x])

'''
x = int(input())
count = 0

#for i in range(x):
while x != 1:
    if x%5 == 0:
        x = x/5
        count += 1
    else:
        x = x-1
    if x%3 == 0:
        x = x/3
        count += 1
    if x%2 == 0:
        x = x/2
        count += 1

print("count = ", count)
print("x = ", x)
'''

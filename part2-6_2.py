# part 2. 주요 알고리즘 이론과 실전 문제
# - Chapter 6. 정렬 알고리즘
# - 예제 6-2. 위에서 아래로

count = int(input())
n_list = []
for i in range(count):
    n_list.append(input())

n_list.sort()
n_list.reverse()
for i in n_list:
    print(i+" ")
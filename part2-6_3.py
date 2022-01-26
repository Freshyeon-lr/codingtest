# part 2. 주요 알고리즘 이론과 실전 문제
# - Chapter 6. 정렬 알고리즘
# - 예제 6-3. 성적이 낮은 순서로 학생 출력하기

count = int(input())
students = []

def set(array):
    return array[1]

for i in range(count):
    inform = input().split()
    name = inform[0]
    score = inform[1]
    students.append((name, score))

result = sorted(students, key=set)

for i in result:
    print(i[0], end=' ')
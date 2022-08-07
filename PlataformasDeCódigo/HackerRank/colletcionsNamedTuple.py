from collections import namedtuple
n, clmn = int(input()), namedtuple('student', input().split())
cls = [clmn(*input().split()) for _ in range(n)]
print(f'{sum([int(student.MARKS) for student in cls])/n}')
students = ["egoing", "sori", "maru"]
grade = [2,1,4]

print(students[0])
print("len(students)", len(students))

print(min(grade))
print(max(grade))

import statistics
print(statistics.median(grade))

import random
print(random.choice(students))

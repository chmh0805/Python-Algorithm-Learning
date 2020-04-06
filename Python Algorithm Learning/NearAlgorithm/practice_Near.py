
import sys


min = sys.maxsize

numbers = [ 24, 53, 45, 30, 89, 76, 92, 62 ]
N = len(numbers)
target = 50
near = 0

for i in range(0, N):
    _abs = abs(numbers[i] - target)
    if _abs < min:
        min = _abs
        near = numbers[i]

print(f"{target}의 근삿값은 {near} 입니다.")


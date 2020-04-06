
import sys

numbers = [ 6728, 6739, 32592, 28, 119, 2856 ]
max = - sys.maxsize - 1
N = len(numbers)

for i in range(N):
    if numbers[i] > max:
        max = numbers[i]

print (f"{numbers}중 가장 큰 수는 {max} 입니다.")

import sys

numbers = [ 30, 31, 40, 50, 60, 70, 80 ]
min = sys.maxsize
N = len(numbers)

for i in range(N):
    if numbers[i] < min and numbers[i] % 2 != 1 :
        min = numbers[i]

print (min)
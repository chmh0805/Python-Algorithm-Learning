
def main():
    pass

numbers = [30, 45, 34, 65, 24, 7]
N = len(numbers)
ranking = [1] * N 

for i in range(0, N - 1):
    for j in range(i + 1, N):
        if numbers[i] < numbers[j]:
            temp = numbers[i]; numbers[i] = numbers[j]; numbers[j] = temp;

for i in range(N):
    ranking[i] = 1
    for j in range(N):
        if numbers[i] < numbers[j]:
            ranking[i] += 1
        
for i in range(N):   
    print(f"{numbers[i]}는 {ranking[i]}등 입니다.")


if __name__ == "__main__":
    main()
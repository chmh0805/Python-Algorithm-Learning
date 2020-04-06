
def main():
    pass


data = [43, 24, 13, 60, 34, 56]
N = len(data)

for i in range(0, N - 1):
    for j in range (i + 1, N):
        if data[i] > data[j]:
            temp = data[i]; data[i] = data[j]; data[j] = temp;

print (data)

if __name__ == "__main__":
    main()
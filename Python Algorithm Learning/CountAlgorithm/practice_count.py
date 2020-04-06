
# 1부터 1,000까지의 정수 중 15의 배수의 개수

def main():
    pass

count = 0

for i in range (0, 1000):
    if i % 15 == 0:
        count += 1

if __name__ == "__main__":
    main()

print (f"1부터 1000까지의 정수 중 15의 배수의 개수는 {count}개 입니다.")
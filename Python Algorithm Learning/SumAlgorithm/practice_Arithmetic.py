
# 1,000 이하 정수 중 홀수의 합

def main():
    pass
sum = 0

for i in range(0, 1000):
    if i % 2 != 0:
        sum = sum + i

print(f"1,000이하 정수 중 홀수의 합은 {sum}입니다.")

if __name__ == "__main__":
    main()
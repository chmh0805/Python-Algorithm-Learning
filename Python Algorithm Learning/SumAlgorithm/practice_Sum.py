
def main():
    pass

scores = [100, 53, 68, 30, 80, 90, 85, 94, 97]
N = len(scores)
sum = 0

for i in range(N):
    if scores[i] >= 80:
        sum = sum + scores[i]


print(f"{scores}중 80점 이상인 점수들의 합계는 {sum}입니다.")

if __name__ == "__main__":
    main()


# n명의 점수 중에서 80점 이상 95점 이하인 점수들의 평균

def main():
    pass

scores = [ 80, 85, 90, 95, 100 ]
N = len(scores)
avg = 0.0
sum = 0
count = 0

for i in range(N):
    if scores[i] >= 80 and scores[i] <= 95:
        sum = sum + scores[i]; count += 1;
    avg = sum / count

print (f"{scores} 중 80점 이상 95점 이하인 점수는 {count}개이고, 합계는 {sum}점이며, 평균은{avg:.2f}점입니다.")

if __name__ == "__main__":
    main()
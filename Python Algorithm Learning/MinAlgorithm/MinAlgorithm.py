
# 최솟값 알고리즘(Min Algorithm) : (주어진 범위 + 주어진 조건)의 자료들 중 가장 작은 값(최솟값)

# [?] 주어진 데이터 중에서 가장 작은 [짝수] 값

import sys

def main():
    # [0] Initialize
    min = sys.maxsize # 최댓값은 최소로 초기화 / 최솟값은 최대로 초기화

    # [1] Input
    numbers = [ 2, 5, 3, 7, 1 ]; # MIN : 1 -> [짝수]MIN : 2
    N = len(numbers) # 의사코드(슈도코드)

    # [2] Process
    for i in range (0,N): #주어진 범위
        if numbers[i] < min and numbers[i] % 2 == 0 : # 짝수 조건 설정
            min = numbers[i] # MIN Algorithm : 더 작은 값으로 할당
    # [3] Output
    print(f"짝수인 최솟값:{min}")

if __name__ == "__main__":
    main()


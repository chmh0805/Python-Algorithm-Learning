# Max Algorithm (최댓값, 결괏값, 변숫값) : (주어진 범위 + 주어진 조건)의 자료들 중 가장 큰 값

# [?] 주어진 데이터 중에서 가장 큰 값
import sys

def main ():
    # [0] Initialize
    max = -sys.maxsize - 1 # 숫자 형식의 데이터 중 가장 작은 값으로 초기화 
   
    # [1] Input
    numbers = [ -2, -5, 0, -3, -7, -1 ] # MAX : 0
    N = len(numbers) # 의사코드(슈도코드)

    # [2] Process : MAX
    for i in range (0,N): # 주어진 범위
        if numbers[i] > max: # 더 큰 데이터가 있다면
            max = numbers[i] # MAX : 더 큰 값으로 할당

    # [3] Output
    print(f"주어진 데이터 중에서 가장 큰 값(최댓값): {max}")

if __name__ == "__main__":
    main()

# 최빈값 알고리즘(MODE Algorithm) : 점수 인덱스(0~n)의 개수(COUNT)의 최댓값(MAX)
# [?] 주어진 데이터에서 가장 많이 나타난(중복된) 값

import sys

# [1] Input
scores = [ 1, 3, 4, 3, 5, 9, 9, 9, 7, 8, 9 ] # 0 ~ 5점까지만 들어온다고 가정
indexes = [0] * ( len(scores) + 1 ) # 0 ~ 5가지 점수 인덱스의 개수 저장
max = -sys.maxsize - 1 # MAX 알고리즘 적용 ( max는 가장 작은 값으로 초기화)
mode = 0 # 최빈값이 담길 그릇

# [2] Process : Data -> Index -> Count -> Max -> Mode
for i in range (0, len(scores)):
    indexes[scores[i]] = indexes[scores[i]] + 1 # COUNT 알고리즘 적용
for i in range (0, len(indexes)):
    if indexes[i] > max :
        max = indexes[i] # MAX 알고리즘 적용
        mode = i # MODE 알고리즘 적용

# [3] Output : 3
print (f"최빈값: {mode} -> {max}번 나타남")
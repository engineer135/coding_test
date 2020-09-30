"""
선택정렬 테스트!
"""
from random import randint
import time

array = []
for i in range(10000):
    array.append(randint(1, 100)) # 1부터 100 사이 랜덤 정수

start_time = time.time()

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스왑..

end_time = time.time()

print("선택정렬 성능 측정: ", end_time - start_time)

# 기본정렬 라이브러리 성능 측정
start_time = time.time()

# 기본정렬 라이브러리 사용
array.sort()

end_time = time.time()

print("기본정렬 라이브러리 성능 측정: ", end_time - start_time)

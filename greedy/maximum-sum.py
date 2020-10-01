"""
큰 수의 법칙

입력값 : 
배열의 크기 N
숫자가 더해지는 횟수 M
배열의 같은 인덱스가 연속해서 K번을 초과하여 더해질 수 없음

ex)
[2,4,5,4,6]
M = 8
K = 3
6+6+6+5+6+6+6+5=46
"""

N = 5
M = 8
K = 3
array = [2,4,5,4,6]
sum = 0

# 일단 큰 순서대로 정렬을 해야겠네
# 그리고 더하면 됨...

# 정렬부터 하자
for i in range(len(array)):
    max_index = i
    for j in range(i+1, len(array)):
        if array[max_index] < array[j] :
            max_index = j
    array[max_index], array[i] = array[i], array[max_index] # swap

print(array)

# 큰수부터 더하자. 대신 K번을 초과하면, 다음 수를 더하고 다시 돌아옴.
index = 0
indexSumCnt = 0
for i in range(M):
    print(array[index])
    sum += array[index]
    indexSumCnt += 1 

    if index > 0 :
        index -= 1
        continue

    if K == indexSumCnt :
        index += 1
        indexSumCnt = 0

print(sum)

'''
이게 내 첫번째 답.
답은 맞게 나왔지만.. 로직에 조건절이 좀 깔쌈한 맛이 안난다. 그리고 다른 배열이 들어왔을때도 정답이 나올까? 확신이 안선다.
'''
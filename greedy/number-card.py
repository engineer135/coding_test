"""
n개의 행 m개의 열 입력 받고
각 행마다 가장 작은 수를 찾은 뒤에 그 수중에서 가장 큰 수를 찾는 문제.
이거는 문제 독해가 더 어려웠음. 무슨 말인지 이해하기가 힘들어서..
이해만 하면 어렵지 않은 문제임
"""

n, m = map(int, input().split())

print("n: ", n)
print("m: ", m)

array = [0]*n

for i in range(n):
    #print(i)
    array[i] = list(map(int, input().split()))

print('array:', array)

min_index = 0
min_number = array[0][0]

# 가장 작은 수가 가장 큰 인덱스를 찾아야함
for i in range(len(array)):
    array[i].sort() # 정렬    
    if min_number > array[i][0]:
        min_number = array[i][0]
        min_index = i

print("min_index: ", min_index)
print("min_number: ", array[min_index][0])

print("최종 숫자 = 가장 작은 수가 있는 인덱스의 가장 큰 수 : ", array[min_index][m-1])



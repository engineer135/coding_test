"""
입력
n n*n개의 정사각형
rlud 상하좌우 커맨드

출력
최종 좌표
"""

n = int(input())
directionList = list(map(str, input().split()))

array = [[0]*n]*n

print(array)

# for i in range(n):
#     for j in range(n):
#         array[i][j] = j+1
# print(array)

"""
좌표가 
1,1 1,2 1,3 ...
2,1 2,2 2,3 ...
이렇게 생기고, 시작점은 1,1 이다.
"""
index = 0
horizon = 0
vertical = 0
while index < len(directionList):
    if directionList[index] == 'r':
        if horizon + 1 < n:
            horizon += 1
    if directionList[index] == 'l':
        if horizon - 1 > 0:
            horizon -= 1
    if directionList[index] == 'u':
        if vertical - 1 > 0:
            vertical -= 1
    if directionList[index] == 'd':
        if vertical + 1 < n:
            vertical += 1
    index += 1

print("horizon : ", horizon+1)
print("vertical : ", vertical+1)

# 아.. 답안 보고 나니 현타 또 오네. 이게 뭐냐 비루한 내 정답..
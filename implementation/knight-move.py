"""
왕실의 나이트 문제.
체스위의 나이트가 갈 수 있는 경우의 수 출력하기.
x축은 a-h
y축은 1~8
최초 좌표 입력 받고, 거기서 나이트가 갈 수 있는 경우의 수를 출력하면 된다.

제한시간은 20분인데 나는 한시간 걸렸네 ㅠㅠ..

좌표 입력받기
a1 > 0,0으로 입력 변환해야함
"""
inputStr = input()
inputX = inputStr[0]
inputY = int(inputStr[1]) - 1
charArr = ['a','b','c','d','e','f','g','h']

locationX = charArr.index(inputX) # 변환 필요
locationY = inputY

print("locationX=", locationX)
print("locationY=", locationY)

#chessBoard = [[x for x in range(0, 8)] for y in range(0, 8)]
#print(chessBoard)

# X가 가로축, Y가 세로축
# 나이트가 갈수 있는 경우의 수는 총 8개밖에 없음
move1 = ['U','U','L']
move2 = ['U','U','R']
move3 = ['L','L','U']
move4 = ['L','L','D']
move5 = ['R','R','U']
move6 = ['R','R','D']
move7 = ['D','D','R']
move8 = ['D','D','L']

moveArr = [move1, move2, move3, move4, move5, move6, move7, move8]

directionArr = ['U','R','D','L']
urdlX = [0, 1, 0, -1]
urdlY = [-1, 0, 1, 0]

# [0,0]이라고 가정하고 시작하면
#locationX = 2
#locationY = 1
movedX = locationX
movedY = locationY
count = 0
for move in moveArr:
    movedX = locationX
    movedY = locationY
    print("move=",move)
    for i in range(len(move)):
        mx = urdlX[directionArr.index(move[i])]
        my = urdlY[directionArr.index(move[i])]
        movedX += mx
        movedY += my
    print("movedX=", movedX)
    print("movedY=", movedY)
    if movedX >= 0 and movedY >= 0:
        count += 1
    else:
        continue

print(count)





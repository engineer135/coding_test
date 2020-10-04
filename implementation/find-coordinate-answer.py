n = int(input())
x, y = 1, 1
plans = input().split() # plans로 받는구나 이렇게 해도 리스트 형식으로 받아지는구나..

#L, R, U, D에 따른 이동 방향!
dx = [0, 0, -1, 1] # 세로
dy = [-1, 1, 0, 0] # 가로
move_types = ['L', 'R', 'U', 'D']
# 아 이걸 이렇게 만들어놓으면 편함? 아 뭔가 편해보인다... -_-

# 이동 계획을 하나씩 확인
nx = 1
ny = 1
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i] # 아 이부분 신박하네 -_-
    # 공간 벗어나는 경우에는 무시... 무시를 여기서 하는구나 일단 nx, ny에 값 박아놓고! temp 값이네.
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    # 공간 안벗어났다면, x, y에 값 대입. 이동 수행.
    x, y = nx, ny

print(x,y)
"""
여기서 헷갈린게 x,y좌표의 위치였음. 
자꾸 가운데가 0,0이고 위아래로 x,y값이 증가한다고 생각하니 좌표값이 계속 헷갈림
좌표 증감 방향을 보고 x,y 값 기준을 생각해야 함. 멍청아...!
"""




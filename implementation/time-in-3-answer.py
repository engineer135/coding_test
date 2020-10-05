"""
아 이거 정답을 봤더니 또 현자 타임.. ㅠㅠ
똥멍청아!
"""

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시간 안에 3이 포함되어 있다면 카운트 증가..ㅠㅠ
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

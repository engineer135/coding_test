"""
단순한 답안 예시
"""

# N M K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 가장 큰수
second = data[n-2] # 두번째로 큰수

result = 0

while True :
    for i in range(k): #가장 큰수 k번 더하기
        if m == 0:
            break
        result += first
        m -= 1 # 더할때마다 1씩 배기
    if m == 0:
        break
    result += second # 두번째 큰수 한번 더함
    m -= 1

print(result)

"""
M의 크기가 100억 이상으로 커진다면 시간 초과 판정이 뜨는 예시.
이것도 엄청 잘한거 같은데..ㅠㅠ
"""
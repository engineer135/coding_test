"""
n, k 입력 받음

1. n-1
2. n/k (단, 이때 k로 나누어 떨어질 경우에만 수행 가능)

위 두가지 식을 수행해서 n을 1로 만드는 최소 수행 횟수를 구하는 문제
"""

n, k = map(int, input().split())
count = 0

while True:
    if n%k == 0:
        # 나누어 떨어진다면 나누기 수행
        n = n//k
    else:
        # 나누어 떨어지지 않으면 -1 수행
        n = n-1
    count += 1
    if n <= 1:
        break

print(count)
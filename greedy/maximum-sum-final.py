"""
이 문제는 '반복되는 수열'에 대해서 파악하는게 첫번째임

(6+6+6+5) + (6+6+6+5)

M을 (K+1)로 나눈 몫 = 반복 횟수
반복 횟수 * K = 가장 큰수가 등장하는 횟수
반복횟수가 나누어 떨어지지 않는 경우에는? 나머지만큼 가장 큰수를 더해야함

정리하면

int(M / (K+1)) * K + M % (K+1)

이 식으로 가장 큰수가 더해지는 횟수를 구한 뒤에,
이를 이용해 두번째 큰 수가 더해지는 횟수까지 구할 수 있음.

아니 근데.. 이게 트레이닝으로 된다고? 이런 생각을 할 수 있다고?
수학적 사고 ㅠㅠ 시바...
"""

n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

firstCnt = int(m / (k+1)) * k + m % (k+1)
secondCnt = m - firstCnt

sum = (first * firstCnt) + (second * secondCnt)

print(sum)
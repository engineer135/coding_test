"""
입력 
n 시간

출력
3이 들어간 시간의 개수

00시 00분 00초부터 n시 59분 59초까지 시간에서 3이 들어간 시간의 개수
"""

n = int(input())

count = 0
for h in range(n+1):
    if h//10 == 3 or h%10 == 3:
        count += 60 * 60 # 시간이 3이 들어가면, 분, 초는 볼 것도 없이 개수에 포함해야함. 분의 개수 * 초의 개수
        continue
    for m in range(60):
        if (m in range(30, 40)) or m//10 == 3 or m%10 == 3:
            count += 60 # 분이 3이 들어가면, 초는 볼 것도 없이 개수에 포함해야함. * 초의 개수
            continue
        for s in range(60):
            #print("hh mm ss",h,m,s)
            if (s in range(30, 40)) or s//10 == 3 or s%10 == 3:
                count += 1 # 초는 하나씩 다 세야함

print(count)

"""
제한시간 15분인데 40분만에 풀었네 ㅠㅠ
그래도 혼자 푼게 어디냐 긍정적으로 생각하자 ㅋ
"""
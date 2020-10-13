"""
스택 = 박스 쌓기
선입후출, 후입선출
"""

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.pop() # 3제거
stack.append(1)

print(stack) # 최하단부터 출력
print(stack[::-1]) # 최상단부터 출력


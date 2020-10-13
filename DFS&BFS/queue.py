"""
큐=대기 줄이랑 같음
선입선출
"""

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft() #5제거
queue.append(1)

print(queue)
queue.reverse() #뒤집기
print(queue)
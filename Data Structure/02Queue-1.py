# Queue
# 구조: FIFO / LILO

# 알아둘 용어
# - Enqueue : 큐에 데이터를 넣는 기능
# - Dequeue : 큐에서 데이터를 꺼내는 기능

# 파이썬 queue 라이브러리
# - Queue(): 가장 일반적인 큐 자료구조
# - LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조 (=스택)  
# - PriorityQueue(): 데이터마다 우선순위를 넣어서 우선순위가 높은 순으로 데이터 출력

# import library
import queue    
data_queue = queue.Queue()

# add data in queue
data_queue.put("a")
data_queue.put(2)

# check size
data_queue.qsize()
print(data_queue.qsize()) # result = 2

# get data = 데이터 빼기
data = data_queue.get()
print(data) # result = a = 제일 처음 넣은 데이터

# 다시 check size
print(data_queue.qsize())   # result = 1 / 하나 빠졌으니까

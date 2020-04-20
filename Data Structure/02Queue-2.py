# LifoQueue
import queue
data_queue = queue.LifoQueue()

data_queue.put("abc")
data_queue.put(123)

print(data_queue.qsize())   #result = 2

print(data_queue.get()) #result = 123 = 마지막에 넣은 값이 출력

print(data_queue.qsize()) #result = 1



# PriorityQueue()
prior = queue.PriorityQueue()

# .put((우선순위, "값"))
prior.put((10, "data"))
prior.put((5,1))
prior.put((15,"abc"))

print(prior.qsize())    #result = 3

first = prior.get()
print(first)    #(5,1) 우선순위 제일 낮은 값 출력됨


# 큐는 멀티 태스킹을 위한 프로세스 스케줄링 방식을 구현하기 위해 많이 사용됨
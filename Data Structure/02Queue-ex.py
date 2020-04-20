queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]    #첫번째 값 꺼내주기
    del queue_list[0]       #값 뺐으니 삭제!
    return data

for i in range(10):
    enqueue(i)

size = len(queue_list)
print(size)     #result = 10

dequeue()
print(len(queue_list))
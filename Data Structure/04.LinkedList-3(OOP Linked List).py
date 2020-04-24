# 파이썬 OOP로 링크드 리스트 구현하기

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class NodeMg:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
# 데이터 삭제할 때

# 1) 맨 앞 삭제 = head 없어짐 ㅠ
# 2) 맨 마지막 삭제
# 3) 중간 삭제
    def delete(self,data):
        if self.head =='':
            print("해당 값을 가진 노드가 없습니다")
            return
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data==data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next


list1 = NodeMg(0)
print("Describe list1")
list1.desc()    # 0

print("\n")
print("Create node")

for data in range (1,10):
    list1.add(data)
list1.desc()

print("\n")
print("Check head and delete it")

#head가 살아있음을 확인
print("head: ",list1.head)   # <__main__.Node object at 0x039F6220>

#head =1 삭제 후 확인하기
list1.delete(0)
print("head after deletion: ",list1.head)   # None


print("\n")
print("Create new node (list2)")
# new node
list2 = NodeMg(0)
list2.desc()

print("\n")
print("Add data in new node (list2)")
for i in range(1,5):
    list2.add(i)
list2.desc()

print("\n")
print("Delete a node = 3 (list2)")
list2.delete(3)
list2.desc()
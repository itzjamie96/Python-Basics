# 다양한 링크드 리스트 구조

# Double Linked List
# - 노드 = (이전 데이터 주소) + (데이터) + (다음 데이터 주소)
# - 앞뒤로 주소가 달린 구조
# - 기존의 링크드 리스트의 단점(앞에서부터 정보 찾기)을 보완한 구조!

class Node:
    # prev(앞) & next(뒤)
    def __init__(self,data,prev=None,next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMg:
    def __init__(self,data):
        self.head = Node(data)
        
        # 뒤에서도 검색해야하니까 head도 있고 tail도 있다
        self.tail = self.head

    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # 앞에서 검색하기!
    def search_from_head(self,data):
        if self.head == None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    # 뒤에서부터 검색하기!
    def search_from_tail(self,data):
        if self.head == None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

# testing
print("Create list")
double = NodeMg(0)
for i in range(1,5):
    double.insert(i)
double.desc()

print("\n")
print("Search from head")
node3 = double.search_from_head(3)
if node3:
    print(node3.data)
else:
    print("No data")

print("\n")
print("Search from tail")
node2 = double.search_from_tail(2)
if node2:
    print(node2.data)
else:
    print("No data")


# 링크드 리스트의 장단점

# 장점
# - 미리 데이터 공간을 할당하지 않아도 됨

# 단점
# - 연결을 위한 별도 데이터 공간이 필요하기 때문에 저장공간 효율이 낮음
# - 연결 정보를 찾는 시간이 필요 = 접근 속도 느림
#   - 배열은 인덱스 번호로 바로 찾을 수 있는 반면 링크르 리스트는 앞에서부터 쭉 가야함
# - 중간 데이터 삭제/추가하면 앞뒤 데이터 연결을 다시 해줘야함


# 링크드 리스트 사이에 데이터 추가해보기
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Node와 Node 연결
node1 = Node(1)
node2 = Node(2)
node1.next = node2  #연결해주기
head = node1    #가장 앞의 주소 알아내기 

print("Original Node: ")
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

# new Node
node3 = Node(1.5)

node = head
search = True
while search:
    if node.data ==1:
        search = False
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

print("New Node: ")
while node.next:
    print(node.data)
    node = node.next
print(node.data)
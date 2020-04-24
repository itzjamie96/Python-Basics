# Linked List
# - 연결 리스트라고도 함

# - 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조
# - 미리 배열의 크기를 정해줘야했음 -> 이걸 보완하기 위한 자료구조 = Linked List
# => 필요할 때마다 추가할 수 있는 구조!

# - 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
# - 원래 C언어에서는 주요한 데이터 구조지만 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원


# 용어
# - Node: 데이터 저장 단위 (데이터값, 포인터)로 구성
# - 노드 = 데이터 + 다음 데이터 주소
# - 맨 앞 노드의 주소만 알면 전체 리스트의 값들을 알 수 있게됨
# - 주소 값이 null = 뒤에 연결된 데이터 없음

# - Pointer: 각 노드 안에서 다음이나 이전의 노드와의 연결 정보를 가진 공간


# Node 직접 구현해보기
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def add(data):
    node = head
    while node.next:        #노드에 다음 주소가 있을 때까지
        node = node.next
    node.next = Node(data)


# Node와 Node 연결
node1 = Node(1)
# node2 = Node(2)
# node1.next = node2  #연결해주기
head = node1    #가장 앞의 주소 알아내기

for index in range(1,10):   #1~9까지 (0~10까지의 마지막 숫자가 9니까)
    add(index)

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)
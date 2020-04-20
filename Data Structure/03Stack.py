# Stack
# - 데이터를 제한적으로 접근할 수 있는 구조
# - 한 쪽 끝에서만 자료를 넣거나 뺄 수 있음
# - 가장 나중에 넣은 데이터를 가장 먼저 빼낼 수 있음 = LIFO, FILO

# 대표 활용: 컴퓨터 내부의 프로세스 구조의 함수 동작 방식

# 주요 기능
# - push(): 데이터 넣기
# - pop(): 데이터 꺼내기

# 예시 (재귀함수)
def recursive(data):
    if data<0:
        print("finished")
    else:
        print(data)
        recursive(data-1)   #스스로 호출 중
        print("returned", data)

# recursive(4)

# 4
# 3
# 2
# 1
# 0
# finished      --> 끝났을 때 recursive(0)인 상태. data = 0
# returned 0    --> 그래서 0부터 시작
# returned 1
# returned 2
# returned 3
# returned 4



# 스택의 장단점
# - 장점: 구조 단순, 구현 쉬움, 데이터를 읽는 속도 빠름
# - 단점: 데이터 최대 갯수 미리 정해놔야함, 저장 공간 낭비할 수 있음


# 예시 1
stack = list()

stack.append(1)
stack.append(2)

print(stack)    # result = [1,2]

stack.pop()
print(stack)    # result = [1]



# 예시 2: 리스트 변수로 스택을 다루는 pop, push 구현해보기
stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]   # -1: 항상 맨 끝 값
    del stack_list[-1]
    return data

for i in range(10):
    push(i)

print(stack_list)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(stack_list[-1])   # result = 9

stack_list.pop()
print(stack_list)   # [0, 1, 2, 3, 4, 5, 6, 7, 8]
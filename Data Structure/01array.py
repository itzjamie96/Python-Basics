# 배열
# - 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
# - 파이썬에서는 리스트 타입이 배열 기능을 제공하고 있음

# 배열이 왜 필요할까?
# - 같은 종류의 데이터를 효율적으로 관리하기 위해 사용
# - 같은 종류의 데이터를 순차적으로 저장

# 장점:
# - 빠른 접근 가능
# 단점:
# - 배열의 사이즈 미리 알고있어야함
# - 추가, 삭제가 쉽지 않음

# 파이썬에서의 배열
country = 'US'
print(country)

country += 'A'
print(country) 
# 리스트처럼 배열이 사용가능하기 때문에 기존 배열의 단점을 느끼기 어려움


# 1차원 배열
data = [1,2,3,4,5]
print(data)

# 2차원 배열: 리스트로 구현시
twoD = [[1,2,3], [4,5,6],[7,8,9]]
print(twoD)
print(twoD[0])
print(twoD[0][1])

# 예제 1
# 위의 2차원 배열에서 9,8,7 순서로 출력해보기
arr = twoD[2]
print(arr[2], arr[1], arr[0])


# 예제 2: dataset에서 M이 몇번 나오는지 빈도수 출력하기
dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']
count=0
for name in dataset:
    for i in range(len(name)):
        if name[i] == 'M':
            count += 1
print(count)

        
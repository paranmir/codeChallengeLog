# A-B
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	401926	275410	232026	69.820%
# 문제
# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 첫째 줄에 A-B를 출력한다.

input = input().split()
print(int(input[0]) - int(input[1]))


a, b = map(int, input().split())
print(a-b)



# 평범한 배낭
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	119792	44559	28539	35.723%
# 문제
# 이 문제는 아주 평범한 배낭에 관한 문제이다.

# 한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 
# 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다.
# 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
# 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

# 입력
# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

# 입력으로 주어지는 모든 수는 정수이다.

# 출력
# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.



num, maxWeight = map(int, input().split())
#자리차지용 0,0 넣기. 
lst = [[0,0]]

# 2차원 배열을 만듦.
#이거는 가로로 테스트무게만큼, 세로로 물건갯수만큼, 값은 물건value의 합
backpack = [[0] * (maxWeight + 1) for _ in range(num + 1)]

# a b 줄바꿈 a b 형태로 들어오는걸 input으로 받아서 lst에 append 해야함
for _ in range(num):
    # [0]이 weight, [1]이 value.
    lst.append( [int(x) for x in input().split()] )
    
#range를 1로 시작해서, 물건갯수랑 가방의 최대 무게를 들어온 그대로 쓸 수 있게 함.
for stock in range(1, num + 1) :
    for testingWeight in range(1, maxWeight + 1) :
        weight = lst[stock][0]
        value = lst[stock][1]
        if testingWeight < weight:
            #넣어야할게 현재 testingWeight보다 무거우면, 이전 물건을 봤을때의 value 상태 유지.
            backpack[stock][testingWeight] = backpack[stock - 1][testingWeight]
        else :
            backpack[stock][testingWeight] = max(backpack[stock - 1][testingWeight], backpack[stock - 1][testingWeight-weight] + value)
            
print(backpack[num][maxWeight])
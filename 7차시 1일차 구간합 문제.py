times =int(input(''))
list1=[]                        # [[숫자들 1], [숫자집합2], [숫자집합 n]]
state = []                      #[숫자들 총 개수,  구간길이]
for i in range(times):
    list2=[]
    state.append(list(map(int, input().split(' '))))
    list2 = list(map(int, input().split()))
    list1.append(list2)

def sectionSumMax (list1, state):           
    totalNum = state[0]
    section = state[1]
    sumMax=0
    for i in range(section):     
        sumMax += list1[i] 
    for j in range(0, totalNum-section+1):
        intervalSum = 0
        for k in range(j, j+section):
            intervalSum += list1[k]
        if intervalSum > sumMax:
            sumMax = intervalSum
    return sumMax

def sectionSumMin (list1, state):
    intervalSum = 0                               #구간합
    totalNum = state[0]
    section = state[1]     
    sumMin =0   
    for i in range(section):
        sumMin += list1[i]
    for j in range(totalNum+1-section):
        intervalSum = 0
        for k in range(j, j+section):
            intervalSum += list1[k]
        if intervalSum < sumMin:
            sumMin = intervalSum
        intervalSum = 0
    return sumMin

for i in range(times):
    print(f'#{i+1} {sectionSumMax(list1[i], state[i])-sectionSumMin(list1[i], state[i])}')











    
                
    

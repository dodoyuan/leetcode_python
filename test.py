# --*-- coding:utf8 --*--

#Importing required modules
import math
import random
# import matplotlib.pyplot as plt


# First function to optimize
# 最大化
def function1(x):
    value = -x**2
    return value


# Second function to optimize
# 最大化
def function2(x):
    value = -(x-2)**2
    return value


# Function to find index of list
def index_of(a, list):
    for i in range(0, len(list)):
        if list[i] == a:
            return i
    return -1


# Function to sort by values
def sort_by_values(list1, values):
    '''
    返回的是list1对应的value排序后的下标。
    '''
    sorted_list = []
    while len(sorted_list) != len(list1):
        if index_of(min(values), values) in list1:
            sorted_list.append(index_of(min(values), values))
        values[index_of(min(values), values)] = float('inf')
    return sorted_list


# Function to carry out NSGA-II's fast non dominated sort
def fast_non_dominated_sort(values1, values2):
    S=[[] for i in range(0,len(values1))]
    front = [[]]
    n = [0 for i in range(0,len(values1))]
    rank = [0 for i in range(0, len(values1))]

    for p in range(0, len(values1)):
        S[p] = []  # 被p支配的解的集合
        n[p] = 0   # 支配p的解的个数
        for q in range(0, len(values1)):
            if (values1[p] > values1[q] and values2[p] > values2[q]) or (values1[p] >= values1[q] and values2[p] > values2[q]) or (values1[p] > values1[q] and values2[p] >= values2[q]):
                if q not in S[p]:
                    S[p].append(q)
            elif (values1[q] > values1[p] and values2[q] > values2[p]) or (values1[q] >= values1[p] and values2[q] > values2[p]) or (values1[q] > values1[p] and values2[q] >= values2[p]):
                n[p] += 1
        if n[p] == 0:
            rank[p] = 0
            if p not in front[0]:
                front[0].append(p)

    i = 0
    while front[i] != []:
        Q = []
        for p in front[i]:
            for q in S[p]:
                n[q] -= 1
                if n[q] == 0:
                    rank[q] = i+1
                    if q not in Q:
                        Q.append(q)
        i += 1
        front.append(Q)

    del front[len(front)-1]
    return front


# Function to calculate crowding distance
def crowding_distance(values1, values2, front):
    '''
    返回的是 front(下标表示)元素的拥挤度
    :param values1:
    :param values2:
    :param front:
    :return:
    '''
    # print 'front', front
    distance = [0 for i in range(0, len(front))]
    # 对front中指定下标的元素，根据其对应value值进行从小到大排序，返回的是排序好的下标
    sorted1 = sort_by_values(front, values1[:])
    sorted2 = sort_by_values(front, values2[:])
    # print sorted1, sorted2
    distance[0] = float('inf')
    distance[len(front) - 1] = float('inf')
    # distance 返回的是排序好之后的元素对应拥挤度，没有和 front 对应
    for k in range(1, len(front)-1):
        # 下面程序初次审查有点问题 values2[sorted1[k+1]] - values2[sorted1[k-1]]
        distance[k] = distance[k] + (values1[sorted1[k+1]] - values1[sorted1[k-1]])/(max(values1)-min(values1))
    for k in range(1, len(front)-1):
        distance[k] = distance[k] + (values1[sorted2[k+1]] - values2[sorted2[k-1]])/(max(values2)-min(values2))
    print 'distance:', distance
    return distance


# Function to carry out the crossover
def crossover(a, b):
    r = random.random()
    if r > 0.5:
        return mutation((a+b)/2)
    else:
        return mutation((a-b)/2)


# Function to carry out the mutation operator
def mutation(solution):
    mutation_prob = random.random()
    if mutation_prob <1:
        solution = min_x + (max_x-min_x) * random.random()
    return solution

# Main program starts here
pop_size = 20
max_gen = 30


# Initialization
min_x = -55
max_x = 55
solution = [min_x+(max_x-min_x)*random.random() for i in range(0, pop_size)]
gen_no = 0
while(gen_no < max_gen):
    function1_values = [function1(solution[i]) for i in range(0, pop_size)]
    function2_values = [function2(solution[i]) for i in range(0, pop_size)]
    # non_dominated_sorted_solution 中保存的是每层pareto最优解的序号
    non_dominated_sorted_solution = fast_non_dominated_sort(function1_values[:], function2_values[:])
    print("The best front for Generation number ", gen_no, " is")
    for valuez in non_dominated_sorted_solution[0]:
        # print(round(solution[valuez],3),end=" ")
        # 打印出每轮的pareto最优解
        print(round(solution[valuez], 3))
    print("\n")
    crowding_distance_values = []
    for i in range(0, len(non_dominated_sorted_solution)):
        crowding_distance_values.append(crowding_distance(function1_values[:], function2_values[:], non_dominated_sorted_solution[i][:]))
    solution2 = solution[:]
    # Generating offsprings
    while len(solution2) != 2 * pop_size:
        a1 = random.randint(0, pop_size-1)
        b1 = random.randint(0, pop_size-1)
        solution2.append(crossover(solution[a1], solution[b1]))
    function1_values2 = [function1(solution2[i]) for i in range(0, 2 * pop_size)]
    function2_values2 = [function2(solution2[i]) for i in range(0, 2 * pop_size)]
    # 对生成的新种群进行快速非排序
    # 输出类似 [[4, 8, 20], [29, 9], [11, 34], [19, 37], [12], [36], [17, 38], [15, 28],...]
    # 其中每个元素是对应到solution中解的下标
    non_dominated_sorted_solution2 = fast_non_dominated_sort(function1_values2[:], function2_values2[:])
    print 'non_dominated', non_dominated_sorted_solution2
    crowding_distance_values2 = []
    # 按层计算拥挤度，对应到上面的排序好之后的新种群
    for i in range(0, len(non_dominated_sorted_solution2)):
        crowding_distance_values2.append(crowding_distance(function1_values2[:], function2_values2[:], non_dominated_sorted_solution2[i][:]))
    new_solution = []
    # 从父子种群中选择出数量N的最优种群作为父种群,这步最需要理解
    for i in range(0, len(non_dominated_sorted_solution2)):
        non_dominated_sorted_solution2_1 = [index_of(non_dominated_sorted_solution2[i][j], non_dominated_sorted_solution2[i]) for j in range(0, len(non_dominated_sorted_solution2[i]))]
        # 这里比较乱，代码写的不好
        front22 = sort_by_values(non_dominated_sorted_solution2_1[:], crowding_distance_values2[i][:])
        front = [non_dominated_sorted_solution2[i][front22[j]] for j in range(0, len(non_dominated_sorted_solution2[i]))]
        front.reverse()
        print 'front:', front
        for value in front:
            new_solution.append(value)
            if len(new_solution) == pop_size:
                break
        if len(new_solution) == pop_size:
            break
    solution = [solution2[i] for i in new_solution]
    gen_no = gen_no + 1

#Lets plot the final front now
function1 = [i * -1 for i in function1_values]
function2 = [j * -1 for j in function2_values]
# plt.xlabel('Function 1', fontsize=15)
# plt.ylabel('Function 2', fontsize=15)
# plt.scatter(function1, function2)
# plt.show()
print function1
print function2
# --*-- coding:utf-8 --*--

# 直接插入排序
def insertSort(number):
    for i, num in enumerate(number):
        j = i - 1
        while j > 0 and number[j] > num:
            number[j+1] = number[j]
            j -= 1
        number[j+1] = num
    print number

def insertSort1(number):
    for i in range(1,len(number)):
        for j in range(i-1,-1,-1):
            if number[j] > number[j+1]:
                number[j], number[j+1] = number[j+1], number[j]
    print number


insertSort1([1,3,4,2,7,6,4])

# 冒泡排序
def bubbleSort(number):
    length = len(number)
    for i in xrange(length):
        for j in xrange(length-i-1):
            if number[j] > number[j+1]:
                number[j], number[j+1] = number[j+1], number[j]
    print number

bubbleSort([1,3,4,2,7,6,4])


# 选择排序
def selectSort(number):
    length = len(number)
    for i in range(length):
        minIndex = i
        for j in range(i+1, length):
            if number[j] < number[minIndex]:
                minIndex = j
        number[i], number[minIndex] = number[minIndex], number[i]

    print number

selectSort([1,3,4,2,7,6,4])

# 希尔排序
def shellSort(seq):
    length = len(seq)
    inc = 0
    while inc <= length/3:
        inc = inc * 3 + 1
    while inc >= 1:
        for i in range(inc, length):
            for j in range(i, 0, -inc):
                if seq[j] < seq[j-inc]:
                    seq[j], seq[j-inc] = seq[j-inc], seq[j]

        inc//=3


def shellSort1(seq):
    length = len(seq)
    inc = 0
    while inc <= length / 3:
        inc = inc * 3 + 1
    while inc >= 1:
        for i in range(inc, length):
            j = i
            temp = seq[j]
            while j-inc >= 0 and temp < seq[j-inc]:
                seq[j] = seq[j-inc]
                j -= inc
            seq[j] = temp

        inc //= 3


def HeapSort(seq):
    pass

# 增加一个元素，在数组尾, 然后进行堆调整
def HeapAdjustAdd(seq,index):
    temp = seq[index]
    rootIndex = (index - 1) / 2
    while rootIndex >= 0 and index != 0:
        if seq[rootIndex] <= temp:
            break
        else:
            seq[index] = seq[rootIndex]
            index = rootIndex
            rootIndex = (rootIndex - 1) / 2
    seq[index] = temp

# 堆调整
def HeapAdjust(seq, index, length):
    temp = seq[index]
    childIndex = index * 2 + 1
    while childIndex < length:
        # 找出左右节点中最大的数
        if childIndex + 1 < length and seq[childIndex] < seq[childIndex + 1]:
            childIndex += 1
        if seq[childIndex] <= temp:
            break
        seq[index] = seq[childIndex]
        index = childIndex
        childIndex = childIndex * 2 + 1
    seq[index] = temp


def heap_sort(data):
    m = len(data) / 2 - 1
    for i in range(m, -1, -1):
        HeapAdjust(data, i, len(data))
    for n in range(len(data) - 1, 0, -1):
        data[0], data[n] = data[n], data[0]
        HeapAdjust(data, 0, n)
    print data


def heap_adjust(data, s, m):
    temp = data[s]
    j = 2 * s + 1
    while j < m:
        if j < m - 1 and data[j] < data[j + 1]:
            j += 1
        if temp > data[j]:
            break
        data[s] = data[j]
        s = j
        j = 2 * s + 1
    data[s] = temp


def heap_sort1(data):
    m = len(data) / 2 - 1
    for i in range(m, -1, -1):
        heap_adjust(data, i, len(data))
    for n in range(len(data)-1, 0, -1):
        data[0], data[n] = data[n], data[0]
        heap_adjust(data, 0, n)
    print data


def mergeSort(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq) / 2
    left = mergeSort(seq[:mid])
    right = mergeSort(seq[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res

def quickSort(seq):
    if not seq:
        return []
    base = seq[0]
    left = [item for item in seq if item < base]
    right = [item for item in seq if item > base]
    return quickSort(left) + [base] + quickSort(right)

def countingSort(alist,k):
    n=len(alist)
    b=[0 for i in xrange(n)]
    c=[0 for i in xrange(k+1)]
    for i in alist:
        c[i]+=1
    for i in xrange(1,len(c)):
        c[i]=c[i-1]+c[i]
    for i in alist:
        b[c[i]-1]=i
        c[i]-=1
    return b

def radixSort(seq):
    for k in range(3):
        bucket = [[] for _ in range(10)]
        for item in seq:
            bucket[item // (10**k) % 10].append(item)
        seq = [item for i in bucket for item in i]
    return seq


if __name__=='__main__':
    import random
    a=[random.randint(0, 100) for i in xrange(100)]
    print radixSort(a)



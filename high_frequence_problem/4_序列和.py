


def SumofSeq():
    temp = raw_input().split(' ')
    number, n = map(int, temp)
    count, begin = 0, -1
    for i in xrange(n, 101):
        count = i
        if i > number:
            break
        if (number * 2) % i == 0:
            temp = (number * 2) / i - i + 1
            if temp % 2 == 0:
                begin = temp / 2
                break
    if count <= 100 and begin != -1:
        res = str(begin)
        for i in xrange(count-1):
            res += ' ' + str(begin + i + 1)
    else:
        res = 'No'
    print res

SumofSeq()
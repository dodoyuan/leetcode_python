

def possible_number():
    n = int(raw_input())
    temp = raw_input().split(' ')
    nums = map(int, temp)
    nums.sort()
    res = 'mistake'
    for i in xrange(1, n):
        if nums[i] == nums[i-1]:
            print 'mistake'
            return
    if nums[-1] - nums[0] == n - 1:
        if nums[0] == 1:
            res = str(nums[-1] + 1)
        else:
            res = str(nums[0] - 1) + ' ' + str(nums[-1] + 1)
    elif nums[-1] - nums[0] == n:
        for i in xrange(1, n):
            if nums[i] - nums[i - 1] == 2:
                res = str(nums[i] - 1)
                break
    else:
        res = 'mistake'
    print res


def binarysearch(nums,n):
    start, end = 0, n - 1
    while start + 1 < end:
        mid = start + (end - start) / 2
        if nums[mid] - nums[start] == mid - start:
            start = mid
        elif nums[mid] - nums[start] == mid - start + 1:
            end = mid

    if nums[start] + 2 == nums[end]:
        return nums[start] + 1
    else:
        return 'mistake'


possible_number()
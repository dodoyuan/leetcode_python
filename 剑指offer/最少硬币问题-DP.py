# --*-- coding:utf-8 --*--

# 面值为1 3 5的三种硬币，给定一个sum，求最少需要多少硬币

def minNumberOfcoins(sum):
    res = [0] * (sum + 1)
    for i in range(1, sum+1):
        if i >= 5:
            res[i] = min(res[i-5], res[i-3], res[i-1]) + 1
        elif i >= 3:
            res[i] = min(res[i - 3], res[i - 1]) + 1
        else:
            res[i] = res[i-1] + 1
    return res[-1]

if __name__ == '__main__':
    print minNumberOfcoins(4)
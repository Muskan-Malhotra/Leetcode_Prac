from math import sqrt

def main():
    n = 36
    num = n
    res = []

    for i in range (1, int(sqrt(n))+1):
        if n%i == 0:
            res.append(i) #36%2 => 18 [2]
            if n//i != i:
                res.append(n//i) # 18 => [2,18]

    # res.sort()
    return res




if __name__ == '__main__':
    res = main()
    print(res)

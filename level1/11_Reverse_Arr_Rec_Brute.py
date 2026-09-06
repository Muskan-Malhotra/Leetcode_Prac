def fun(lft, rgt, arr, out):
    if (lft == rgt):
        out.append(arr[lft])
        return

    fun(lft+1,rgt,arr,out)
    out.append(arr[lft])

    return



def main():
    arr = [5,7,3,2,6,1,5,9]
    # left = 2
    # right = 5
    left = 0
    right = 7

    out = []

    for i in range(0,left):
        out.append(arr[i])

    fun(left,right,arr,out)

    for i in range (right+1, len(arr)):
        out.append(arr[i])

    print(out)

if __name__ == '__main__':
    main()
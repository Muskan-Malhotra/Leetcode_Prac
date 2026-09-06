arr = [5,7,3,2,6,1,5,9]

lft = 0
rgt = 7

while(lft < rgt):

    # if (lft == rgt or lft > rgt):
    #     break

    arr[lft], arr[rgt] = arr[rgt], arr[lft]

    lft +=1
    rgt -=1

print(arr)
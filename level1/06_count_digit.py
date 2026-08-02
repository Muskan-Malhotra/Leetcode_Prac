from math import *

n=58731110239384934893

### Method 1
# num = n

# count = 0
# while(num >0):
#     num //= 10
#     count += 1

# print(count)


#Method 2

print(int(log10(n)+1))


## * TC: O(log10(n)) SC: O(1)

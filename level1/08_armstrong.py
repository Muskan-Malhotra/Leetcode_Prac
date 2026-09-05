n = 1634 #153
num = n
#method 1 nod=number of digits
nod = len(str(n)) # or int(log10(n)+1)

total = 0
while(n > 0):

    rem = n%10
    total += rem**nod
    n //= 10

if total == num:
    print("Is armstrong")
else:
    print("Not armstrong")


## * TC=O(log10(n)) *SC = O(1)
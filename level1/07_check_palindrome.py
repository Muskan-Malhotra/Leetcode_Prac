n = 121

num = n
res = 0
while(num > 0):

    ld = num%10
    num //= 10
    res = res*10 + ld


if res == n:
    print("Is Palindrome")
else:
    print("Not a palindrome")

### * TC = O(log10(N)). * SC = O(1)
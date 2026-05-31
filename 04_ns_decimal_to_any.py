n = 123
prod = 1
convert_to = 8
res = 0

while(n > 0):

    rem = n%convert_to
    res += rem*prod

    n //= convert_to
    prod *= 10

print(res)
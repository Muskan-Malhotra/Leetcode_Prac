n = 100
convert_from = 2
power = 0
res = 0

while(n>0):
    rem = n%convert_from
    res += rem*(convert_from**power)

    # print(f"{convert_to} {power} {convert_to ** power} {n}")

    n //= 10
    power += 1

print(res)
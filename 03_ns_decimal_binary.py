# Number system : binary to decimal

bin_num = 100
number = 0
prod = 1

while(bin_num>0):

    rem = bin_num%2
    number += rem*prod

    bin_num //= 2
    prod *= 10

print(number)

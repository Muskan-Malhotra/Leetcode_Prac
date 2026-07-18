n = -4
count = 0
digit = 4

while(n>0):
    if n%10 == digit:
        count = count+1
    
    n = n//10

print(count)


"""
Test Cases
-> 12343214144324454444
-> 4
-> -4
-> 2
-> -2
"""
n = 10
strg = ""

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1:
            strg += "*"
        else:
            if j == n-i-1:  
                strg += "*"
            else:
                strg += " "
    print(strg)
    strg = ""
                    

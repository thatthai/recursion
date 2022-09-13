def Fac(n) :
    if n == 0 or n == 1:
        return 1
    else :
        return Fac(n-1) * n
    

inp = int(input("Enter Number : "))
print(str(inp) + "! = " + str(Fac(inp)))
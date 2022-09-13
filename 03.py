def power(a,n) : #a^n
    if n == 0 :
        if a == 0 :
            return "Invalid"
        else :
            return 1
    elif n == 1 :
        return a
    else :
        return power(a,n-1) * a

a,b = input("Enter Input a b : ").split()
a,b = int(a),int(b)
print(power(a,b))


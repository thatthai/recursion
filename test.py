#Recursion การแก้ปัญหาแบบเรียกซ้ำ
#แก้ปัญหาเดิมให้มันเล็กลง
 
#  eatUp(n) = eatUp(n-1) + eat1

# Ex; 

# def EatUp(n) :
#     if n > 1 : #ถ้า n > 1 ถือเป็น recursive case
#         EatUp(n-1)
#         print('eat1')
#     #n <= 1
#     elif n==1 : #base case 
#         print('eat1')

#interative
# def Fac(n) :
#     result = 1
#     for i in range(2, n+1) :
#         result *= i
#     print(result)

#recursive
# def Fac(n) :
#     if n == 0 or n == 1:
#         return 1
#     else :
#         return Fac(n-1) * n

#sum ผิดตรงไหนแวะ
# def sum(n,l):
#     if n == 0 :
#         return 0
#     elif n == 1:
#         return l[-1]
#     else :
#         return sum(n-1,l) + l[-1]
    

#inp = int(input("enter : "))
l =[10,15]
print(sum(len(l),l))

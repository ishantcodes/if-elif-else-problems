#Write a program to find the greatest of four numbers entered by the user.


n1st = int(input("Enter 1st numbrr: "))
n2nd = int(input("Enter 2nd numbrr: "))
n3rd = int(input("Enter 3rd numbrr: "))
n4th = int(input("Enter 4th numbrr: "))

if n1st>n2nd and n1st>n3rd and n1st>n4th:
    print("greatest number is", n1st)
elif n2nd>n1st and n2nd>n3rd and n2nd>n4th:
    print("greatest number is", n2nd)
elif n3rd>n1st and n3rd>n2nd and n3rd>n4th:
    print("greatest number is", n3rd)
else:
    print("greatest number is", n4th)
    
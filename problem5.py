# Write a program which finds out whether a given name is present in a list or not.

l = []

n1 = input("Enter Your Name: ")
n2 = input("Enter Your Name: ")
n3 = input("Enter Your Name: ")
n4 = input("Enter Your Name: ")
n5 = input("Enter Your Name: ")
n6 = input("Enter Your Name: ")
n7 = input("Enter Your Name: ")
n8 = input("Enter Your Name: ")

l.append(n1)
l.append(n2)
l.append(n3)
l.append(n4)
l.append(n5)
l.append(n6)
l.append(n7)
l.append(n8)

find = input("Enter the Name you wanna Find: ")

if find in l:
    print("Your given name index is", l.index(find), "in list :", l)
else:
    print("no name found")

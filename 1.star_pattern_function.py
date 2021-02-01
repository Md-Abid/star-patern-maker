a = int(input("Please enter number of line you want to print\n"))
b = bool(int(input("please enter 1 for true or  0 for False\n")))


def star(a, b):
    if b == True:
        c = 1
        while c <= a:
            print(c * "*")
            c = c + 1
    else:
        while a > 0:
            print(a * "*")
            a = a - 1

star(a, b)

#Making Pyramid.
a=int(input())
for i in range(a):
    for j in range(a-i-1):
        print(end=" ")
    for j in range(i+1):
        print("*",end=' ')
    print()
    
#Making pyramid.
n = int(input())
for i in range(n):
    print(" "*(n-(1+i))+"* "*(1+i))

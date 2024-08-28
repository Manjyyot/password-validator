#prime number

a = int(input("enter a number"))

if a<2:

    print(a ," is not prime")

if a>=2:

    flag = 0

    for i in range(2,a//2+1):

        if a%i == 0:

            flag = 1

            break

        else:

            flag = 0

if flag == 1:

    print (a, " is not prime")

else:

    print(a," is prime")
n1 = 0
n2 = 1

userNum = int(input("Enter a Fib number: "))

if userNum <= 0:
    print("ERROR: User number must be positive")
elif userNum == 1:
    print("0")
else:
    print(str(n1) + " + " + str(n2), end="")
    for i in range(userNum - 2):
        n3 = n1 + n2
        print(" + " + str(n3), end="")
        n1 = n2
        n2 = n3

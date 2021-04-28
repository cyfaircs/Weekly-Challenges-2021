# Michael Cardoso, Project Weekly Challenge

import random

print ("Which project would you like: ")
print ("1. FizzBuzz")
print ("2. Fibonacci")
print ("3. Fibonacci - Cont.")
print ("4. Trivia Game")

projectNum = input()

if (projectNum == "1"): #FizzBuzz
    print ()
    x = 0
    while x < 100:
        x += 1
        if ((x % 3 == 0) and (x % 5 == 0) ):
            print (x, "-FizzBuzz")
        elif (x % 3 == 0):
            print (x, "-Fizz")
        elif (x % 5 == 0):
            print (x, "-Buzz")
        else:
            print(x)

elif (projectNum == "2"): #Fibonacci
    print ()
    print ("How long do you want your Fibonacci to be?")
    fibLength = int(input())
    a_0 = 0
    a_1 = 1
    counting = 0
    if (fibLength < 0):
        print ("It cannot be less than zero.")
    elif (fibLength == 0):
        print (a_0)
    elif (fibLength == 1):
        print (a_1)
    else :
        while (counting < fibLength - 1):
            a_n = a_0 + a_1
            a_0 = a_1
            a_1 = a_n
            counting += 1
    print( "Fib(" + str(fibLength) + ") = " + str(a_n))


elif (projectNum == "3"): #Fibonacci - Cont.
    print ()
    print ("How long do you want your Fibonacci to be?")
    fibLength = int(input())
    a_0 = 0
    a_1 = 1
    counting = 0
    sum = 0
    if (fibLength <= 0):
        print ("It cannot be less than zero.")
    elif (fibLength == 1):
        print (a_0)
    else :
        while (counting < fibLength - 1):
            a_n = a_0 + a_1
            a_0 = a_1
            a_1 = a_n
            if (a_1 % 2 == 0):
                sum = sum
            else:
                sum = sum + a_1
            counting += 1
    print( "Total sum:", sum + 1)
    
elif (projectNum == "4"): #Trivia Game
    print ("This is the Magic 8-Ball, Write your desires and I'll tell you our outcome:")
    userAns = input()
    outcomes = [
        "As I see it, yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "It is certain.",
        "It is decidedly so.",
        "Most likely.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook good.",
        "Reply hazy, try again.",
        "Signs point to yes.",
        "Very doubtful.",
        "Without a doubt.",
        "Yes.",
        "Yes – definitely.",
        "You may rely on it."
        ]
    print (random.choice(outcomes))
else :
    print ("Yooo u braken B use numbers from 1 to 4 dawg!")
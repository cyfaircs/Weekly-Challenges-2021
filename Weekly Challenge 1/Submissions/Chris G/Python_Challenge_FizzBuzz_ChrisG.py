for i in range(101):
    if int(i) % 5 == 0 and int(i) % 3 == 0:
        print(str(i) + " - FizzBuzz")
    elif int(i) % 5 == 0:
        print(str(i) + " - Buzz")
    elif int(i) % 3 == 0:
        print(str(i) + " - Fizz")

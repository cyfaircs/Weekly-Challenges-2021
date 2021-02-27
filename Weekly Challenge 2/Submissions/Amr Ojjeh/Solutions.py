def factors(n: int):
    numbers = set()
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            numbers.add(i)
            numbers.add(n // i)
    numbers = list(numbers)
    numbers.sort()
    return numbers

def sort_numbers():
    numbers = input("Enter numbers (separated by comma): ").replace(" ", "").split(",")
    numbers = list(map(float, numbers))
    numbers.sort()
    print("Here's the list in increasing order: ", end="")
    print(", ".join(map(str, numbers)))

def sort_numbers_reverse():
    numbers = input("Enter numbers (separated by comma): ").replace(" ", "").split(",")
    numbers = list(map(float, numbers))
    numbers.sort(reverse=True)
    print("Here's the list in descending order: ", end="")
    print(", ".join(map(str, numbers)))

def print_all_factors():
    n = int(input("Enter an integer: "))
    all_factors = factors(n)
    print(f"The factors are: {', '.join(map(str,all_factors))}")


def is_prime():
    n = int(input("Enter an integer: "))
    all_factors = factors(n)
    if len(all_factors) == 2:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")

challenges = [sort_numbers, sort_numbers_reverse, print_all_factors, is_prime]

try:
    while True:
        print("Pick your challenge. Type anything else to quit.")
        for num, challenge in enumerate(challenges):
            print(f"{num + 1}. {challenge.__name__.replace('_', ' ').title()}")
        challenges[int(input("Enter a number corresponding to a challenge: ")) - 1]()
        print("\n\n")
except:
    pass

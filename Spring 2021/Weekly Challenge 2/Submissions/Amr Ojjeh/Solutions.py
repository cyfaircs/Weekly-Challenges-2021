def factors(n: int):
    numbers = []
    for i in range(1, n + 1):
        if n % i == 0:
            numbers.append(i)
    return numbers

def quick_sort(numbers, reverse=False):
    def swap(a, b):
        numbers[a], numbers[b] = numbers[b], numbers[a]

    def partition(a, b):
        i = a - 1
        j = a
        pivot = numbers[b - 1]
        for _ in range(b - a):
            if (not reverse and numbers[j] <= pivot) or (reverse and numbers[j] >= pivot):
                i += 1
                swap(i, j)
            j += 1
        return i

    def helper(low, high):
        if low == high:
            return

        pivot_index = partition(low, high)
        helper(low, pivot_index)
        helper(pivot_index + 1, high)

    helper(0, len(numbers))

    return numbers

def sort_numbers():
    numbers = input("Enter numbers (separated by comma): ").replace(" ", "").split(",")
    numbers = list(map(float, numbers))
    # Easy way: numbers.sort()
    # Harder way (quick sort):
    quick_sort(numbers)

    print("Here's the list in increasing order: ", end="")
    print(", ".join(map(str, numbers)))

def sort_numbers_reverse():
    numbers = input("Enter numbers (separated by comma): ").replace(" ", "").split(",")
    numbers = list(map(float, numbers))
    # Easy way: numbers.sort(reverse=True)
    # Harder way (quick sort):
    quick_sort(numbers, True)
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

if __name__ == "__main__":
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

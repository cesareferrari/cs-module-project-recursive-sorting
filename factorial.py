# code a factorial function

# n!
# n * (n - 1)... 1


# recursive

# Define base case
## return if we are at n == 1

# Move toward the base case
# Call itself

def factorial(n):
    if n == 1:
        return n
    # call with each number, then -1 and multiply it to 
    # previous until we hit base case
    return n * factorial(n - 1)

print(factorial(3) == 6)
print(factorial(4) == 24)


def iter_factorial(n):
    # make a tracker
    total = 1
    # make a while loop, and decrement n as we go
    while n != 1:
        # multiply our tracker at every step
        total *= n
        n -= 1

    # return tracker
    return total


print(factorial(3) == iter_factorial(3))
print(factorial(4) == iter_factorial(4))


# Time complexity: O(n) for both
# Space complexity: itertive

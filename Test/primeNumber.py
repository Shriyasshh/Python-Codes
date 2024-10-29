def is_prime(number):
    if number <= 1:
        return False  # 0 and 1 are not prime

    # Check divisibility from 2 to the square root of the number
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False  # Found a divisor, not prime

    return True  # No divisors found, prime

# Example usage:
user_number = int(input("Enter a positive integer: "))
if is_prime(user_number):
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")

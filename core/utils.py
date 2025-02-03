import math
import requests

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

# def is_armstrong(n):
#     digits = list(map(int, str(n)))
#     power = len(digits)
#     return sum(d ** power for d in digits) == n

def is_armstrong(n: int) -> bool:
    # Use the absolute value of the number for Armstrong checks
    n = abs(n)
    digits = list(map(int, str(n)))
    power = len(digits)
    return n == sum(d ** power for d in digits)

# def digit_sum(n):
#     return sum(map(int, str(n)))

def digit_sum(n: int) -> int:
    # Ensure negative numbers are handled correctly
    return sum(map(int, str(abs(n))))

def get_number_fact(n):
    url = f"http://numbersapi.com/{n}/math"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return "No fun fact available."
    return "No fun fact available."

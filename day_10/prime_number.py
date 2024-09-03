def is_prime(num):
    """Checks if number is prime(divisible just by 1 or itself)"""
    if num == 2:
        return True
    if num == 1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
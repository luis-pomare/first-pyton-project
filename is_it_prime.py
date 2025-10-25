def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if n is prime, False otherwise
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Check odd divisors from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def main():
    """Test the prime checking function with some examples."""
    test_numbers = [2, 3, 4, 5, 17, 25, 29, 97, 100, 101]
    
    print("Prime number checker:")
    print("-" * 30)
    
    for num in test_numbers:
        result = is_prime(num)
        status = "prime" if result else "not prime"
        print(f"{num:3d} is {status}")


if __name__ == "__main__":
    main()

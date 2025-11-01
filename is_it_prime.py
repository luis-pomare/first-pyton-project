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
    print("Prime number checker:")
    print("-" * 10)
    
    # Allow the user to input a number
    while True:
        try:
            user_input = input("Enter a number to check (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            num = int(user_input)
            result = is_prime(num)
            status = "prime" if result else "not prime"
            print(f"{num} is {status}")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

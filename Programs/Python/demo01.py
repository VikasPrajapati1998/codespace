'''
Prime number prediction program.
'''
def check_prime(num : int)-> bool:
    '''
        Check wheather a number is prime or not.
        Args: 
                num (int)
        Returns: 
                bool (True/False)
        Raises: 
                AnyException : If anything bad happen.
    '''
    for var in range(2, (num//2)+1, 1):
        if num % var == 0:
            return False
    return True

def main():
    '''
        Program execution start from this main() function.
        Args:
            None
        Returns:
            None
        Raises:
            AnyException : If anything bad happen.
    '''
    print("Check Wheather a number is Prime of not Prime.")
    num = int(input("Enter a number : "))
    if check_prime(num):
        print(f"{num} is a Prime Number.")
    else:
        print(f"{num} is not a Prime Number.")

if __name__ == "__main__":
    main()

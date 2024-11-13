def prime_checker(number):
    not_prime = False
    for n in range(2, number):
        if number % n == 0: 
            not_prime = True
    if not_prime:
        print(f"{number} is not prime number")
    else:
        print(f"{number} is a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)

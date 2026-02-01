def is_prime(num):
    if num == 1:
        return True
    # 1 is not prime
    if num == 2:
        return True
    # Return True (2 is prime)
    
    for i in range(2, num):
        if num % i == 0:
            return False
        # Checks if num is divisible by i
        # If yes → not prime → return False
        # Function stops immediately
        return True
        
        # This line runs after the loop finishes
        # Means no number divided num
        # So num is prime

number = int(input("enter the number:"))
if is_prime(number):
    print(number , "is a prime number")
else:
    print(number , "is not a prime number")    
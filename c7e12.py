def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primeNumbersUpToN(n):
    primes = [i for i in range(2, n+1) if isPrime(i)]
    return primes


n = int(input("Enter an integer greater than 1: "))
print("Prime numbers up to", n, ":", primeNumbersUpToN(n))

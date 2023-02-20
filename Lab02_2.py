while True:
    try:
        m = int(input("Enter the number m: "))
        n = int(input("Enter the number n: "))
        if m < 0 or n < 0:
            print("Invalid number please re-enter")
        else:
            break
    except ValueError:
        print("Please enter a number")
a = m
b = n
def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    if result == []:
        result.append("None")
    else:
        return result

#1.	Display all common prime dividers of them.
def problem1():
    m_primes = []
    n_primes = []
    primes = []
    limit = 0
    global m, n
    if m > n:
        limit = m
    if m < n:
        limit = n
    if m == n:
        limit = m

    for num in range (2, limit):
        isPrime = True
        for count in range(2, num):
            if num % count == 0:
                isPrime = False
                break
            if isPrime:
                primes.append(count)

    for i in range (0, len(primes)):
        if m % primes[i] == 0:
            m_primes.append(primes[i])
        while m % primes[i] == 0:
            m /= primes[i]
    
    for j in range (0, len(primes)):
        if n % primes[j] == 0:
            n_primes.append(primes[j])
        while n % primes[j] == 0:
            n/= primes[j]

    print("The common prime divisor of these two numbers are: ", common_elements(n_primes,m_primes))
problem1()

#2.	Find the greatest common divider (GCD) of them
def problem2(a,b):
    if b==0:
        return a
    else:
        return problem2(b,a%b)
print(problem2(a,b))

#3.	Find the least common multiple (LCM) of them.
def problem3():
    return (a*b) / problem2(a,b)
print(problem3())
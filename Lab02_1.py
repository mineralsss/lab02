while True:
    try:
        num = int(input("Please input an interger: "))
        if num <= 5:
            print("Re-enter")
        else:
            break
    except ValueError:
        print("Please input an interger")
# 2.	S1 = 1 + 2 + 3 + ... + n.
def problem1():
    sum = 0
    for i in range(1, num+1):
        sum += i
    print(sum)
problem1()

#3.	S2 = n! 
def problem2():
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print(fact)
problem2()

#4.	S3 =1+1/2+1/3 +...+1/n .
def problem3():
    sum = 0
    for i in range(1, num+1):
        sum += 1/i
    print(sum)
problem3()

#5.	Re-input n. Check whether n is a prime number or not.
def problem4():
    prime = False
    while True:
        try:
            num = int(input("Please input an interger: "))
            if num <= 5:
                print("Re-enter")
            else:
                for i in range(2, num):
                    if num % i == 0:
                        prime = True
                        break
            if prime:
                print(num,"is not a prime")
            else:
                print(num,"is a prime")
            break
        except ValueError:
            print("Please input an interger")
     
problem4()
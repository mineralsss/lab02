while True:
    try:
        n = int(input("enter an integer n (n>1 and n<=9): "))
        if n <= 1 or n > 9:
            True
        else:
            break
    except ValueError:
        print("Please enter an interger")
for i in range(1,11):
    print(i," x ", n,"= ", n * i)




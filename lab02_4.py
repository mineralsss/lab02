while True:
    try:
        p = int(input("Input initial deposit ammount (>1.000.000): "))
        r = float(input("Input intrest rate (0 < intrest < 1): "))
        t = int(input("Input years: "))
        if t < 1:
            print("Please enter valid number of years")
        elif p < 1000000 or r < 0 or r > 1:
            print("Invalid deposit ammount or intrest rate")
        else:
            break
    except ValueError:
        print("Please enter a number")
def compoundIntrest(p, r, t, n):
    for period in range(1, t+1):
        amount = p*(pow((1+r/n), n*(period)))
        print('Period:', period, amount)
    return amount
compoundIntrest(p, r, t, 1)

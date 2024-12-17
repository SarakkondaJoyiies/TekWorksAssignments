initial_balance = float(input("Enter the initial balance (K0): "))
interest_rate = float(input("Enter the interest rate: "))

interest_rate = interest_rate / 100
current_balance = initial_balance
n = int(input("Enter the number of years: ")) 
year = 0 
print("\nYear :",year,"Capital = ",current_balance)

while year < n:
    year += 1
    current_balance += current_balance * interest_rate 
    print("Year :",year,"Capital = ",current_balance)

print("\nFinal capital after", n, "years is:", round(current_balance, 2))

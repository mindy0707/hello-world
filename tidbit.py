def main():
    price = float(input("Enter the purchase price: "))

    down_payment = price * 0.10
    balance = price - down_payment
    monthly_payment = price * 0.05
    rate = 0.12

    print("Month   Balance   Interest   Principal   Payment   New Balance")
    print("--------------------------------------------------------------")

    month = 1

    while balance > 0:
        interest = balance * (rate / 12)
        principal = monthly_payment - interest

        if principal > balance:
            principal = balance
            monthly_payment = interest + principal

        new_balance = balance - principal

        print(month, balance, interest, principal, monthly_payment, new_balance)

        balance = new_balance
        month += 1

main()

balance = 1000
withdrawal_amount = 1

amount = balance - withdrawal_amount

if withdrawal_amount <= balance:
    print(f"Success!Remaining balance: {amount}")
else:
    print("Insufficient funds")
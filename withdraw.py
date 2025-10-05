def withdraw(customers, name, pin, amount):
    for c in customers:
        if c["name"].lower() == name.lower() and c["pin"] == pin:
            if c["balance"] >= amount:
                c["balance"] -= amount
                print(f"\n ₹{amount} withdrawn successfully! Remaining: ₹{c['balance']}\n")
            else:
                print("\n Insufficient balance.\n")
            return
    print("\n Invalid credentials.\n")

def deposit(customers, name, pin, amount):
    for c in customers:
        if c["name"].lower() == name.lower() and c["pin"] == pin:
            c["balance"] += amount
            print(f"\n ₹{amount} deposited successfully! New balance: ₹{c['balance']}\n")
            return
    print("\n Invalid credentials.\n")

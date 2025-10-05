def check_balance(customers, name, pin):
    for c in customers:
        if c["name"].lower() == name.lower() and c["pin"] == pin:
            print(f"\n Current Balance: ₹{c['balance']}\n")
            return
    print("\n Invalid name or PIN.\n")

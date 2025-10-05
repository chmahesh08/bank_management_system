def transfer_money(customers, name, pin, receiver_name, amount):
    sender = receiver = None
    for c in customers:
        if c["name"].lower() == name.lower() and c["pin"] == pin:
            sender = c
        if c["name"].lower() == receiver_name.lower():
            receiver = c

    if not sender:
        print("\n Invalid sender credentials.\n")
        return
    if not receiver:
        print("\n Receiver not found.\n")
        return
    if sender["balance"] < amount:
        print("\n Insufficient balance.\n")
        return

    sender["balance"] -= amount
    receiver["balance"] += amount
    print(f"\n ₹{amount} transferred from {sender['name']} to {receiver['name']} successfully!\n")

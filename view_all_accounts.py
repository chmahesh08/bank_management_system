def view_all_accounts(customers):
    print("\n===== All Customer Accounts =====")
    print("{:<5} {:<15} {:<10}".format("ID", "Name", "Balance"))
    print("-" * 35)
    for c in customers:
        print("{:<5} {:<15} {:<10}".format(c["id"], c["name"], c["balance"]))
    print()

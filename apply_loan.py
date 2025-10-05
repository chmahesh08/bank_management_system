def apply_loan(loan_requests, customers, name, amount):
    for c in customers:
        if c["name"].lower() == name.lower():
            loan_requests.append({"customer_id": c["id"], "amount": amount, "status": "Pending"})
            print(f"\n Loan request for ₹{amount} submitted successfully!\n")
            return
    print("\n Customer not found.\n")

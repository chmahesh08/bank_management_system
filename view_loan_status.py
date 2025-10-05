def view_loan_status(loan_requests, customers, name):
    for c in customers:
        if c["name"].lower() == name.lower():
            print("\n===== Loan Status =====")
            found = False
            for req in loan_requests:
                if req["customer_id"] == c["id"]:
                    print(f"Amount: ₹{req['amount']} | Status: {req['status']}")
                    found = True
            if not found:
                print("No loan requests found.")
            print()
            return
    print("\n Customer not found.\n")

def view_loan_requests(loan_requests, customers):
    print("\n===== Loan Requests =====")
    pending = [req for req in loan_requests if req["status"] == "Pending"]
    if not pending:
        print("No pending loan requests.\n")
        return

    for req in pending:
        name = next(c["name"] for c in customers if c["id"] == req["customer_id"])
        print(f"Customer: {name}, Amount: ₹{req['amount']}, Status: {req['status']}")
    print()

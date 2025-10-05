def reject_loan(loan_requests, customer_id):
    for req in loan_requests:
        if req["customer_id"] == customer_id and req["status"] == "Pending":
            req["status"] = "Rejected"
            print("\n Loan request rejected.\n")
            return
    print("\n No pending loan found for that customer ID.\n")

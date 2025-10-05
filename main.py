from admin.admin_menu import admin_menu
from customer.customer_menu import customer_menu

customers = [
    {"id": 1, "name": "Mahesh", "balance": 5000, "pin": 1234, "loan_requests": []},
    {"id": 2, "name": "Upendar", "balance": 70000, "pin": 2345, "loan_requests": []},
    {"id": 3, "name": "Prabhas", "balance": 1000000, "pin": 3456, "loan_requests": []}
]

loan_requests = [
    {"customer_id": 1, "amount": 5000, "status": "Pending"},
    {"customer_id": 2, "amount": 10000, "status": "Pending"}
]

def main_menu():
    while True:
        print("\n===== Bank Management System =====")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin_menu(customers, loan_requests)
        elif choice == "2":
            customer_menu(customers, loan_requests)
        elif choice == "3":
            print("\n Thank you for using the Bank Management System!\n")
            break
        else:
            print("\n Invalid choice.\n")

if __name__ == "__main__":
    main_menu()

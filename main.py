from database import init_db
from manager import EmployeeManager

def main():
    init_db()  
    mgr = EmployeeManager()
    
    while True:
        print("\n--- EMPLOYEE MANAGEMENT SYSTEM ---")
        print("1. Add Employee")
        print("2. Fetch Employee by ID")
        print("3. Fetch All Active Employees")
        print("4. Update Employee")
        print("5. Delete Employee (Soft Delete)")
        print("6. Exit")
        
        choice = input("\nSelect an option (1-6): ")

        if choice == '1':
            name = input("Name: ")
            email = input("Email: ")
            dept = input("Department: ")
            sal = input("Salary: ")
            print(mgr.add_employee(name, email, dept, float(sal)))

        elif choice == '2':
            eid = input("Enter ID: ")
            print(mgr.fetch_by_id(eid))

        elif choice == '3':
            active_list = mgr.fetch_all_active()
            print("\nID | Name | Email | Dept | Salary | Status")
            for emp in active_list:
                print(emp)

        elif choice == '4':
            eid = input("Enter ID to update: ")
            n = input("New Name: ")
            e = input("New Email: ")
            d = input("New Dept: ")
            s = input("New Salary: ")
            print(mgr.update_employee(eid, n, e, d, float(s)))

        elif choice == '5':
            eid = input("Enter ID to soft delete: ")
            print(mgr.soft_delete(eid))

        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

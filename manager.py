from database import query_db
import sqlite3

class EmployeeManager:
    def add_employee(self, name, email, department, salary):
        try:
            query = "INSERT INTO employees (name, email, department, salary) VALUES (?, ?, ?, ?)"
            query_db(query, (name, email, department, salary))
            return f"\n Success: Employee '{name}' added."
        except sqlite3.IntegrityError:
            return "\n Error: This email already exists in the system."

    def fetch_by_id(self, emp_id):
        query = "SELECT * FROM employees WHERE id = ?"
        result = query_db(query, (emp_id,), fetchone=True)
        return result if result else "\n Error: Employee not found."

    def fetch_all_active(self):
        query = "SELECT * FROM employees WHERE status = 'ACTIVE'"
        return query_db(query, fetchall=True)

    def update_employee(self, emp_id, name, email, department, salary):
        # First check if employee exists
        if not self.fetch_by_id(emp_id): return "\n Error: Employee not found."
        
        try:
            query = "UPDATE employees SET name=?, email=?, department=?, salary=? WHERE id=?"
            query_db(query, (name, email, department, salary, emp_id))
            return "\n Success: Employee updated."
        except sqlite3.IntegrityError:
            return "\n Error: Could not update. Email might already be taken."

    def soft_delete(self, emp_id):
        query = "UPDATE employees SET status = 'INACTIVE' WHERE id = ?"
        query_db(query, (emp_id,))
        return f"\n Success: Employee ID {emp_id} marked as INACTIVE."

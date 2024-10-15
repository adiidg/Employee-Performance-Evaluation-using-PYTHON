# app.py
from data import Employee, PerformanceReview
from analytics import generate_performance_graph
import matplotlib.pyplot as plt

def main():
    employees = []
    reviews = []

    while True:
        print("\nEmployee Performance Evaluation System")
        print("1. Add Employee")
        print("2. Add Performance Review")
        print("3. View Employees")
        print("4. View Reviews")
        print("5. View Performance Analytics")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            name = input("Enter employee name: ")
            department = input("Enter employee department: ")
            employee = Employee(name, department)
            employees.append(employee)
            print(f"Employee {name} added.")

        elif choice == "2":
            if not employees:
                print("No employees available. Please add employees first.")
                continue
            
            for idx, emp in enumerate(employees):
                print(f"{idx + 1}. {emp.name} - {emp.department}")

            emp_index = int(input("Select employee by number: ")) - 1

            if emp_index < 0 or emp_index >= len(employees):
                print("Invalid selection.")
                continue

            score = float(input("Enter performance score (0-10): "))
            comments = input("Enter comments: ")
            review = PerformanceReview(employees[emp_index], score, comments)
            reviews.append(review)
            print("Performance review added.")

        elif choice == "3":
            print("\nEmployees:")
            for emp in employees:
                print(f"- {emp.name} | Department: {emp.department}")

        elif choice == "4":
            print("\nPerformance Reviews:")
            for review in reviews:
                print(f"{review.employee.name} | Score: {review.score} | Comments: {review.comments}")

        elif choice == "5":
            if not reviews:
                print("No performance reviews available for analytics.")
                continue
            
            generate_performance_graph(reviews)

        elif choice == "6":
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def display_menu(self):
        print("\nStudent Management System Menu:")
        print("1. Enter student details")
        print("2. Delete student details")
        print("3. Update student details")
        print("4. Display all students")
        print("5. Exit")

    def enter_details(self):
        name = input("Enter student name: ")
        phone_number = self.get_valid_phone_number()
        email = input("Enter student email id: ")
        address = input("Enter student address: ")

        student = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }

        self.students.append(student)
        print("Student details added successfully!")

    def get_valid_phone_number(self):
        while True:
            phone_number = input("Enter student phone number (10 digits): ")
            if phone_number.isdigit() and len(phone_number) == 10:
                return phone_number
            else:
                print("Invalid phone number. Please enter a 10-digit numeric value.")

    def delete_details(self):
        name = input("Enter student name to delete: ")

        for student in self.students:
            if student['name'] == name:
                self.students.remove(student)
                print("Student details deleted successfully!")
                return

        print("Student not found with the given name.")

    def update_details(self):
        name = input("Enter student name to update: ")

        for student in self.students:
            if student['name'] == name:
                student['phone_number'] = self.get_valid_phone_number()
                student['email'] = input("Enter updated email id: ")
                student['address'] = input("Enter updated address: ")
                print("Student details updated successfully!")
                return

        print("Student not found with the given name.")

    def display_all_students(self):
        if not self.students:
            print("No student details available.")
            return

        print("\nAll Student Details:")
        for student in self.students:
            print(f"Name: {student['name']}, Phone Number: {student['phone_number']}, "
                  f"Email: {student['email']}, Address: {student['address']}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.enter_details()
            elif choice == '2':
                self.delete_details()
            elif choice == '3':
                self.update_details()
            elif choice == '4':
                self.display_all_students()
            elif choice == '5':
                print("Exiting Student Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    student_system = StudentManagementSystem()
    student_system.run()

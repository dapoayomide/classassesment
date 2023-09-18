import mysql.connector

dapodb = mysql.connector.connect(

    host="localhost",
    user="root",
    password="1234",
    database="dapodb1"
)

cursor = dapodb.cursor()

class Student:

    def __init__(self, student_id, first_name, last_name, GPA):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.GPA = GPA
   
    def insert_student(self):
        try:

            insert = "INSERT INTO students (FirstName, LastName, GPA) VALUES (%s, %s, %s)"

            students_data = (self.student_id, self.first_name, self.last_name, self.GPA)

            cursor.execute(insert, students_data)

            dapodb.commit()

            print("Student has been added"
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")
           
    def get_student_by_id(self, student_id):
        try:
            getstudent = "SELECT id, FirstName, LastName, GPA FROM students WHERE id = %s"
            cursor.execute(getstudent, (student_id,))
            info = cursor.fetchone()
            if info:
                self.student_id, self.first_name, self.last_name, self.GPA = info
                print("Info retrieved successfully")
            else:
                print("Student id does not exist")
        except mysql.connector.Error as err:
            print(f"Error: {err}")    

    def update_gpa(self, new_gpa):
        try:
            update_gpa = "UPDATE students SET GPA = %s WHERE id = %s"
            cursor.execute(update_gpa, (new_gpa, self.student_id))
            dapodb.commit()
            print("Student GPA has been updated")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

database = Student(1, "Dapo", "Banjo", 4.0)


database.insert_student()

database.get_student_by_id(1)

database.update_gpa(3.5)  

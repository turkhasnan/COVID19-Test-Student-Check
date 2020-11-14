import sys 

class  StudentName:
    
    def _init_(self, first_name, last_name, student_id):
        
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        
    def info(self):
        
        print(f"{self.first_name} {self.last_name} {self.student_id}")

                         
if __name__ == "__main__":
    
    student = StudentName()
    print("Please enter the following:")
    print("First name:")
    student.first_name = input()
    print("Last name:")
    student.last_name = input()
    print("Student ID:")
    student.student_id = input()
    student.info()
                        

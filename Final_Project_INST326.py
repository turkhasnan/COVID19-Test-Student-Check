import sys 

class  Name:
    
    def _init_(self, first_name, last_name, id, covid):
        
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.covid = covid
        
    def info(self):
        
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"ID: {self.id}")
        print(f"Covid check: {self.covid}")

                         
if __name__ == "__main__":
    
    print("Are you a teacher or a student?")
    user_input = input()
    if user_input == "teacher":
        teacher = Name()
        print("Please enter the following:")
        print("First name:")
        teacher.first_name = input()
        print("Last name:")
        teacher.last_name = input()
        print("Teacher Code:")
        teacher.id = input()
        print("Have you done a Covid-19 check?")
        teacher.covid = input()
        teacher.info()
        
    else:
        student = Name()
        print("Please enter the following:")
        print("First name:")
        student.first_name = input()
        print("Last name:")
        student.last_name = input()
        print("Student ID:")
        student.id = input()
        print("Have you done a Covid-19 check?")
        student.covid = input()
        student.info()
    

                        

import sys 

class  Name:
     """gets input for information from a student
    
    Args:
    
    first_name(string): first name of student
    
    last_name(string): last name of student
    
    id(int): id number of the student
    
    covid(string): check whether or not a student has taken the covid 19 test
    
    """
    def _init_(self, first_name, last_name, id, covid):
         """initialize first and last name, id and covid check
        
        Args:
        
        first_name(string): first name of student
        
        last_name(string): last name of student
        
        id(int): id number of the student
        
        covid(string): check whether or not a student has taken the covid 19 test
        
        """
        
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.covid = covid
        
    def info(self):
        """prints out student id after its been input from the student 
        
        Args:
        
        """    
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"ID: {self.id}")
        print(f"Covid check: {self.covid}")

if __name__ == "__main__":

    student = Name()
    print("Please enter your first name:")
    student.first_name = input()
    print("Please enter your last name:")
    student.last_name = input()
    print("Have you done a Covid-19 check?")
    student.covid = input()
    if student.covid == "yes" or "y" or "Yes" or "Y":
        print("Student ID:")
        student.id = input()
        student.info()
    elif student.covid == "no" or "n" or "No" or "N":
        print("please take a covid 19 test before retrying. Thank you.")
                             
                   

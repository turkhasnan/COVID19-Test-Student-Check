
import sys
import random

class  Name:
    """gets input for information from a student
    
    Args:
    
        first_name(string): first name of student
    
        last_name(string): last name of student
    
        id(int): id number of the student
    
        covid(string): check whether or not a student has taken the covid 19 test
    
    """
    def _init_(self, first_name, last_name, id, covid, reason, room):
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
        self.reason = reason
        self.room = room
        
    
    def info(self):
        """prints out student id after its been input from the student 
        
        Args:
        
        """    
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"ID: {self.id}")
        print(f"Covid check: {self.covid}")
        print(f"reason: {self.reason}")
        print(f"room #: {self.room}")
        
        
def capacity(roomcap):
    """Checks the room capacity. If it is 20 people, then the room is full
    
    Parameters:
        roomcap: integer value that holds the amount of students in the room
        
    Side effect:
        After the message, the program quits.
    """
    if roomcap >= 21:
        print("Sorry, the room is full. Please try again and pick a different room.")
        quit()
   
        

if __name__ == "__main__":

    student = Name()
    roomcap1 = 0
    roomcap2 = 0
    roomcap3 = 0
    roomcap4 = 0
    
    # Name input
    student.first_name = input("Please enter your first name: ")
    print(" ")
    student.last_name = input("Please enter your last name: ")
    print(" ")
    
    # Covid Check ( will not advance if the answer is no)
    student.covid = input("Have you done a Covid-19 check (yes or no): ")
    
    if student.covid == "yes":
        print(" ")
        while True:
            student.id = int(input("Student ID: "))
            
            if len(str(student.id)) != 8 :
                print("Please try again")
            else:
                break
        
        int(student.id)
    elif student.covid == "no":
            print("***please take a covid 19 test before retrying. Thank you.***\n")
            quit()
    else:
        raise ValueError
    
    
    # reason input
    while True:
        print(" ")
        print("What is the reason for entering? \n 1) Teacher appointment \n or \n 2) lab time \n ")

        student.reason = int(input("please enter the number: "))
        
        if student.reason == 1:
            break
        elif student.reason == 2:
            break
        
        print(" ")
    
    # Room input option (once reason has been chosen you will be asked for the room of your choice). 
    # time slot is produced for user and given here
    if student.reason == 1:
        while True:
            student.room = int(input("which room would you like? 1 or 2: "))
            if student.room == 1:
                roomcap1 = roomcap1 + 1
                capacity(roomcap1)
                print("This is your alloted time: ")
                print(" ")
                break 
            elif student.room == 2:
                roomcap2 = roomcap2 + 1
                capacity(roomcap2)
                print("This is your alloted time: ")
                print(" ")
                break
    elif student.reason == 2:
        while True:
            student.room = int(input("which room would you like 3 or 4: "))
            if student.room == 3:
                roomcap3 = roomcap3 + 1
                capacity(roomcap3)
                print("This is your alloted time: ")
                print(" ")
                break
            elif student.room == 4:
                roomcap4 = roomcap4 + 1
                capacity(roomcap4)
                print("This is your alloted time: ")
                print(" ")
                break

            
    #building enter code
    randnum = random.randint(3000, 8000)
    print(f"Here is your building access code: {randnum}")
    
    #show info
    print(" ")
    student.info()

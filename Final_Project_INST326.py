import sys
import random
import time
import pandas as pd

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
    if roomcap >= 10:
        print("Sorry, the room is full. Please try again and pick a different room.")
        
   

def slots():

    timeslot1 = roomcount
    timeslot2 = random.randint(0,10)
    timeslot3 = random.randint(0,10)
    timeslot4 = random.randint(0,10)
    timeslot5 = random.randint(0,10)
    timeslot6 = random.randint(0,10)
    timeslot7 = random.randint(0,10)

    print("Time availibility:\n")
    
    print(f"1) 9:00 - 10:00: {timeslot1} students are here")
    print(f"2) 10:30 - 11:30: {timeslot2} students are here")
    print(f"3) 12:00 - 1:00: {timeslot3} students are here")
    print(f"4) 1:30 - 2:30: {timeslot4} students are here")
    print(f"5) 3:00 - 4:00: {timeslot5} students are here")
    print(f"6) 4:30 - 5:30: {timeslot6} students are here")
    print(f"7) 6:00 - 7:00: {timeslot7} students are here\n")
    
    timeslot = input("Please enter the number of time slot that you would like: ")
    
    if timeslot == "1":
        capacity(timeslot1)
        timeslot1+=1
        print(" ")
        print("Your time is set to 9:00 to 10:00")

    elif timeslot == "2":
        capacity(timeslot2)
        timeslot2 += 1
        print(" ")
        print("Your time is set to 10:30 to 10:00")

    elif timeslot == "3":
        capacity(timeslot3)
        timeslot3 += 1
        print(" ")
        print("Your time is set to 12:00 to 1:00")

    elif timeslot == "4":
        capacity(timeslot4)
        timeslot4 += 1
        print(" ")
        print("Your time is set to 1:30 to 2:30")

    elif timeslot == "5":
        capacity(timeslot5)
        timeslot5 += 1
        print(" ")
        print("Your time is set to 3:00 to 4:00")

    elif timeslot == "6":
        capacity(timeslot6)
        timeslot6 += 1
        print(" ")
        print("Your time is set to 4:30 to 5:30")

    elif timeslot == "7":
        capacity(timeslot7)
        timeslot7 += 1
        print(" ")
        print("Your time is set to 6:00 to 7:00")

    else:
        print("*****please pick a number between 1 and 7*****")



        
if __name__ == "__main__":
    student = Name()
    roomcap1 = 0
    roomcap2 = 0
    roomcap3 = 0
    roomcap4 = 0
    
    df = pd.read_csv("roomcapacity.csv")
    roomcount = len(df["Name"])
    
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
        student.reason = int(input("Please enter the 1 or 2: "))
        print(" ")
        
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
            print(" ")
            if student.room == 1:
                roomcap1 = roomcap1 + 1
                capacity(roomcap1)
                slots()
                print(" ")

                break 
            elif student.room == 2:
                roomcap2 = roomcap2 + 1
                capacity(roomcap2)
                slots()
                print(" ")
                break
    elif student.reason == 2:
        while True:
            student.room = int(input("which room would you like 3 or 4: "))
            print(" ")
            if student.room == 3:
                roomcap3 = roomcap3 + 1
                capacity(roomcap3)
                slots()
                print(" ")
                break
            elif student.room == 4:
                roomcap4 = roomcap4 + 1
                capacity(roomcap4)
                slots()
                print(" ")
                break
    #building enter code
    randnum = random.randint(3000, 8000)
    print(f"Here is your building access code: {randnum}")

    #Show info
    print(" ")
    student.info()

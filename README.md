# COVID 19 TEST STUDENT CHECK

This code makes students, who want to gain access to the USG buildings, confirm whether they've gotten a COVID19 Test. The code will check if the student has taken a covid 19 test. If they have, then they may continue. If they do not, then the code will prompt them to take it and the code will end. If the student has taken it, then the code will ask for there student ID. This ID has to be at least 8 numbers long or else it will need to be put in again. If the ID is correct ( 8 digits ), then the the code will continue and ask what is the reason for entering the building. The code will display two reasons: either for lab time or to meet a professor. The user will have to enter either 1 or 2, or the code will not continue. After, the code will ask which room the student would like to be in. The student will have to then choose the room number and enter that number to continue. The time slots availible for that room and will be displayed. If that timeslot for the room has more than 10 students, then the student will not be allowed to enter that room. If it is below 10, then that time will be their timeslot to go into the USG building. A csv file is read in to determine how many people are in a certain time slot. Please also download this file in order to have that room information. The code will then display all the information entered and it will end. 


### For the code to run you will need to install the pandas module 

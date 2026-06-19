"""
PROGRAMMER NAME: Kamohelo Kotelo
START DATE: 03/06/2026 (10:19 AM)
PROGRAM PURPOSE: To develop a Python application for the Learner Progress Tracking 
System
END DATE: 10/06/2026 (9:45 AM)
"""
from tkinter import messagebox
import tkinter as tk 
root = tk.Tk()
root.withdraw()
root.wm_attributes("-topmost", 1)
root.lift()

# Global variables, all_learners variable to store the leaners and person is a temporary 
# to asign Learner Object later
all_learners = []
person = None

# Create 5 global functions captureMarks(), recursiveSum(), calculateAverage(), 
# learnerSummary() and searchLearnerID()
def captureMarks(mark):
    try:
       # We ask the user to enter a the amount of marks they want to enter
       marks_amount = int(input("How many marks do you want to enter?: ").strip())
    except ValueError:
       print("Please add a number.")
       return None
              
    # We are looping to the amount of marks the user enters
    for i in range(marks_amount):
        try:
           # Then we ask the user to enter the marks
           the_marks = int(input(f"Enter mark {i+1}: ").strip())
        except ValueError:
            print("Please enter a number value.")
            
        # We want to make show the the marks being entered are not 0 and 100
        if the_marks < 0 or the_marks > 100:
            print("Please enter number between 0 and 100")
            continue
        # After all the marks have been entered we append the marks to the Learners object
        mark.marks.append(the_marks)
    
    messagebox.showinfo("Success", "Marks captuerd successfully.")
    
    
# This recursive function calculates the sum of a learner's marks
def recursiveSum(marks_list, index=0): # Inside the argument of the function we collect 
    # the marks list of the students eg. [56,64,70] and set the index the postion of the values 
    # in the list to 0.
    # if the index finally reaches the length of the list we return 0 to stop 
    if index == len(marks_list):
        return 0
    else: # If not we keep on addomg the sum of the learners marks
        return marks_list[index] + recursiveSum(marks_list, index + 1)
    
# This function calculated the average 
def calculateAverage(learner_average): # We capture the specific learner in the argument
    if len(learner_average.marks) == 0: # We check if the length of the learners marks == 0 
        # simply return 0 and discontinue
        return 0
    else:
        # We use the recursiveSum function to calculate the total sum of the learners marks
        total_sum = recursiveSum(learner_average.marks)
        # Then we divied the sum of learners markers with the length of the learners marks 
        # to get the average
        calculated_avg = total_sum / len(learner_average.marks)
        # Then we return the calculated average
        return calculated_avg

# In this function we are collecting the learner summary
def learnerSummary():
    # We check if the are no learners before we can do summary
    if len(all_learners) == 0:
        print("Please add learners.")
    
    else:
        # We check for learner in all learners then calculate their average
        for learner in all_learners:
            learner_avg = calculateAverage(learner)
            # We use if else statement to check their results
            if learner_avg < 50:
                learner_status = "Fail"
            elif learner_avg >= 50 and learner_avg <= 74:
                learner_status = "Pass"
            else:
                learner_status = "Pass with distinction"
            if learner_avg >= 50:
                certificate_status = "Yes"
            else:
                certificate_status = "No"
            
            # Then we print out the learner summary 
            print("------ Learner Summary ------")
            print("Learner ID: " + learner.learner_id)
            print("Name: " + learner.name)
            print("Age: " + str(learner.age))
            print("Course: " + learner.course)
            print("Marks: " + str(learner.marks))
            print("Average: " + str(learner_avg))
            print("Result: " + learner_status) 
            print("Certificate: " + certificate_status)
    
# This function searches for the learner ID 
def searchLearnerID():
    # We ask the user to enter the ID to search for the learner 
    search_learner = input("Enter learner ID to search: ")
    # Then we loop through all learners to see if they have that specific learner id to return it
    for learner in all_learners:
        if learner.learner_id == search_learner:
            return learner 
    # Other wise we return nothing
    return None
    
# Create a base class of Person with two attributes of name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
# Create a class called Learner with 5 starting attributes, learnerID, name, age and marks
class Learner(Person): # 7. Make Learner Inherit from base class Person
    def __init__(self, learner_id, name, age, course):
        # Remove the previous attributets of name and age and replace them with the 
        # inherited ones using super().__init__
        """
        self.name = name
        self.age = age
        
        """
        super().__init__(name, age)
        self.learner_id = learner_id
        self.course = course
        self.marks = []
        
        # Create Encapsulated values for average mark and learner status
        self.__average_mark = 0
        self.__learner_status = "Pass"
        
    # To use the encapsulated attributes we have to use methods getters and setters
    def getAverage(self):
        return self.__average_mark
    
    def setAverage(self, value):
     self.__average_mark = value
        
    def getStatus(self):
        return self.__learner_status
    
    def setStatus(self, value):
     self.__learner_status = value
        
        
    # Create a new add learners method function 
    def addLearners(self):
        # We open a fill called students.txt so all our learners can stay in our device and use 
        # "a" to append them
        file = open("students.txt", "a")
        # Then we write them inside the file 
        file.write(str(self.learner_id) + "\n")
        file.write(self.name + "\n")
        file.write(str(self.age) + "\n")
        file.write(self.course + "\n")
        # We close the file after we are done
        file.close() 
        
    # Create a view learners details method function 
    def viewLearnerDetails(self):
        # We print the learners details 
        print("------ Learner Summary ------")
        print("Learner ID: " + self.learner_id)
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Course: " + self.course)
        print("Marks: " + str(self.marks))
        
        # We assign the encapusled value to the calculate average function 
        self.__average_mark = calculateAverage(self)
        
        # Then use if else statment to see if a learners has passed or failed
        if self.__average_mark < 50:
            self.__learner_status = "Fail"
        elif self.__average_mark >= 50 and self.__average_mark <= 74:
            self.__learner_status = "pass"
        else:
            self.__learner_status = "Pass with distinction"
        
        print("Average: " + str(self.getAverage()))
        print("Result: " + str(self.getStatus()))
        
        # We check if the average is more the 50 or 50 so we can hand the certificate
        if self.getAverage() >= 50:
            print("Certificate: Yes")
        else:
            print("Certificate: No")
        
        
    # Create an update learner details methods function
    def updateLearnerDetails(self):
        # Create new variables 
        new_name = input("Enter new name: ")
        new_age = int(input("Enter new age: "))
        new_course = input("Enter new course: ")
        # The we re-assing the new details to the old ones
        self.name = new_name
        self.age = new_age
        self.course = new_course
        
        messagebox.showinfo("Success", "Learner details updated successfully.")

        
    # Create a remove learner methods function
    def removeLearner(self):
        # We ask the user to confirm if they really want to delete learner
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to remove {self.name}?")
        if confirm:
          return True
        else:
          return False

# To track the users choice 
choice_input = ""
# We use a while loop to run the program 
while choice_input != "8": # Here we are saying if the user doesn't choose 8 we can 
    # continue the program and dispaly the menu
    # We print all the options that exist
    print("===== Learner Progress Tracking System =====")
    
    print("\n1. Add learner")
    print("\n2. Enter marks")
    print("\n3. View all learners")
    print("\n4. Search learner")
    print("\n5. Update learner")
    print("\n6. Remove leaner")
    print("\n7. Show learner result")
    print("\n8. Exist")
    
    # We ask the user to choose an option
    choice_input = input("Enter your input: ")
    # If they choose the number 1 to enter we ask them to enter all the values to add learner
    if choice_input == "1":
        learner_ID = input("Enter learner ID: ").strip()
        learner_name = input("Enter learner name: ").strip()
        learner_age = int(input("Enter learner age: ").strip())
        learner_course = input("Enter course name: ").strip()
        # The we pass those values into an object
        person = Learner(learner_ID, learner_name, learner_age, learner_course)
        # then we add the learners by access the add learners method
        person.addLearners()
        # then we appended the new added learners inside the all_learners = [] variable 
        all_learners.append(person)
        messagebox.showinfo("Success", "Learner added succesfully.")
    
    # Option 2 is for them to enter marks for the learner 
    elif choice_input == "2":
        # We first check if the learner ID exists if not we tell the user the learner is not found
        get_learner = searchLearnerID()
        if get_learner is None:
            print("Learner ID not found")
        else:
            # Then we capture the marks
            captureMarks(get_learner)
    
    # This options asks the user to display the summary of learner 
    elif choice_input == "3":
        # We call the learner summary function
        learnerSummary()
    
    # Option 4 serachers for the learner 
    elif choice_input == "4":
        # We assign get learner to the searchLearnerID function
        get_learner = searchLearnerID()
        # If the learner ID exist then we view the learner Details otherwise we tell the user 
        # that the ID entered does not match
        if get_learner is not None:
            get_learner.viewLearnerDetails()
        else:
            print("Entered ID does not Match Learner ID")
    
    # Option 5 updates learner details 
    elif choice_input == "5":
        # We first search for the learner
        get_learner = searchLearnerID()
        if get_learner is None:
          print("Learner ID not found")
        else:
          # If learner is found we show their details
          get_learner.updateLearnerDetails()
    
    # Option 6 removes a learner 
    elif choice_input == "6":
        # Once again we search for the learner ID
        get_learner = searchLearnerID()
        if get_learner is None:
            print("Learner ID not found")
        else:
            # then if the learner ID is foun we remove them inside the all_learners = [] using the 
            # remove method
            if get_learner.removeLearner() == True:
                all_learners.remove(get_learner)
                messagebox.showinfo("Success", "Learner removed successfully.")
    
    # We display learner results only with option 7
    elif choice_input == "7":
        get_learner = searchLearnerID()
        if get_learner is None:
            print("Learner ID not found")
        else:
           # We use setters and getters to calculate the value
           get_learner.setAverage(calculateAverage(get_learner)) # here we check for the learners average 
           # Then we check if they have passed or failed
           if get_learner.getAverage() < 50:
             get_learner.setStatus("Fail")
           elif get_learner.getAverage() >= 50 and get_learner.getAverage() <= 74:
             get_learner.setStatus("Pass")
           else:
            get_learner.setStatus("Pass with distinction")
           # We then print the values we need to find
           print("Result for: " + get_learner.name)
           print("Average: " + str(round(get_learner.getAverage(), 2)))
           print("Performance: " + get_learner.getStatus())
           print("")
           if get_learner.getAverage() >= 50:
             messagebox.showinfo("Result", get_learner.name + " qualifies for a certificate.")
           else:
             messagebox.showinfo("Result", get_learner.name + " does not qualify for a certificate.")

                
    # Option 8 allows us to get out of the prgroam
    elif choice_input == "8":
        confirm_exit = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm_exit == True:
            print("Thank you for using the system. Goodbye!")
            break
        else:
         choice_input = ""
                           
        
            
"""
REFERENCES:

Python Simplified (2021) Recursion Simply Explained with Code Examples - Python for Beginners. 
Available at: https://www.youtube.com/watch?v=m1Fjdnj_Mds : This video help me understand recursion a bit more.
This website was an excellent recourse to help me remember how to use classes and methods and control structures: 
https://www.w3schools.com/python/python_class_init.asp
https://www.w3schools.com/python/python_file_write.asp
https://www.w3schools.com/python/python_encapsulation.asp
https://www.w3schools.com/python/python_arrays.asp

Needed to understand a bit more on getters and setters so i did read here:
https://www.geeksforgeeks.org/python/getter-and-setter-in-python/   
"""          
            
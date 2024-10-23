from tkinter import *
from tkinter import ttk

# Initializing Variables
highscore = 0.0             # To make it easier to compare the percentages, I'm making these numbers 'float' types
lowscore = 100.0            
students = []               # This list will store every dictionary record of each student info
studentnames = []           # This list will store every name of each student for the dropbox
f1 = []                     # This list will store everything in the text file for dissection

# Functions
def openFile():             # A function that will sort the text file content into reusable and mutable versions.
    
    students.clear()        # .clear() is used to remove everything inside a list type variable
    studentnames.clear()    # This is used to prevent duplicates from adding to the lists after functions are run.

    with open("studentMarks.txt") as f1:
        data = f1.readlines()[1:]           # readlines()[1:] will start reading from the second line of the .txt
                                            # and onwards
    
        for line in data:
            studentdata = { 
                           "Name" : "",
                           "ID" : "",
                           "CourseTotal" : "",          # This essentially works as a blueprint for every instance of 
                           "ExamMark" : "",             # student info read from data, it will be stored accordingly
                           "PercentTotal" : "",         # to their 'keys' (category).
                           "Grade" : "",
                           }
        
            j = line.split(",")             # Any characters after a comma will be treated as a separate 'item'
            
            studentdata["Name"] = j[1]
            studentdata["ID"] = j[0]
            studentdata["CourseTotal"] = str(int(j[2]) + int(j[3]) + int(j[4]))
            studentdata["ExamMark"] = j[5]
            
            percenttotal = ((int(studentdata["CourseTotal"]) + int(j[5])) / 160)*100
            # The reason percenttotal does not have a string concatenation unlike 'CourseTotal's is so that
            # the function getValues() can start comparing the float percentages with float numbers, otherwise it'll be an error
            
            studentdata["PercentTotal"] = round(percenttotal, ndigits=1) # round() is a function that rounds decimals to a specified number
            studentdata["Grade"] = gradeSystem(percenttotal)
    
            students.append(studentdata)    # Once done assigning dictionary type infos, added to a huge masterlist


def getValues():                    # This will decide the values for the highest/lowest scores + names for dropbox.
    
    global highscore, lowscore                      # global variables are used to declare 
    
    for studentdata in students:                    # The only way this could work is if the dictionaries have been created
        studentnames.append(studentdata["Name"])    # Therefore, calling them by 'key' to add every name can be possible

        if float(studentdata["PercentTotal"]) > highscore:      # If the current percentage total is higher/lower, that will replace the
            highscore = studentdata["PercentTotal"]             # highscore/lowscore variable, and will do so everytime the loop happens
                                                                # until it has compared every percentage value
        if float(studentdata["PercentTotal"]) < lowscore:   
            lowscore = studentdata["PercentTotal"]
    
    
def gradeSystem(percentages):       # A simple function that returns the specific grade once a percentage condition is met
    
    if percentages >= 70:
        grade = "A"
    
    elif percentages >= 60 and percentages <= 69:
        grade = "B"
    
    elif percentages >= 50 and percentages <= 59:
        grade = "C"
    
    elif percentages >= 40 and percentages <= 49:
        grade = "D"
    
    else:
        grade = "F"
        
    return grade


def allRecords(txtarea):            # A function that concerns with printing out every information of the students
    
    txtarea.delete("1.0", "end")    # the delete() function prevents duplicates from being entered in the display field
    count = 0                       # count variable to count how many students there are
    totalpercentages = 0            # totalpercentages to find the median percentage between students
    
    for i in students:
            printLayout(i["Name"], i["ID"], 
                        i["CourseTotal"], i["ExamMark"], 
                        i["PercentTotal"], i["Grade"], txtarea)
            txtarea.insert(END,"\n・ ・ ・ ・ ・\n")
            count += 1
            totalpercentages += i["PercentTotal"]
    
    txtarea.insert(END, f"Number of students in class: {count} \n")
    txtarea.insert(END, f"Average percentage of marks: {totalpercentages/count}% \n")
    

def oneRecord(txtarea,names):       # A function that will find a student's info using the name given in the dropbox
    
    txtarea.delete("1.0", "end")
    
    userpick = names.get()          # Once the button is pressed, the dropdown menu will obtain the name--
                                    # And start comparing it with the names inside the students list/database
                                    
    for i in range(len(students)):
        if students[i]["Name"] == userpick:
            printLayout(students[i]["Name"], students[i]["ID"], 
                        students[i]["CourseTotal"], students[i]["ExamMark"], 
                        students[i]["PercentTotal"], students[i]["Grade"], txtarea)


def highestScore(txtarea):          # A function that will find the student's info with the highest score
    
    txtarea.delete("1.0", "end")
    
    for i in range(len(students)):
        if students[i]["PercentTotal"] == highscore: # The highscore variable is used as a reference to find the contents
            printLayout(students[i]["Name"], students[i]["ID"], 
                        students[i]["CourseTotal"], students[i]["ExamMark"], 
                        students[i]["PercentTotal"], students[i]["Grade"], txtarea)


def lowestScore(txtarea):            # A function that will find the student's info with the highest score
    
    txtarea.delete("1.0", "end")
    
    for i in range(len(students)):
        if students[i]["PercentTotal"] == lowscore:
            printLayout(students[i]["Name"], students[i]["ID"], 
                        students[i]["CourseTotal"], students[i]["ExamMark"], 
                        students[i]["PercentTotal"], students[i]["Grade"], txtarea)
         
            
def printLayout(nameinstance,IDinstance,courseinstance,markinstance,percentinstance,gradeinstance,txtarea):
    # A function made purely to make things easier, this is a layout that can be reusable 
    # in order to prevent repeating txtarea.insert when needing to display anything
    
    txtarea.insert(END,"Name: " + nameinstance + "\n")
    txtarea.insert(END,"Number: " + IDinstance + "\n")
    txtarea.insert(END,"Coursework Total: " + courseinstance + "\n")
    txtarea.insert(END,"Exam Mark: " + markinstance)
    txtarea.insert(END,"Overall Percentage: " + str(percentinstance) + "% \n")
    txtarea.insert(END, "\nGrade: " + gradeinstance + "\n")


def mainMenu():     # Main menu displays all the buttons, fields and labels with the responsive functions.
    
    openFile()
    getValues()
    
    names = StringVar()
    
    title = Label(mainwindow, text = "STUDENT MANAGER", font = "Arial 32 bold", bg = "#141211", fg = "white")
    title.place(relx = 0.5, rely = 0.15, anchor = CENTER)
    
    b1 = Button(mainwindow, text = "View All Records", font = "Corbel 12", bg = "#dbc15a", width = 16,
                bd = 0, command = lambda: allRecords(txtarea))
    b1.place(relx = 0.25, rely = 0.3, anchor = CENTER)
    
    b2 = Button(mainwindow, text = "Show Highest Score", font = "Corbel 12", bg = "#dbc15a", width = 16, 
                bd = 0, command = lambda: highestScore(txtarea))
    b2.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    
    b3 = Button(mainwindow, text = "Show Lowest Score", font = "Corbel 12", bg = "#dbc15a", width = 16,
                bd = 0, command = lambda: lowestScore(txtarea))
    b3.place(relx = 0.75, rely = 0.3, anchor = CENTER)
    
    sen1 = Label(mainwindow, text = "Individual Student Records:", font = "Corbel 13", bg = "#141211", fg = "white")
    sen1.place(relx = 0.28, rely = 0.385, anchor = CENTER)
    
    records = ttk.Combobox(mainwindow, width = 25, textvariable = names)
    records['values'] = studentnames
    records.place(relx = 0.55, rely = 0.385, anchor = CENTER)
    
    b4 = Button(mainwindow, text = "View Record", font = "Corbel 12", bg = "#dbc15a", width = 12, 
                bd = 0, command = lambda: oneRecord(txtarea, names))
    b4.place(relx = 0.775, rely = 0.385, anchor = CENTER)
    
    txtarea = Text(mainwindow)
    txtarea.place(relx = 0.5, rely = 0.7, anchor = CENTER, height = 300, width = 500)
    
    scrollV = Scrollbar(mainwindow, orient = "vertical")
    scrollV.place(relx = 0.85, rely = 0.7, anchor = CENTER, height = 300)
    # Adding the scrollbar
    
    scrollV.config(command = txtarea.yview)
    txtarea.config(yscrollcommand = scrollV.set)
    
mainwindow = Tk()
mainwindow.title("Student Manager")
mainwindow.geometry("700x600")
mainwindow.resizable(0,0)
mainwindow.config(bg = "#141211")

mainMenu()

mainwindow.mainloop()

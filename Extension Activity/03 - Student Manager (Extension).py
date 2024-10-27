from tkinter import *
from tkinter import ttk

"""
UPDATE
"""

highscore = 0.0             
lowscore = 100.0            
students = []              
studentnames = []           

mainwindow = Tk()
mainwindow.title("Student Manager 2.0")
mainwindow.geometry("700x700")
mainwindow.resizable(0,0)
mainwindow.config(bg = "#141211")


options = ['Ascending', 'Descending']

def deleteItems():
    # A function to reset the contents displayed on a tkinter window
    for item in mainwindow.winfo_children():
        item.destroy()


def openFile(): 

    students.clear()       
    studentnames.clear()

    count = 1

    with open("studentMarks.txt") as f1:
        data = f1.readlines()[1:]
    
        for line in data:
            # No. is a new dictionary key added for each student record, this 
            # will be helpful in accessing records since it will be easier to 
            # compare user options/index lines of a text file to the 'index' of 
            # each student record
            studentdata = { "No." : "",
                           "Name" : "",
                           "ID" : "",
                           "CourseTotal" : "",          
                           "ExamMark" : "",            
                           "PercentTotal" : "",        
                           "Grade" : "",
                           }
        
            j = line.split(",")
            
            studentdata["No."] = count
            
            studentdata["Name"] = j[1]
            studentdata["ID"] = j[0]
            studentdata["CourseTotal"] = str(int(j[2]) + int(j[3]) + int(j[4]))
            studentdata["ExamMark"] = j[5]
            
            percenttotal = ((int(studentdata["CourseTotal"]) + int(j[5])) / 160)*100
            
            studentdata["PercentTotal"] = round(percenttotal, ndigits=1) 
            studentdata["Grade"] = gradeSystem(percenttotal)
    
            students.append(studentdata)
            count += 1


def getValues():                
    
    global highscore, lowscore                     
    
    for studentdata in students:                   
        studentnames.append(studentdata["Name"])   

        if float(studentdata["PercentTotal"]) > highscore:     
            highscore = studentdata["PercentTotal"]            
                                                              
        if float(studentdata["PercentTotal"]) < lowscore:   
            lowscore = studentdata["PercentTotal"]
    
    
def gradeSystem(percentages):       
    
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


def allRecords(txtarea):           
    
    txtarea.delete("1.0", "end")   
    count = 0                      
    totalpercentages = 0           
    
    for i in students:
            printLayout(i["Name"], i["ID"], 
                        i["CourseTotal"], i["ExamMark"], 
                        i["PercentTotal"], i["Grade"], txtarea)
            txtarea.insert(END,"\n・ ・ ・ ・ ・\n")
            count += 1
            totalpercentages += i["PercentTotal"]
    
    txtarea.insert(END, f"Number of students in class: {count} \n")
    txtarea.insert(END, f"Average percentage of marks: {round((totalpercentages/count), ndigits = 1)}% \n")
    

def oneRecord(txtarea, names):      
    
    txtarea.delete("1.0", "end")
    
    userpick = names.get()          
                                    
    for i in range(len(students)):
        if students[i]["Name"] == userpick:
            printLayout(students[i]["Name"], students[i]["ID"], 
                        students[i]["CourseTotal"], students[i]["ExamMark"], 
                        students[i]["PercentTotal"], students[i]["Grade"], txtarea)

def highestScore(txtarea):        
    
    txtarea.delete("1.0", "end")
    
    for i in range(len(students)):
        if students[i]["PercentTotal"] == highscore: 
            printLayout(students[i]["Name"], students[i]["ID"], 
                        students[i]["CourseTotal"], students[i]["ExamMark"], 
                        students[i]["PercentTotal"], students[i]["Grade"], txtarea)

def lowestScore(txtarea):          
    
    txtarea.delete("1.0", "end")
    
    for i in range(len(students)):
        if students[i]["PercentTotal"] == lowscore:
            printLayout(students[i]["Name"], students[i]["ID"], 
                        students[i]["CourseTotal"], students[i]["ExamMark"], 
                        students[i]["PercentTotal"], students[i]["Grade"], txtarea)
         

def sortData(txtarea, options):
    # A function that will sort a list in ascending order or descending order
    # (Alphabetical wise and reverse alphabetical) if the sort option chosen was
    # either ascending or descending.
    
    txtarea.delete("1.0", "end")
    
    sortoption = options.get() 
    
    if sortoption == "Ascending":
        alist = sorted(students, key = lambda x: x["Name"])
        
        for i in alist:
            printLayout(i["Name"], i["ID"], 
                        i["CourseTotal"], i["ExamMark"], 
                        i["PercentTotal"], i["Grade"], txtarea)
            txtarea.insert(END,"\n・ ・ ・ ・ ・\n")
            
        
    elif sortoption == "Descending":
        dlist = sorted(students, key = lambda x: x["Name"], reverse = True)
        
        for i in dlist:
            printLayout(i["Name"], i["ID"], 
                        i["CourseTotal"], i["ExamMark"], 
                        i["PercentTotal"], i["Grade"], txtarea)
            txtarea.insert(END,"\n・ ・ ・ ・ ・\n")


def addStudent():
    # A function that will display the menu that will obtain the neccessary 
    # details for a student record from the user
    
    deleteItems()
    
    name = StringVar()
    idnum = StringVar()
    mark1 = StringVar()
    mark2 = StringVar()
    mark3 = StringVar()
    exammark = StringVar()
    
    title2 = Label(mainwindow, text = "ADD STUDENT", font = "Arial 32 bold", bg = "#141211", fg = "white")
    title2.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    
    label = Label(mainwindow, text = "Name:", font = "Corbel 13", bg = "#141211", fg = "white")
    label.place(relx = 0.25, rely = 0.25, anchor = W)
    prompt = Entry(mainwindow, textvariable = name, width = 20, font = "Corbel 13", bd=3)
    prompt.place(relx = 0.6, rely = 0.25, anchor = CENTER)

    label2 = Label(mainwindow, text = "ID:", font = "Corbel 13", bg = "#141211", fg = "white")
    label2.place(relx = 0.25, rely = 0.35, anchor = W)
    prompt2 = Entry(mainwindow, textvariable = idnum, width = 20, font = "Corbel 13", bd=3)
    prompt2.place(relx = 0.6, rely = 0.35, anchor = CENTER)
    
    label3 = Label(mainwindow, text = "Course Marks 1: ", font = "Corbel 13", bg = "#141211", fg = "white")
    label3.place(relx = 0.25, rely = 0.45, anchor = W)
    prompt3 = Entry(mainwindow, textvariable = mark1, width = 20, font = "Corbel 13", bd=3)
    prompt3.place(relx = 0.6, rely = 0.45, anchor = CENTER)
    
    label4 = Label(mainwindow, text = "Course Marks 2: ", font = "Corbel 13", bg = "#141211", fg = "white")
    label4.place(relx = 0.25, rely = 0.55, anchor = W)
    prompt4 = Entry(mainwindow, textvariable = mark2, width = 20, font = "Corbel 13", bd=3)
    prompt4.place(relx = 0.6, rely = 0.55, anchor = CENTER)
    
    label5 = Label(mainwindow, text = "Course Marks 3: ", font = "Corbel 13", bg = "#141211", fg = "white")
    label5.place(relx = 0.25, rely = 0.65, anchor = W)
    prompt5 = Entry(mainwindow, textvariable = mark3, width = 20, font = "Corbel 13", bd=3)
    prompt5.place(relx = 0.6, rely = 0.65, anchor = CENTER)
    
    label6 = Label(mainwindow, text = "Exam Marks: ", font = "Corbel 13", bg = "#141211", fg = "white")
    label6.place(relx = 0.25, rely = 0.75, anchor = W)
    prompt6 = Entry(mainwindow, textvariable = exammark, width = 20, font = "Corbel 13", bd=3)
    prompt6.place(relx = 0.6, rely = 0.75, anchor = CENTER)
    
    submit = Button(mainwindow, text = "Submit", font = "Corbel 15", bg = "#dbc15a", bd = 0,
                    width = 15, command = lambda: addInfo(name,idnum,mark1,mark2,mark3,exammark))
    submit.place(relx = 0.35, rely = 0.875, anchor = CENTER)
    
    back = Button(mainwindow, text = "Back", font = "Corbel 15", bg = "#dbc15a", bd = 0,
                    width = 15, command = lambda: mainMenu())
    back.place(relx = 0.65, rely = 0.875, anchor = CENTER)
        

def addInfo(name,idnum,mark1,mark2,mark3,exammark):
    # This function gets all the input from the user and assigns the data
    # to corresponding variables + 'cleansing' the desired input from any data
    # type impurities.
    
    name = name.get()
    idnum = idnum.get()
    mark1 = mark1.get()
    mark2 = mark2.get()
    mark3 = mark3.get()
    exammark = exammark.get()
    
    name = stringCleanse(name)
    idnum = idCleanse(idnum)
    mark1 = courseMarkCleanse(mark1)
    mark2 = courseMarkCleanse(mark2)
    mark3 = courseMarkCleanse(mark3)
    exammark = examMarkCleanse(exammark)
    
    # After this is done the append command is used to add the new record
    # to the last line of the text file
    
    with open("studentMarks.txt", "a") as f1:
        f1.write(str(idnum) + "," + name + "," + str(mark1) + "," + str(mark2) + "," 
                 + str(mark3) + "," + str(exammark) + "\n")
        
    mainMenu()
 

def idCleanse(idnum):    
    # A function that will keep the id in a certain length 
    check = True
    length = len(idnum)
    
    while check == False:
    # Loops until idnum is a reasonable length

        if length > 4:
            idnum = idnum[:-1]
            length = len(idnum)
            idnum = "".join(c for c in idnum if length.isdigit())
            # .isdigit() checks for all the integer values in the string
            # and will only keep them (ignores special characters and letters).
            # the .join will add those that satisfy the condition, (meaning:
            # that if a character contains an integer, add it to the idnum var)

        else:
            check = True
            
    return idnum
    
    
def stringCleanse(string):
    # A function that will keep the string variables a certain length in order
    # to prevent the program from breaking and to only allow letters in the
    # variable
    
    check = False
    length = len(string)

    while check == False:
    
        if length > 25:
            string = string[:-1]
            # start deleting the last character if the length still exceeds limit
            length = len(string)
            string = "".join(c for c in string if c.isalpha())
            # .isalpha() is a function to check if the character(s) are a letter
            # or not
        else:
           check = True
           
    return string


def courseMarkCleanse(integer):
    # A function that keeps the course marks in a limit (if exceeded will reset
    # the value) and removes data type impurities from the input
    
    integer = list(filter(lambda x: x.isdigit(), integer.split()))
    integer = sum([int(s) for s in integer])
    
    if integer >= 20:
        integer = 20
    
    elif integer <= 0:
        integer = 0
        
    return integer


def examMarkCleanse(integer):
    # A function that keeps the exam marks in a limit (if exceeded will reset
    # the value) and removes data type impurities from the input 
    
    integer = list(filter(lambda x: x.isdigit(), integer.split()))
    integer = sum([int(s) for s in integer])
    
    if integer >= 100:
        integer = 100
    
    elif integer <= 0:
        integer = 0
        
    return integer


def updateMenu1(studentnames):
    # A function that will ask which record the user wants to edit
    
    deleteItems()
    openFile()
    getValues()
    name = StringVar()
    
    title = Label(mainwindow, text = "UPDATE RECORD", font = "Arial 32 bold", bg = "#141211", fg = "white")
    title.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    
    logo = Label(mainwindow, text = "ⓘ", font = "Arial 67", bg = "#141211", fg = "white")
    logo.place(relx = 0.5, rely = 0.375, anchor = CENTER)
    
    enquiry = Label(mainwindow, text = "Which record would you like to edit?", font = "Corbel 15",
                    bg = "#141211", fg = "white")
    enquiry.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    records = ttk.Combobox(mainwindow, width = 25, textvariable = name)
    records['values'] = studentnames
    records.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    
    submit = Button(mainwindow, text = "Enter", font = "Corbel 15", bg = "#dbc15a",
                    bd = 0, width = 15, command = lambda: updateMenu2(name))
    submit.place(relx = 0.35, rely = 0.75, anchor = CENTER)
    
    back = Button(mainwindow, text = "Back", font = "Corbel 15", bg = "#dbc15a",
                  bd = 0, width = 15, command = lambda: mainMenu())
    back.place(relx = 0.65, rely = 0.75, anchor = CENTER)
    
    
def updateMenu2(name):
    # A function that will obtain the available data from the chosen record
    # and then fill each detail about the student inside entry banks as reference,
    # in case the user wants to edit certain details only

    deleteItems()
    openFile()
    getValues()
    
    choice = name.get()
    
    for i in range (len(students)):
        if students[i]["Name"] == choice:
            linetoupdate = students[i]["No."]
            
        count = 1

    with open("studentMarks.txt", "r") as f1:
        data = f1.readlines()[1:]
        
        # Assigning the reference data for the entry banks
        for i in data:
            if count == linetoupdate:
                j = i.split(",")
                
                idno = j[0]
                name = j[1]
                mark1 = j[2]
                mark2 = j[3]
                mark3 = j[4]
                exammark = j[5]
                
            count +=  1

    newname = StringVar()
    newidnum = StringVar()
    newmark1 = StringVar()
    newmark2 = StringVar()
    newmark3 = StringVar()
    newexammark = StringVar()

    title = Label(mainwindow, text = "UPDATE RECORD", font = "Arial 32 bold", bg = "#141211", fg = "white")
    title.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    
    label = Label(mainwindow, text = "Name:", font = "Corbel 13", bg = "#141211", fg = "white")
    label.place(relx = 0.25, rely = 0.25, anchor = W)
    prompt = Entry(mainwindow, textvariable = newname, width = 20, font = "Corbel 13", bd=3)
    prompt.place(relx = 0.6, rely = 0.25, anchor = CENTER)
    prompt.insert(0,idno) 
    # insert is a function thats allowed to be used for entry banks in order to fill them
    # with a default value (string/integer/whatever)

    label2 = Label(mainwindow, text = "ID:", font = "Corbel 13", bg = "#141211", fg = "white")
    label2.place(relx = 0.25, rely = 0.35, anchor = W)
    prompt2 = Entry(mainwindow, textvariable = newidnum, width = 20, font = "Corbel 13", bd=3)
    prompt2.place(relx = 0.6, rely = 0.35, anchor = CENTER)
    prompt2.insert(0,name)
    
    label3 = Label(mainwindow, text = "Course Marks 1: ", font = "Corbel 13", bg = "#141211", fg = "white")
    label3.place(relx = 0.25, rely = 0.45, anchor = W)
    prompt3 = Entry(mainwindow, textvariable = newmark1, width = 20, font = "Corbel 13", bd=3)
    prompt3.place(relx = 0.6, rely = 0.45, anchor = CENTER)
    prompt3.insert(0,mark1)

    label4 = Label(mainwindow, text = "Course Marks 2: ", font = "Corbel 13", bg = "#141211", fg = "white")
    label4.place(relx = 0.25, rely = 0.55, anchor = W)
    prompt4 = Entry(mainwindow, textvariable = newmark2, width = 20, font = "Corbel 13", bd=3)
    prompt4.place(relx = 0.6, rely = 0.55, anchor = CENTER)
    prompt4.insert(0,mark2)
    
    label5 = Label(mainwindow, text = "Course Marks 3: ", font = "Corbel 13", bg = "#141211", fg = "white")
    label5.place(relx = 0.25, rely = 0.65, anchor = W)
    prompt5 = Entry(mainwindow, textvariable = newmark3, width = 20, font = "Corbel 13", bd=3)
    prompt5.place(relx = 0.6, rely = 0.65, anchor = CENTER)
    prompt5.insert(0,mark3)
    
    label6 = Label(mainwindow, text = "Exam Marks: ", font = "Corbel 13", bg = "#141211", fg = "white")
    label6.place(relx = 0.25, rely = 0.75, anchor = W)
    prompt6 = Entry(mainwindow, textvariable = newexammark, width = 20, font = "Corbel 13", bd=3)
    prompt6.place(relx = 0.6, rely = 0.75, anchor = CENTER)
    prompt6.insert(0,exammark)
    
    submit = Button(mainwindow, text = "Submit", font = "Corbel 15", bg = "#dbc15a", bd = 0,
                    width = 15, command = lambda: updateInfo(newname,newidnum,newmark1,newmark2,newmark3,
                                                             newexammark,choice))
    submit.place(relx = 0.35, rely = 0.875, anchor = CENTER)
    
    back = Button(mainwindow, text = "Back", font = "Corbel 15", bg = "#dbc15a", bd = 0,
                    width = 15, command = lambda: mainMenu())
    back.place(relx = 0.65, rely = 0.875, anchor = CENTER)
    

def updateInfo(newname,newidnum,newmark1,newmark2,newmark3,newexammark,choice):
    # A function that will add the newly inputted data, look for the pre existing 
    # record in the txt file, rewrite the contents of the file to include the newly updated one
    
    newname = newname.get()
    newidnum = newidnum.get()
    newmark1 = newmark1.get()
    newmark2 = newmark2.get()
    newmark3 = newmark3.get()
    newexammark = newexammark.get()
    
    newname = stringCleanse(newname)
    newname = idCleanse(newname)
    newmark1 = courseMarkCleanse(newmark1)
    newmark2 = courseMarkCleanse(newmark2)
    newmark3 = courseMarkCleanse(newmark3)
    newexammark = examMarkCleanse(newexammark)
    
    count = 0
    
    for i in range (len(students)):
        if students[i]["Name"] == choice:
            linetoupdate = students[i]["No."]
            
    with open("studentMarks.txt", "r") as f:
        data = f.readlines()
    
    with open("studentMarks.txt", "w") as f:
        for i in data:
            try:
                if count != linetoupdate:
                    f.write(i)
                else:
                    f.write(str(newidnum) + "," + newname + "," + str(newmark1) + "," + str(newmark2) + "," 
                                + str(newmark3) + "," + str(newexammark) + "\n")
            except:
                f.write(i)
            count += 1
    
    mainMenu()


def deleteInfo(names):
    # A function that looks for the index of the line in the text file using the
    # index of the record in the internal dictionary then rewrites the contents 
    # of the text file to not include the record index referenced, thus 'deleting'
    # its existence by not making it known.
    
    userpick = names.get()
    
    for i in range(len(students)):
        if students[i]["Name"] == userpick:
            linetoignore = students[i]["No."]
            
    count = 0
    
    with open("studentMarks.txt", "r") as f:
        data = f.readlines()
        
    with open("studentMarks.txt", "w") as f:

        for i in data:
            try: 
                if count != linetoignore:
                    f.write(i)
                count += 1
                
            except:
                f.write(i)
    
    mainMenu()
    
    
def printLayout(nameinstance,IDinstance,courseinstance,markinstance,percentinstance,gradeinstance,txtarea):
   
    txtarea.insert(END,"Name: " + nameinstance + "\n")
    txtarea.insert(END,"Number: " + IDinstance + "\n")
    txtarea.insert(END,"Coursework Total: " + courseinstance + "\n")
    txtarea.insert(END,"Exam Mark: " + markinstance)
    txtarea.insert(END,"Overall Percentage: " + str(percentinstance) + "% \n")
    txtarea.insert(END, "\nGrade: " + gradeinstance + "\n")


def mainMenu():
    
    deleteItems()
    
    openFile()
    getValues()
    
    names = StringVar()
    sorts2 = StringVar()
    
    title = Label(mainwindow, text = "STUDENT MANAGER", font = "Arial 32 bold", bg = "#141211", fg = "white")
    title.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    
    b1 = Button(mainwindow, text = "View All Records", font = "Corbel 12", bg = "#dbc15a", width = 16,
                bd = 0, command = lambda: allRecords(txtarea))
    b1.place(relx = 0.25, rely = 0.2, anchor = CENTER)
    
    b2 = Button(mainwindow, text = "Show Highest Score", font = "Corbel 12", bg = "#dbc15a", width = 16, 
                bd = 0, command = lambda: highestScore(txtarea))
    b2.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    
    b3 = Button(mainwindow, text = "Show Lowest Score", font = "Corbel 12", bg = "#dbc15a", width = 16,
                bd = 0, command = lambda: lowestScore(txtarea))
    b3.place(relx = 0.75, rely = 0.2, anchor = CENTER)
    
    sen1 = Label(mainwindow, text = "Individual Student Records:", font = "Corbel 13", bg = "#141211", fg = "white")
    sen1.place(relx = 0.28, rely = 0.285, anchor = CENTER)
    
    records = ttk.Combobox(mainwindow, width = 25, textvariable = names)
    records['values'] = studentnames
    records.place(relx = 0.55, rely = 0.285, anchor = CENTER)
    
    b4 = Button(mainwindow, text = "View Record", font = "Corbel 12", bg = "#dbc15a", width = 12, 
                bd = 0, command = lambda: oneRecord(txtarea, names))
    b4.place(relx = 0.775, rely = 0.285, anchor = CENTER)
    
    txtarea = Text(mainwindow)
    txtarea.place(relx = 0.5, rely = 0.55, anchor = CENTER, height = 300, width = 500)
    
    scrollV = Scrollbar(mainwindow, orient = "vertical")
    scrollV.place(relx = 0.85, rely = 0.55, anchor = CENTER, height = 300)
    scrollV.config(command = txtarea.yview)
    txtarea.config(yscrollcommand = scrollV.set)

    sorts = ttk.Combobox(mainwindow, width = 25, textvariable = sorts2)
    sorts['values'] = options
    sorts.place(relx = 0.55, rely = 0.8, anchor = CENTER)
    
    b5 = Button(mainwindow, text = "Sort", font = "Corbel 12", bg = "#dbc15a", width = 12,
                bd = 0, command = lambda: sortData(txtarea, sorts))
    b5.place(relx = 0.775, rely = 0.8, anchor = CENTER)
    
    b6 = Button(mainwindow, text = "Add Student", font = "Corbel 12", bg = "#dbc15a", width = 16,
                bd = 0, command = lambda: addStudent())
    b6.place(relx = 0.25, rely = 0.885, anchor = CENTER)
    
    b7 = Button(mainwindow, text = "Delete Record", font = "Corbel 12", bg = "#dbc15a", width = 16,
                bd = 0, command = lambda: deleteInfo(names))
    b7.place(relx = 0.5, rely = 0.885, anchor = CENTER)
    
    b8 = Button(mainwindow, text = "Update Record", font = "Corbel 12", bg = "#dbc15a", width = 16,
                bd = 0, command = lambda: updateMenu1(studentnames))
    b8.place(relx = 0.75, rely = 0.885, anchor = CENTER)
    
mainMenu()

mainwindow.mainloop()
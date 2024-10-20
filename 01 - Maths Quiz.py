from tkinter import *
import random

# Initializing Variables
difficulty = ""
operations = ["add", "sub"] # Making the add/sub as a list prevents the programmer (me) from
                            # not caring what I assigned 1 - ? and 0 - ? as. (Readability)
progress = 1                
score = 0
no1 = 0
no2 = 0
tries = 0                   # This will keep track of each attempt of the user when they give an answer.

# Defining Functions
def clearwindow():
    for item in quizwin.winfo_children():           # This function in particular clears every item using a loop and destroy()
        item.destroy()                              # Each Label, Button and etc are considered a 'children' item of the 'parent' window

def displayMenu ():                                 # Everytime the user wants to 'play' the quiz it will run this function
    global progress, tries, score                   # Global variables are declared to make sure they are accessible outside the function.
    score = 0                                       # This is particularly important as we need to make changes throughout the quiz--
    tries = 0                                       # like, when the user needs to play again so things like the score requires a reset.
    progress = 1
    
    clearwindow()                                   # Functions that required space for labels have their contents deleted to make
                                                    # new/clean space for the next function. Ex: After the results screen, the program-
                                                    # requires the same window to display the menu, thus we need to delete the items of
                                                    # displayResults() for displayMenu()'s items.

    title = Label(quizwin, text = "Welcome to the 2.4 Maths Quiz!", font = "Helvetica 20 bold", bg = "#18ba43")
    title.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    
    subtitle = Label(quizwin,text = "Developed by additionmission.org", font = "Helvetica 15", 
                     bg = "#18ba43", fg = "#3b3b3b")
    subtitle.place(relx = 0.5, rely = 0.25, anchor = CENTER)
    
    subtitle2 = Label(quizwin, text = "Choose your difficulty:", font = "Helvetica 15 bold", bg = "#18ba43")
    subtitle2.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    
    ezy = Button(quizwin, text = "Easy", command = lambda: randomInt(difficulty = "Easy"), # Whenever a difficulty button is pressed, the 
                                                                                           # function is called, then an arguement with an 
                                                                                           # assigned value is given to immediately start the quiz.
                    fg = "#032413", bg = "#0bb55d", font = "Helvetica 15", width = 12, bd = 0)      
    ezy.place(relx = 0.25, rely = 0.5, anchor = CENTER)
    
    modr = Button(quizwin, text = "Moderate", command = lambda: randomInt(difficulty = "Moderate"), 
                  fg = "#303304", bg = "#c4d10f", font = "Helvetica 15", width = 12, bd = 0)
    modr.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    adv= Button(quizwin, text = "Advanced", command = lambda: randomInt(difficulty = "Advanced"), 
                fg = "#2e0a08", bg = "#d92d27",font = "Helvetica 15", width = 12, bd = 0)
    adv.place(relx = 0.75, rely = 0.5, anchor = CENTER)
    
    goodluck = Label(quizwin, text = "ヽ(*´∀｀)八(´∀｀*)ノ", fg = "white", font = "Helvetica 18 bold", bg = "#18ba43")
    goodluck.place(relx = 0.5, rely = 0.75, anchor = CENTER)

    
def randomInt (difficulty):                     # This parameter will obtain the values of the first button pressed and start.
    global no1, no2                             # These numbers need to be global to be accessed in other functions.
    
    if difficulty == "Easy":                    # Easy mode only allows one digit, Moderate two digits and Advanced three digits.
        no1 = random.randint(1,9)
        no2 = random.randint(1,9)               # random.randint() assigns random values from a given range such as, between 1 - 9

    elif difficulty == "Moderate":
        no1 = random.randint(10,99)
        no2 = random.randint(10,99)
        
    elif difficulty == "Advanced":
        no1 = random.randint(100,999)
        no2 = random.randint(100,999)
        
    decideOperation(no1, no2, difficulty)       # Once values are assigned, the type of operation will then be decided (add/sub).


def decideOperation (no1, no2, difficulty):
    global operationchoice, correctanswer
    
    operationchoice = operations[random.randint(0,1)]        # Randomizing between addition or subtraction
  
    if operationchoice == "add":
        correctanswer = no1 + no2                            # The correct answer will be decided before using the numbers as string

    elif operationchoice == "sub":
        correctanswer = no1 - no2
            
    displayProblem(no1, no2, operationchoice, difficulty)   


def displayProblem (no1, no2, operationchoice, difficulty):
    clearwindow()                                           # In order to start displaying the questions, every item in the window is 'erased'
                                                            
    global correctanswer, progress                          
    
    progresscheck = Label(quizwin, text = "Question " + str(progress) + " out of 10", 
                          font = "Helvetica 15 bold", bg = "#18ba43")            # Progress is converted to string in order to display it 
                                                                                 # as something readable. The same thing is done for the equations.
    
    progresscheck.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    
    question = Label(quizwin, text = "", font = "Helvetica 50 bold", bg = "#18ba43")
    question.place(relx = 0.5, rely = 0.35, anchor = CENTER)

    if operationchoice == "add":                                                
        question.config(text = (str(no1) + " + " + str(no2) + " = "))            # .config() is a function that allows changes for a single attribute
                                                                                 # in an existing Label/Button/ETC, useful for preventing repitition.
    elif operationchoice == "sub":
        question.config(text = (str(no1) + " - " + str(no2) + " = "))

    result = Entry(quizwin, width = 8, textvariable = answer, font = "Helvetica 20")
    result.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    submit = Button(quizwin, width = 8, text = "ENTER", fg = "white", bg = "#119147", 
                    font = "Helvetica 20", bd = 0, command = lambda: isCorrect(no1, no2, correctanswer, difficulty)) # IsCorrect() Checks the answer
    submit.place(relx = 0.5, rely = 0.65, anchor = CENTER)
    
    scoreinfo = Label(quizwin, text = "First try: 10 points || Second try: 5 points", font = "Helvetica 10", bg = "#18ba43")
    scoreinfo.place(relx = 0.5, rely = 0.82, anchor = CENTER)


def isCorrect(no1, no2, correctanswer, difficulty): # In order to prevent the quiz from breaking, its important to 'continue' the--
    global score, tries, progress                   # values for each variable when they are 'ran' through functions
    userresult = answer.get()                       # get() is a function under the tkinter library that obtains the value entered by 
                                                    # the user into the python program and stores it in a variable like 'userresult'
    try:
        if userresult == correctanswer:             # If the user enters the correct answer (assigned from decideOperation()) it will--
            progress += 1                           # move to the next question. However--
            
            if tries == 1:                          # If the user has attempted to answer the question and failed before it will
                tries = 0                           # Reset the amount of tries for the next question but only award 5 points.
                score += 5
                
                if progress > 10:                   # And, if the progress (aka 10 questions are answered) is exceeded it will end--
                    displayResults()                # the quiz and display the results of the user.
                    
                else:
                    randomInt(difficulty)
                    
            else:
                score += 10
    
                if progress > 10:                   # Whether or not the user has succeeded or failed to answer this program will always check--
                    displayResults()                # the condition of whether or not they have completed 10 questions.
                    
                else:
                    randomInt(difficulty)           # But if the progress is not exceeding 10 it will display a new problem.
    
        else:
            tries += 1
            
            if tries == 2:
                progress += 1
                tries = 0
            
                if progress > 10:
                    displayResults()
                    
                else:
                    randomInt(difficulty)
                    
            else:
                warning = Label(quizwin, text = "You have one more attempt.", font = "Helvetica 15", 
                            fg = "red", bg = "#18ba43")                           # To alert the user they have one last attempt.
                warning.place(relx = 0.5, rely = 0.75, anchor = CENTER)
                      
    except TypeError:            # Raises an error for the console whem the user enters something other than an integer type.
        raise TypeError
    
def displayResults():            # displayResults() will start comparing the 'score' earned in the quiz and gives an accomodating grade.
    clearwindow()
    
    global score
    
    results = Label(quizwin, text = "Your total score is: " + str(score), font = "Helvetica 20 bold", bg = "#18ba43")
    results.place(relx = 0.5, rely = 0.25, anchor = CENTER)
    
    results2 = Label(quizwin, text = "GRADE:", font = "Helvetica 15", bg = "#18ba43")
    results2.place(relx = 0.5, rely = 0.35, anchor = CENTER)
    
    grade = Label(quizwin, text = "", font = "Helvetica 20 bold", bg = "#18ba43")       # Will display as empty but once quiz is done, will--
    grade.place(relx = 0.5, rely = 0.42, anchor = CENTER)                               # display a grade.
    
    if (score < 50):
        grade.config(text = "F")
        
    elif(score >= 51 and score <= 60):
        grade.config(text = "E")
        
    elif(score >= 61 and score <= 70):
        grade.config(text = "D")
        
    elif(score >= 71 and score <= 80):
        grade.config(text = "C")
        
    elif(score >= 81 and score <= 90):
        grade.config(text = "B")
        
    elif(score >= 91):
        grade.config(text = "A")
        
    elif(score == 100):                                                                 # Perfect score is automatically given an A+
        grade.config(text = "A+")
    
    quizagain = Button(quizwin, text = "TRY AGAIN", font = "Helvetica 16", width = 10, bg = "#d3d600", bd = 0, command = lambda: displayMenu())
    quizagain.place(relx = 0.35, rely = 0.6, anchor = CENTER)
    
    quitwindow = Button(quizwin, text = "EXIT", font = "Helvetica 16", width = 10, bg = "#d62700", bd = 0, command = quizwin.destroy) 
                                                                                        # destroy just closes the window/stops it running.
    quitwindow.place(relx = 0.65, rely = 0.6, anchor = CENTER)

quizwin = Tk()
answer = IntVar(quizwin)                                                                # Initializing the answer as an only integer value.

quizwin.title("Mathemathics Quiz 2.4.3")
quizwin.geometry('620x500')
quizwin.resizable(0,0)
quizwin.config(bg = "#18ba43")                                                          # Changes background colour of tkinter window.

displayMenu()

quizwin.mainloop()
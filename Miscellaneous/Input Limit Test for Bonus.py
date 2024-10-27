"""
user = input(str("Enter a name: "))


check = False
length = len(user)

while check == False:
    
    if length > 30:
        user = user[:-1]
        length = len(user)
        user = "".join(c for c in user if c.isalpha())
        
    else:
        check = True
"""

    
"""    
    with open("studentMarks.txt", "r") as f1:
        data = f1.readlines()[1:]
        
        for i in data:
            if count == linetoupdate:
                j = i.split(",")
                
                idno = j[0]
                name = j[1]
                mark1 = j[2]
                mark2 = j[3]
                mark3 = j[4]
                exammark = j[5]
                
                newidnum.delete(0, END)
                newname.delete(0, END)
                newmark1.delete(0, END)
                newmark2.delete(0, END)
                newmark3.delete(0, END)
                newexammark.delete(0, END)
                
                newname.insert(0, name)
                newidnum.insert(0, idno)
                newmark1.insert(0, mark1)
                newmark2.insert(0, mark2)
                newmark3.insert(0, mark3)
                newexammark.insert(0, exammark)
                
            count +=  1
"""


"""
    with open("studentMarks.txt", "r") as f1:
        data = f1.readlines()[1:]
        
        for i in data:
            if count == linetoupdate:
                j = i.split(",")
                
                idno = j[0]
                name = j[1]
                mark1 = j[2]
                mark2 = j[3]
                mark3 = j[4]
                exammark = j[5]
                
                ogid.delete(0, END)
                ogname.delete(0, END)
                ogmark1.delete(0, END)
                ogmark2.delete(0, END)
                ogmark3.delete(0, END)
                ogexammark.delete(0, END)
                
                ogname.insert(0, name)
                ogid.insert(0, idno)
                ogmark1.insert(0, mark1)
                ogmark2.insert(0, mark2)
                ogmark3.insert(0, mark3)
                ogexammark.insert(0, exammark)
                
            count +=  1
"""

intnum = "There are 2 apples for 4 persons"
test = [1,2,3,4]

test2 = "Richardson Barksonwewrwe"
print(len(test2))

print(len(test))

# use the split() method to split
# use the filter() function to filter out non-numeric elements from the list
intnum = list(filter(lambda x: x.isdigit(), intnum.split()))

# intnum = list(filter(lambda x: x.isdigit(), integer.split()))
# use a list comprehension to convert the remaining elements to integers
intnum = sum([int(s) for s in intnum])

print(intnum)


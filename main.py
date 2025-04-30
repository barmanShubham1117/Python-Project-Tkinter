# Reference: https://www.geeksforgeeks.org/python-todo-gui-application-using-tkinter/


# importing required packages
from tkinter import *

tasks_list = []
counter = 1

def clearTask():
    enterTaskField.delete(0, END)

def insertTask():
    global counter

    content = enterTaskField.get() + '\n'
    print(f'New Task: {content}')

    tasks_list.append(content)
    print(f'Current task list: {tasks_list}')

    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)

    counter += 1

    clearTask()
    

if __name__ == "__main__":
    root = Tk()

    root.title('My TO-DO Application')
    root.geometry("500x600")
    root.configure(background="light grey", border="2")

    enterTask = Label(root, text = "Ibrahim, what are you up for today?", bg = "light green")
    enterTaskField = Entry(root)

    Submit = Button(root, text = "Submit", fg = "Black", bg = "Red", command=insertTask)
    TextArea = Text(root, height = 5, width = 25, font = "arial")
 
    taskNumber = Label(root, text = "Delete Task Number", bg = "blue")
                        
    taskNumberField = Text(root, height = 1, width = 2, font = "lucida 13")
 
    delete = Button(root, text = "Delete", fg = "Black", bg = "Red")

    Exit = Button(root, text = "Exit", fg = "Black", bg = "Red", command = exit)
 
    enterTask.grid(row = 0, column = 2)
              
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)
                        
    Submit.grid(row = 2, column = 2)
         
    TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
                        
    taskNumber.grid(row = 4, column = 2, pady = 5)
                        
    taskNumberField.grid(row = 5, column = 2)
                 
    delete.grid(row = 6, column = 2, pady = 5)

    Exit.grid(row = 7, column = 2)

    root.mainloop()
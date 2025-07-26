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

def deleteTask():
    global counter

    try:
        task_number = int(taskNumberField.get("1.0", "end-1c").strip())
        if 1 <= task_number < counter:
            tasks_list.pop(task_number - 1)
            print(f'Task {task_number} deleted. Current task list: {tasks_list}')
            TextArea.delete("1.0", "end")
            for i, task in enumerate(tasks_list, start=1):
                TextArea.insert('end', f"[ {i} ] {task}")
            counter -= 1
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")
    
    taskNumberField.delete("1.0", "end")
    

if __name__ == "__main__":
    window = Tk()

    window.title('My TO-DO Application')
    window.geometry("500x600")
    window.configure(background="light grey", border="2")

    enterTask = Label(window, text = "Ibrahim, what are you up for today?", bg = "light green")
    enterTaskField = Entry(window)

    Submit = Button(window, text = "Submit", fg = "Black", bg = "Red", command=insertTask)
    TextArea = Text(window, height = 5, width = 25, font = "arial")
 
    taskNumber = Label(window, text = "Delete Task Number", bg = "blue")
                        
    taskNumberField = Text(window, height = 1, width = 2, font = "lucida 13")
 
    delete = Button(window, text = "Delete", fg = "Black", bg = "Red", command=deleteTask)

    Exit = Button(window, text = "Exit", fg = "Black", bg = "Red", command = exit)
 
    enterTask.grid(row = 0, column = 2)
              
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)
                        
    Submit.grid(row = 2, column = 2)
         
    TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
                        
    taskNumber.grid(row = 4, column = 2, pady = 5)
                        
    taskNumberField.grid(row = 5, column = 2)
                 
    delete.grid(row = 6, column = 2, pady = 5)

    Exit.grid(row = 7, column = 2)

    window.mainloop()
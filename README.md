# My TO-DO Application

A simple GUI-based To-Do List application built with Python's Tkinter library. This project allows users to add, view, and manage daily tasks in an interactive window.

## Features
- **Add Tasks:** Enter a task and submit to add it to your list.
- **View Tasks:** All tasks are displayed in a numbered list.
- **Delete Tasks:** (UI present, logic can be added) Delete a task by entering its number.
- **Clear Input:** Input field is cleared after each submission.
- **Exit Button:** Close the application safely.

## Getting Started

### Prerequisites
- Python 3.x
- Tkinter (usually included with Python standard library)

### How to Run
1. Clone or download this repository.
2. Open a terminal and navigate to the project directory.

#### (Recommended) Run in a Python Virtual Environment
1. Create a virtual environment:
   ```powershell
   python -m venv venv
   ```
2. Activate the virtual environment:
   ```powershell
   .\venv\Scripts\activate
   ```
3. (Optional) Upgrade pip:
   ```powershell
   python -m pip install --upgrade pip
   ```
4. Run the application:
   ```powershell
   python main.py
   ```
   Or use your preferred Python IDE.

## File Structure
- `main.py` : Main application file containing all logic and UI code.

## Usage
1. Enter your task in the input field.
2. Click **Submit** to add the task to the list.
3. To delete a task, enter its number in the "Delete Task Number" field and click **Delete** (delete logic can be implemented).
4. Click **Exit** to close the application.

## Customization
- You can change the UI colors, fonts, and window size in `main.py`.
- To add more features (e.g., persistent storage, improved delete logic), modify the code as needed.

## Example Screenshot
*(Add a screenshot of the running application here)*

## Credits
- Based on [GeeksforGeeks Python To-Do GUI Application using Tkinter](https://www.geeksforgeeks.org/python-todo-gui-application-using-tkinter/)

## License
This project is for educational purposes. Feel free to use and modify as needed.

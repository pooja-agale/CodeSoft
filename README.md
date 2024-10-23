# CodeSoft

# Simple Python Calculator
This is a basic calculator script written in Python. The program takes two numbers and an operator as input from the user and performs the corresponding mathematical operation (addition, subtraction, multiplication, division, or percentage). The result is then displayed to the user.

Features:
Addition: Adds two numbers and displays the result.
Subtraction: Subtracts the second number from the first and shows the result.
Multiplication: Multiplies the two numbers and outputs the result.
Division: Divides the first number by the second and displays the result (handles float division).
Percentage Calculation: Calculates the percentage of the two numbers.
Input Validation: Handles invalid operator input by displaying an error message.
How It Works:
The user is prompted to input two numbers.
The user enters a mathematical operator (+, -, *, /, %).
Based on the operator, the corresponding operation is performed:
+ for addition
- for subtraction
* for multiplication
/ for division
% for percentage calculation
If an invalid operator is entered, the program prints "Invalid Input."
The result of the operation is printed along with a "THANK YOU" message.
Example Usage:
plaintext
Copy code
_______CALCULATOR________

Enter number: 10
Enter number: 5
Enter operator: +
Addition:  15
....THANK YOU....
Technologies Used:
Python: The script is written in Python and uses basic control structures like if-elif-else to handle user input and perform operations.
Setup Instructions:
Ensure Python is installed on your system.
Run the script (calculator.py) in a Python environment.
Follow the on-screen instructions to input numbers and choose an operator.


# Contact Book Application

This is a Python-based Contact Book application built using the Tkinter library for creating a graphical user interface (GUI). The application allows users to add, view, search, and delete contacts easily. It offers a simple and intuitive interface for managing a list of contacts with names and phone numbers.

Features:
Add Contact: Users can enter a name and contact number, which is then added to the contact list.
View Contact: Displays the entire list of contacts in a separate window.
Search Contact: Users can search for a contact by name, and the matching results are displayed.
Delete Contact: Users can select a contact from the list and delete it.
Close Button: An exit button is provided to close the application at any point.
How It Works:
Main Window: The main window contains input fields for the name and contact number, along with buttons to submit the contact, view all contacts, search for a contact, and delete a selected contact.
Adding Contacts: Users can add contacts by entering the name and phone number and clicking the "Submit" button. The contact is then stored in a list and displayed in the contact listbox.
Viewing Contacts: The "View Contact" button opens a new window where the user can see all saved contacts.
Searching Contacts: The "Search Contact" button opens a new window where users can enter a name to search for. If any matches are found, they are displayed in a list.
Deleting Contacts: The "Delete Contact" button allows users to remove a selected contact from the list.
Project Structure:
Tkinter GUI: This application uses Tkinter to create a user-friendly graphical interface.
Listbox: The Listbox widget is used to display the list of contacts and results.
Entry Fields: Two entry fields are provided for users to input names and contact numbers.
Technologies Used:
Python: The primary language used for building the application.
Tkinter: A Python library for building desktop GUI applications.
Toplevel Widgets: Used to create additional windows for viewing and searching contacts.
Setup Instructions:
Python Installation: Make sure you have Python installed on your machine.
Run the Script: Clone the repository and run the contact_book.py file to start the application.
Adding Contacts: Input the contact details in the provided fields and manage your contacts easily.
Example Usage:
Adding a Contact:

Enter a name in the "Name" field.
Enter the contact number in the "Add Contact" field.
Click "Submit" to add the contact.
Viewing Contacts:

Click the "View Contact" button to see all contacts.


# Random Password Generator

This Python script generates a random password consisting of uppercase and lowercase letters, digits, and special characters. It uses the random and string modules to create secure passwords.

Features:
Random Password Generation: The script generates an 8-character password by default, combining letters, numbers, and special characters for enhanced security.
Customizable Length: You can modify the length of the password by changing the value of password_len.
How It Works:
Password Length: The script sets the password length to 8 characters.
Character Pool: It uses string.ascii_letters, string.digits, and string.punctuation to create a pool of possible characters.
Password Generation: The script loops through and selects random characters from the pool to create a password.
Output: Once the password is generated, it is displayed in the console.
Code Breakdown:
string.ascii_letters: Contains all lowercase and uppercase English letters.
string.digits: Contains numbers 0-9.
string.punctuation: Contains special characters like !@#$%^&*(), etc.
random.choice(): Randomly selects a character from the available pool for each position in the password.
Example Usage:
perl
Copy code
Your random password: 4$eG&n@B
How to Run:
Python Installation: Ensure you have Python installed on your system.
Run the Script: Execute the script in your terminal or IDE. The randomly generated password will be printed to the console.
Customization:
To increase or decrease the password length, modify the password_len variable at the top of the script.
python
Copy code
password_len = 12  # For a 12-character password
Technologies Used:
Python: The script is written in Python and utilizes the built-in random and string modules.

# To-Do List Application

This is a simple graphical user interface (GUI) To-Do List application built using Python's Tkinter library. The app allows users to add, delete, track, and update tasks, making it easier to manage tasks in an organized way.

Features:
Add Tasks: Users can add tasks by typing in the input field and clicking the "Add Task" button.
Delete Tasks: Selected tasks can be deleted by choosing the task from the list and clicking the "Delete Task" button.
Update Task List: The task list can be refreshed and updated by clicking the "Update Task" button.
Track Tasks: Displays a list of all added tasks in a separate window when the "Track To-Do List" button is clicked.
Exit: A simple exit button to close the application.
How It Works:
Adding Tasks: When a user enters a task and clicks the "Add Task" button, it is added to both the displayed list (Listbox) and the tasks list.
Deleting Tasks: Selecting a task from the list and clicking "Delete Task" removes the task from the list and updates the task display.
Tracking Tasks: Clicking "Track To-Do List" opens a new window showing all current tasks.
Updating Task List: Clicking "Update Task" refreshes the task display to ensure the latest tasks are shown.
Closing the App: The "Exit" button closes the app.
Code Breakdown:
add_task(): Adds the entered task to the tasks list and updates the Listbox.
delete_task(): Deletes the selected task from both the tasks list and the Listbox.
show_tracked_tasks(): Opens a new window to show all tasks in the list.
update_task_section(): Updates the Listbox by reloading the list of tasks.
UI Setup: The user interface is created using Tkinter widgets such as Label, Entry, Listbox, and Button. The window is configured with a purple background.
Technologies Used:
Python: The application is written in Python.
Tkinter: This is the standard GUI library in Python, used for building the graphical interface of the app.
How to Run:
Python Installation: Ensure that Python is installed on your system.
Tkinter Library: Tkinter comes pre-installed with Python, but if not available, install it using:
bash
Copy code
pip install tk
Run the Script: Run the Python script from your terminal or an IDE to open the To-Do List application.
Example Usage:
Add a task like "Buy groceries" using the input field.
Delete a task by selecting it from the task list and clicking the "Delete Task" button.
View all tracked tasks in a new window by clicking the "Track To-Do List" button.
Update or refresh the task list by clicking "Update Task".
Screenshots (optional):
Add screenshots to showcase the functionality of the app.




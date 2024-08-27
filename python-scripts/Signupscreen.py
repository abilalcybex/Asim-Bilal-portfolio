import tkinter as tk
import pyodbc

def open_calculator():
    calculator_window = tk.Toplevel(root)
    calculator_window.title("Login Successful")

    expression = tk.StringVar()
    result = tk.StringVar()

    def evaluate_expression():
        try:
            result.set(eval(expression.get()))
        except:
            result.set("Error")

    def clear():
        expression.set("")
        result.set("")

    def append_to_expression(value):
        current_expression = expression.get()
        expression.set(current_expression + str(value))

    entry_calculator = tk.Entry(calculator_window, textvariable=expression, font=('Arial', 18), bd=10, insertwidth=4, width=25, justify="right")
    entry_calculator.grid(row=0, column=0, columnspan=4)

    result_label = tk.Label(calculator_window, textvariable=result, font=('Arial', 18), bd=10, width=25, anchor="e", relief="groove")
    result_label.grid(row=1, column=0, columnspan=4)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
    ]

    for (text, row, col) in buttons:
        btn = tk.Button(calculator_window, text=text, font=('Arial', 18), bd=5, width=5, command=lambda t=text: append_to_expression(t))
        btn.grid(row=row, column=col)

    clear_button = tk.Button(calculator_window, text='C', font=('Arial', 18), bd=5, width=5, command=clear)
    clear_button.grid(row=5, column=0, columnspan=2)

def submit_form():
    username = entry_username.get()
    password = entry_password.get()
    
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-FKSHIM8\SQLEXPRESS01;'  
                              'Database=Cybex;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM signupscreen_login WHERE username=? AND password=?", (username, password))
        row = cursor.fetchone()
        conn.close()
        if row:
            print("Login successful. Username:", username)
            open_calculator()
        else:
            print("Incorrect username or password.")
    except Exception as e:
        print("Error:", e)

def signup_form():
    username = entry_signup_username.get()
    password = entry_signup_password.get()
        
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-FKSHIM8\SQLEXPRESS01;'
                              'Database=Cybex;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO signupscreen_login (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        print("Signup successful. Username:", username)
    except Exception as e:
        print("Error:", e)

root = tk.Tk()
root.title("Login and Signup")
root.geometry("600x500")  

label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=50, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=50, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=50, pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=50, pady=10)

button_login = tk.Button(root, text="Login", command=submit_form)
button_login.grid(row=2, column=0, columnspan=2, padx=100 , pady=20)

label_signup_username = tk.Label(root, text="Username:")
label_signup_username.grid(row=3, column=0, padx=50, pady=10)
entry_signup_username = tk.Entry(root)
entry_signup_username.grid(row=3, column=1, padx=50, pady=10)

label_signup_password = tk.Label(root, text="Password:")
label_signup_password.grid(row=4, column=0, padx=50, pady=10)
entry_signup_password = tk.Entry(root, show="*")
entry_signup_password.grid(row=4, column=1, padx=50, pady=10)

button_signup = tk.Button(root, text="Signup", command=signup_form)
button_signup.grid(row=7, column=0, columnspan=2, padx=100 , pady=20)

root.mainloop()

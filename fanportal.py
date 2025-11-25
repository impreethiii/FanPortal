import tkinter as tk	
from tkinter import messagebox

USERNAME1 = "fanportal"
PASSWORD1 = "password"

# Function for changing slide for login
def change_slide():
    main_screen.withdraw()  # Hide the main screen

    login_screen = tk.Toplevel()
    login_screen.geometry("600x900")
    login_screen.title("Login")
    login_screen.configure(bg="#E6E6FA")  # Lavender background

    title = tk.Label(login_screen, text="LOG IN", font=('Helvetica', 40, 'bold'), bg="#E6E6FA", fg="#4B0082")  # Dark Purple text
    title.pack(pady=50)

    # Username
    username_label = tk.Label(login_screen, text="Username:", font=('Helvetica', 20), bg="#E6E6FA", fg="#4B0082")
    username_label.pack(pady=10)
    username_entered = tk.Entry(login_screen, font=('Helvetica', 20), bd=2, relief="solid", borderwidth=3)
    username_entered.pack(padx=40, pady=10, ipadx=5, ipady=5)

    # Password
    password_label = tk.Label(login_screen, text="Password:", font=('Helvetica', 20), bg="#E6E6FA", fg="#4B0082")
    password_label.pack(pady=10)
    password_entered = tk.Entry(login_screen, font=('Helvetica', 20), bd=2, relief="solid", borderwidth=3, show="*")
    password_entered.pack(padx=40, pady=10, ipadx=5, ipady=5)

    # Login Button
    login_button2 = tk.Button(login_screen, text="Login", font=('Helvetica', 20), bg="#9370DB", fg="white", relief="flat", width=20, height=2,
                               command=lambda: login(username_entered.get(), password_entered.get(), login_screen))
    login_button2.pack(pady=20)

# Function to check username and password
def login(username, password, login_screen):
    if username == USERNAME1 and password == PASSWORD1:
        messagebox.showinfo("Login", "Login Successful")
        login_screen.destroy()
        main_screen.destroy() 
        show_welcome_screen()  
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# Function to show the welcome screen
def show_welcome_screen():
    welcome_screen = tk.Tk()
    welcome_screen.title("FANPORTAL")
    welcome_screen.geometry("600x900")
    welcome_screen.configure(bg="#E6E6FA") 

    # Add welcome message
    welcome_label = tk.Label(welcome_screen, text="WELCOME TO THE FANPORTAL! \nBecause Every Fan Deserves a Portal ;)", font=('Helvetica', 30, 'bold'), bg="#E6E6FA", fg="#4B0082")
    welcome_label.pack(padx=40, pady=300)
    

    welcome_screen.mainloop()

# Function for signup success
def signup_success(email, username, password, confirm_password, signup_screen):
    if email and password and username and confirm_password:
        if password == confirm_password:
            messagebox.showinfo("Signup Successful", "You have successfully signed up")
            signup_screen.destroy()
            main_screen.destroy()
            show_welcome_screen()  # Open a new welcome screen
        else:
            messagebox.showerror("Signup Failed", "Passwords do not match")
    else:
        messagebox.showerror("Signup Failed", "All fields are required")

# Second slide for signing up
def signup():
    main_screen.withdraw()  # Hide the main screen

    signup_screen = tk.Toplevel()  # Create a new window (Toplevel)
    signup_screen.geometry("600x900")
    signup_screen.title("Sign Up")
    signup_screen.configure(bg="#E6E6FA")  # Lavender background

    # Email
    email_label = tk.Label(signup_screen, text="Email:", font=('Helvetica', 20), bg="#E6E6FA", fg="#4B0082")
    email_label.pack(pady=10)
    email_entered = tk.Entry(signup_screen, font=('Helvetica', 20), bd=2, relief="solid", borderwidth=3)
    email_entered.pack(padx=40, pady=10, ipadx=5, ipady=5)

    # Username
    username_label = tk.Label(signup_screen, text="Username:", font=('Helvetica', 20), bg="#E6E6FA", fg="#4B0082")
    username_label.pack(pady=10)
    username_entry = tk.Entry(signup_screen, font=('Helvetica', 20), bd=2, relief="solid", borderwidth=3)
    username_entry.pack(padx=40, pady=10, ipadx=5, ipady=5)

    # Password
    password_label = tk.Label(signup_screen, text="Password:", font=('Helvetica', 20), bg="#E6E6FA", fg="#4B0082")
    password_label.pack(pady=10)
    password_entry = tk.Entry(signup_screen, font=('Helvetica', 20), show="*", bd=2, relief="solid", borderwidth=3)
    password_entry.pack(padx=40, pady=10, ipadx=5, ipady=5)

    # Confirm password
    confirm_password_label = tk.Label(signup_screen, text="Confirm Password:", font=('Helvetica', 20), bg="#E6E6FA", fg="#4B0082")
    confirm_password_label.pack(pady=10)
    confirm_password_entry = tk.Entry(signup_screen, font=('Helvetica', 20), show="*", bd=2, relief="solid", borderwidth=3)
    confirm_password_entry.pack(padx=40, pady=10, ipadx=5, ipady=5)

    # Sign-up Button
    signup_button2 = tk.Button(signup_screen, text="Sign Up", font=('Helvetica', 20), bg="#9370DB", fg="white", relief="flat", width=20, height=2,
                                command=lambda: signup_success(email_entered.get(), username_entry.get(), password_entry.get(), confirm_password_entry.get(), signup_screen))
    signup_button2.pack(pady=20)

# First slide (main screen)
main_screen = tk.Tk()
main_screen.title("FANPORTAL")
main_screen.geometry("600x900")
main_screen.configure(bg="#E6E6FA")  # Lavender background

# Title
title = tk.Label(main_screen, text="FANPORTAL<3!", font=('Helvetica', 40, 'bold'), bg="#E6E6FA", fg="#4B0082")
title.pack(pady=50)

# Sign up Button
signup_button = tk.Button(main_screen, text="Sign Up", font=('Helvetica', 20), bg="#8A2BE2", fg="white", relief="flat", width=20, height=2, command=signup)
signup_button.pack(pady=20)

# Login Button
login_button1 = tk.Button(main_screen, text="Log In", font=('Helvetica', 20), bg="#8A2BE2", fg="white", relief="flat", width=20, height=2, command=change_slide)
login_button1.pack(pady=20)

main_screen.mainloop()

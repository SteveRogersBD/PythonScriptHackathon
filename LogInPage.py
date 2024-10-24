import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to handle login (placeholder, can be replaced with logic later)
def login():
    messagebox.showinfo("Login", "Login button clicked!")

# Function to handle login with Gmail (placeholder)
def login_with_gmail():
    messagebox.showinfo("Login with Gmail", "Login with Gmail button clicked!")

# Initialize main window
root = tk.Tk()
root.title("Login Page")
root.geometry("500x400")  # Set window size

# Load background image
bg_image = Image.open("cap.jpg")  # Replace with your image path
bg_image = bg_image.resize((500, 400))  # Resize image to fit window
bg = ImageTk.PhotoImage(bg_image)

# Create a label to hold the background image
bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a Frame to hold the input fields and buttons
frame = Frame(root, bg='white', padx=10, pady=10)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the frame

# Email Label and Entry
email_label = Label(frame, text="Email", font=('Arial', 12), bg='white')
email_label.grid(row=0, column=0, pady=10, sticky="w")
email_entry = Entry(frame, font=('Arial', 12), width=30)
email_entry.grid(row=0, column=1, pady=10)

# Password Label and Entry
password_label = Label(frame, text="Password", font=('Arial', 12), bg='white')
password_label.grid(row=1, column=0, pady=10, sticky="w")
password_entry = Entry(frame, font=('Arial', 12), width=30, show='*')
password_entry.grid(row=1, column=1, pady=10)

# Login Button
login_button = Button(frame, text="Login", font=('Arial', 12), bg='#4CAF50', fg='white', width=20, command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Login with Gmail Button
gmail_button = Button(frame, text="Login with Gmail", font=('Arial', 12), bg='#4285F4', fg='white', width=20, command=login_with_gmail)
gmail_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()


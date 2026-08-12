#Commercial Property Management System
#This application allows administrators to manage commercial properties
#It also allows users to search available properties using a graphical interface
#This application is developed using Python and Tkinter for the GUI
#and CSV files for persistent data storage.

import tkinter as tk
from tkinter import messagebox

#Main application Window configuration
root=tk.Tk() # Creates the main Tkinter window
root.title("Commercial Property Management System")
root.geometry("600x500") #Sets the window size
admins={"admin":"admin123"}

import csv
import os

#CSV file setup
file_name="properties.csv" #File to store property details

#Creates the property file if it does not exist
if not os.path.exists(file_name):
    with open(file_name, mode="w", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["Type","floors","Size","Parking","Availability","Cost"])

admin_file="admins.csv" # file used to store admin login credentials

#Creates admin file and add a default admin account if it does not exist
if not os.path.exists(admin_file):
    with open(admin_file, mode="w", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["username","password"])
        csv_writer.writerow(["admin","admin123"])

#Utility function
def clear_window(): #Clears all widgets to change screens
    for widget in root.winfo_children():
        widget.destroy()

#Main menu screen
def main_menu():
    clear_window()
    tk.Label(root,text="Commercial Property Management System",font=("Arial",16)).pack(pady=20)
    tk.Button(root,text="Login as Admin",width=20,command=admin_login).pack(pady=10)
    tk.Button(root,text="Login as User",width=20,command=user_menu).pack(pady=10)
    tk.Button(root,text="Exit",width=20,command=root.quit).pack(pady=10)

def admin_login():
    clear_window() #Clears previous screen before displaying admin login interface

    # Title Label for admin login screen
    tk.Label(root,text="Admin Login",font=("Arial",16)).pack(pady=20)
    tk.Label(root,text="Username").pack()
    username_entry=tk.Entry(root)
    username_entry.pack()

    tk.Label(root,text="Password").pack()
    password_entry=tk.Entry(root,show="*")
    password_entry.pack()

    def login():
        u = username_entry.get()
        p = password_entry.get()

        with open(admin_file, mode="r") as admin_csv:
            reader = csv.reader(admin_csv)
            next(reader) # skips header row
            for row in reader:
                if row[0] == u and row[1] == p:
                    messagebox.showinfo("Success", "Login Successful")
                    admin_menu()
                    return
        messagebox.showerror("Error", "Wrong details")
    tk.Button(root,text="Login",width=20,command=login).pack(pady=10)
    tk.Button(root,text="Exit",width=20,command=main_menu).pack()

#Admin menu screen
def admin_menu():
    clear_window()

    tk.Label(root,text="Admin Menu",font=("Arial",16)).pack(pady=20)
    tk.Button(root,text="Add Property",width=20,command=add_property).pack(pady=5)
    tk.Button(root,text="View Properties",width=20,command=view_properties).pack(pady=5)
    tk.Button(root,text="Search Properties",width=20,command=search_properties).pack(pady=5)
    tk.Button(root, text="Add Admins", width=20, command=add_admin).pack()
    tk.Button(root,text="Logout",width=20,command=main_menu).pack(pady=5)

#Add property screen
def add_property(): #Displays the interface used to enter new commercial property details
    clear_window()
    tk.Label(root,text="Add Property",font=("Arial",16)).pack(pady=10)

#Entry fields for property details
    type_entry=tk.Entry(root)
    floors_entry=tk.Entry(root)
    size_entry=tk.Entry(root)
    parking_entry=tk.Entry(root)
    availability_entry=tk.Entry(root)
    cost_entry=tk.Entry(root)

    fields=[
        ("Type",type_entry),
        ("Floors",floors_entry),
        ("Size (square meterage)",size_entry),
        ("Parking",parking_entry),
        ("Availability (Lease/Purchase/Both)",availability_entry),
        ("Cost (£)",cost_entry)
    ]

# Display all input fields
    for label, entry in fields:
        tk.Label(root,text=label).pack()
        entry.pack()

    def save_property():# Collects the user input from all fields and stores it.

        with open(file_name,mode="a",newline="") as csv_file:
            writer=csv.writer(csv_file)
            writer.writerow([
                type_entry.get().strip(),
                floors_entry.get(),
                size_entry.get(),
                parking_entry.get(),
                availability_entry.get(),
                cost_entry.get()
            ])

        messagebox.showinfo("Success","Property added successfully")
        admin_menu()
    tk.Button(root,text="Save Property",width=20,command=save_property).pack(pady=10)
    tk.Button(root,text="Back",width=20,command=admin_menu).pack(pady=10)

#View property screen
def view_properties(): # Displays all stored properties to the admin.
    clear_window()

    tk.Label(root,text="All Properties",font=("Arial",16)).pack(pady=10)

    frame=tk.Frame(root)
    frame.pack(fill="both",expand=True)

    with open(file_name,mode="r",newline="") as csv_file:
        reader=csv.reader(csv_file)
        next(reader)

        found=False
        for index,row in enumerate(reader,start=1):
            found=True
            prop_type,floors,size,parking,availability,cost=row

            text=(
                f"Property: {index}\n"
                f"Type:{prop_type}\n"
                f"Floors:{floors}\n"
                f"Size:{size} sqm\n"
                f"Parking: {parking}\n"
                f"Availability: {availability}\n"
                f"Cost: £{cost}\n"
                "-----------------------------------------"
            )

            tk.Label(root,text=text,justify="left").pack(anchor="w",padx=20,pady=5)
    if not found:
        tk.Label(frame,text="No properties available.").pack()

    tk.Button(root,text="Back",width=20,command=admin_menu).pack(pady=10)

#Search properties screen
def search_properties():
    # Searches for property based on property type
    # Matching properties are displayed and saved to an external text file.
    clear_window()

    tk.Label(root,text="Search property by type",font=("Arial",16)).pack(pady=10)
    tk.Label(root,text="Enter property type: ").pack()
    search_entry=tk.Entry(root)
    search_entry.pack(pady=5)

    result_frame = tk.Frame(root)
    result_frame.pack(fill="both",expand=True)

    def perform_search():
        for widget in result_frame.winfo_children():
            widget.destroy()
        search_type=search_entry.get().strip().lower()
        found=False

        with open(file_name,mode="r") as csv_file:
            reader=csv.reader(csv_file)
            next(reader)

            for row in reader:
                if row and row[0].strip().lower()==search_type:
                    found=True
                    prop_type,floors,size,parking,availability,cost = row

                    text = (
                        f"Type:{prop_type}\n"
                        f"Floors:{floors}\n"
                        f"Size:{size}\n"
                        f"Parking:{parking}\n"
                        f"Availability:{availability}\n"
                        f"Cost: {cost}\n"
                        "-------------------------------"
                    )

                    tk.Label(result_frame,text=text,justify="left").pack(anchor="w")
        if not found:
            tk.Label(result_frame,text="No properties available.").pack()

    tk.Button(root,text="Search Property",width=20,command=perform_search).pack(pady=5)
    tk.Button(root,text="Back",width=20,command=main_menu).pack(pady=10)

#Add new admin screen
def add_admin():
    clear_window()
    tk.Label(root,text="Add new Admin",font=("Arial",16)).pack(pady=10)

    tk.Label(root,text="Username").pack()
    username_entry=tk.Entry(root)
    username_entry.pack()
    tk.Label(root,text="Password").pack()
    password_entry=tk.Entry(root,show="*")
    password_entry.pack()

    def save_admin():
        with open(admin_file,mode="a",newline="") as admin_csv:
            writer = csv.writer(admin_csv)
            writer.writerow([username_entry.get(),password_entry.get()])
        messagebox.showinfo("Success","Admin added successfully")
        admin_menu()

    tk.Button(root,text="Save Admin",command=save_admin).pack(pady=10)
    tk.Button(root,text="Back",width=20,command=admin_menu).pack(pady=10)

#User menu screen
def user_menu():
    clear_window()

    tk.Label(root,text="User Menu",font=("Arial",16)).pack(pady=20)
    tk.Label(root,text="User Access (view & search only)").pack(pady=10)

    tk.Button(root,text="View properties",width=20,command=view_properties).pack(pady=10)
    tk.Button(root,text="Search Properties",width=20,command=search_properties).pack(pady=10)
    tk.Button(root,text="logout",width=20,command=main_menu).pack(pady=10)

#Program execution starts here
main_menu()
root.mainloop()


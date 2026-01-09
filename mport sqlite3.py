import sqlite3
from tkinter import *
from tkinter import messagebox

# Create or connect database
conn = sqlite3.connect('hospital.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS patient (
    pid INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    disease TEXT
)''')
conn.commit()

# GUI window
root = Tk()
root.title("Hospital Management System")
root.geometry("500x400")

# Add patient function
def add_patient():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    disease = entry_disease.get()

    if name == "" or age == "" or disease == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    c.execute("INSERT INTO patient (name, age, gender, disease) VALUES (?, ?, ?, ?)",
              (name, age, gender, disease))
    conn.commit()
    messagebox.showinfo("Success", "Patient added successfully!")
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    entry_disease.delete(0, END)

# View patients
def view_patients():
    top = Toplevel(root)
    top.title("Patient Records")
    records = c.execute("SELECT * FROM patient")
    for i, row in enumerate(records):
        Label(top, text=row).grid(row=i, column=0)

# Form labels and entries
Label(root, text="Patient Name").pack()
entry_name = Entry(root)
entry_name.pack()

Label(root, text="Age").pack()
entry_age = Entry(root)
entry_age.pack()

Label(root, text="Gender").pack()
gender_var = StringVar()
Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

Label(root, text="Disease").pack()
entry_disease = Entry(root)
entry_disease.pack()

Button(root, text="Add Patient", command=add_patient).pack(pady=10)
Button(root, text="View Patients", command=view_patients).pack(pady=10)

root.mainloop()
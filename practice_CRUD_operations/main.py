from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
from bson import ObjectId


client = MongoClient("mongodb+srv://esteban474sanchez:Yesteb@cluster0.rpbnucr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["PracticePython"]
collection = db["crud_operations"]

def refresh_list():
    listbox.delete(0, END)
    for student in collection.find():
        listbox.insert(END, f"{student.get('_id')} | {student['name']} | {student['age']} | {student['city']}")

def add_student():
    name = entry_name.get()
    age = entry_age.get()
    city = entry_city.get()
    if name and age and city:
        collection.insert_one({"name": name, "age": int(age), "city": city})
        refresh_list()
        entry_name.delete(0, END)
        entry_age.delete(0, END)
        entry_city.delete(0, END)
    else:
        messagebox.showwarning("Input Error", "All fields are required.")

def delete_student():
    selected = listbox.curselection()
    if selected:
        student_str = listbox.get(selected[0])
        student_id = student_str.split('|')[0].strip()
        collection.delete_one({"_id": ObjectId(student_id)})
        refresh_list()
    else:
        messagebox.showwarning("Selection Error", "Select a student to delete.")

def update_student():
    selected = listbox.curselection()
    if selected:
        student_str = listbox.get(selected[0])
        student_id = student_str.split('|')[0].strip()
        name = entry_name.get()
        age = entry_age.get()
        city = entry_city.get()
        if name and age and city:
            collection.update_one(
                {"_id": ObjectId(student_id)},  # Use ObjectId directly
                {"$set": {"name": name, "age": int(age), "city": city}}
            )
            refresh_list()
        else:
            messagebox.showwarning("Input Error", "All fields are required.")
    else:
        messagebox.showwarning("Selection Error", "Select a student to update.")

def fill_form(event):
    selected = listbox.curselection()
    if selected:
        student_str = listbox.get(selected[0])
        _, name, age, city = [s.strip() for s in student_str.split('|')]
        entry_name.delete(0, END)
        entry_name.insert(0, name)
        entry_age.delete(0, END)
        entry_age.insert(0, age)
        entry_city.delete(0, END)
        entry_city.insert(0, city)

window = Tk()
window.title("CRUD Operations")
window.geometry("500x400")

Label(window, text="Name").pack()
entry_name = Entry(window)
entry_name.pack()

Label(window, text="Age").pack()
entry_age = Entry(window)
entry_age.pack()

Label(window, text="City").pack()
entry_city = Entry(window)
entry_city.pack()

Button(window, text="Add", command=add_student).pack(pady=5)
Button(window, text="Update", command=update_student).pack(pady=5)
Button(window, text="Delete", command=delete_student).pack(pady=5)

listbox = Listbox(window, width=60)
listbox.pack(pady=10)
listbox.bind('<<ListboxSelect>>', fill_form)

refresh_list()
window.mainloop()
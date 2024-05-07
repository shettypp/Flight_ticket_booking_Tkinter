import tkinter as tk
from tkinter import messagebox
import sqlite3

con = sqlite3.connect("flights.db")
cur=con.cursor()
cur.execute("create table if not exists details(name text,contact integer,num integer,dest text,f_num integer,price integer)")

class_flights = {
    "Economy": (1000, ["1.IndiGo", "2.Air India"]),
    "Business": (2000, ["3.Air India Express", "4.spiceJet"]),
    "First Class": (3000, ["1.IndiGo", "4.spiceJet"])
}

def add_details(event=None):
    first_name = f_name_entry.get()
    last_name = l_name_entry.get()
    contact_number = contact_entry.get()
    email = email_entry.get()
    num_adults = adults_entry.get()
    num_children = children_entry.get()
    destination = destination_entry.get()
    date = date_entry.get()
    flight_class = class_var.get()
    av = class_flights[flight_class]
    flight_number = flight_num_entry.get()
    price = (av[0] * int(num_adults)) + ((av[0] / 2) * int(num_children))
    bill_text.config(state=tk.NORMAL)
    bill_text.delete('1.0', tk.END)
    bill_text.insert(tk.END, "Billing information:\n")
    bill_text.insert(tk.END, f"First Name: {first_name}\nLast Name: {last_name}\nContact Number: {contact_number}\nEmail: {email}\nNumber of Adults: {num_adults}\nNumber of Children: {num_children}\nDestination City: {destination}\nDate: {date}\nFlight Number: {flight_number}\nTotal Amount: rs{price}")
    bill_text.config(state=tk.DISABLED)
    messagebox.showinfo("Confirmed", f"Flight {flight_number} of {flight_class} is Booked")
    cur.execute("insert into details values(?, ?, ?, ?, ?, ?)", (first_name, int(contact_number), (int(num_adults) + int(num_children)), destination, int(flight_number), price))
    con.commit()

def filter_flights():
    flight_class = class_var.get()
    av = class_flights[flight_class]
    flights_text.config(state=tk.NORMAL)
    flights_text.delete('1.0', tk.END)
    flights_text.insert(tk.END, "Available Flights:\n")
    for i in av[1]:
        flights_text.insert(tk.END, f"Flight {i} available\n")
    flights_text.config(state=tk.DISABLED)

def booked_flights():
    cur.execute("select * from details")
    rows = cur.fetchall()
    book_text.config(state=tk.NORMAL)
    book_text.delete('1.0', tk.END)
    for i in rows:
        book_text.insert(tk.END, f"Name: {i[0]}\nContact Number: {i[1]}\nTotal passangers: {i[2]}\nDestination: {i[3]}\nFlight Number: {i[4]}\nTotal price: {i[5]}\n---------------\n")
    book_text.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Flight Booking")

details_frame = tk.LabelFrame(root, text="Customer Details", pady=10, padx=10)
details_frame.grid(row=0, column=0, padx=10, pady=10)

personal_label = tk.Label(details_frame, text="Personal Information")
personal_label.grid(row=0, column=0, columnspan=2)

f_name_label = tk.Label(details_frame, text="First name: ")
f_name_label.grid(row=1, column=0)

f_name_entry = tk.Entry(details_frame)
f_name_entry.grid(row=1, column=1)

l_name_label = tk.Label(details_frame, text="Last name: ")
l_name_label.grid(row=2, column=0)

l_name_entry = tk.Entry(details_frame)
l_name_entry.grid(row=2, column=1)

contact_label = tk.Label(details_frame, text="Contact number: ")
contact_label.grid(row=3, column=0)

contact_entry = tk.Entry(details_frame)
contact_entry.grid(row=3, column=1)

email_label = tk.Label(details_frame, text="Email: ")
email_label.grid(row=4, column=0)

email_entry = tk.Entry(details_frame)
email_entry.grid(row=4, column=1)

adults_label = tk.Label(details_frame, text="Number of Adults: ")
adults_label.grid(row=5, column=0)

adults_entry = tk.Entry(details_frame)
adults_entry.grid(row=5, column=1)

children_label = tk.Label(details_frame, text="Number of Children: ")
children_label.grid(row=6, column=0)

children_entry = tk.Entry(details_frame)
children_entry.grid(row=6, column=1)

destination_label = tk.Label(details_frame, text="Destination City: ")
destination_label.grid(row=7, column=0)

destination_entry = tk.Entry(details_frame)
destination_entry.grid(row=7, column=1)

date_label = tk.Label(details_frame, text="Date: ")
date_label.grid(row=8, column=0)

date_entry = tk.Entry(details_frame)
date_entry.grid(row=8, column=1)

flight_num_label = tk.Label(details_frame, text="Flight Number: ")  # Add flight number label
flight_num_label.grid(row=9, column=0)

flight_num_entry = tk.Entry(details_frame)  # Add entry for flight number
flight_num_entry.grid(row=9, column=1)

submit_btn = tk.Button(details_frame, text="Submit", command=add_details)
submit_btn.grid(row=10, column=0, columnspan=2)

filter_frame = tk.LabelFrame(root, text="Filter flights", padx=10, pady=10)
filter_frame.grid(row=0, column=1, padx=10, pady=10)

class_label = tk.Label(filter_frame, text="Class: ")
class_label.grid(row=0, column=0)

class_var = tk.StringVar() 
class_dropdown = tk.OptionMenu(filter_frame, class_var, "Economy", "Business", "First Class")
class_dropdown.grid(row=0, column=1)

filter_button = tk.Button(filter_frame, text="Find Flights", command=filter_flights)
filter_button.grid(row=1, column=0, columnspan=2)

flights_text = tk.Text(filter_frame, height=10, width=40, state=tk.DISABLED)
flights_text.grid(row=2, column=0, columnspan=2)

billing_frame = tk.LabelFrame(root, text="Billing information", pady=10, padx=10)
billing_frame.grid(row=1, column=0, padx=10, pady=10)

bill_text = tk.Text(billing_frame, height=10, width=40, state=tk.DISABLED)
bill_text.grid(row=0, column=0)

booked_frame = tk.LabelFrame(root, text="Booked Flights", pady=10, padx=10)
booked_frame.grid(row=1, column=1, padx=10, pady=10)

book_text = tk.Text(booked_frame, height=10, width=40, state=tk.DISABLED)
book_text.grid(row=0, column=0)

show_all = tk.Button(booked_frame, text="Show All", command=booked_flights)
show_all.grid(row=1, column=0, columnspan=2)

root.mainloop()

con.close()
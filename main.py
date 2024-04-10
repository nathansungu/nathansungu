import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
from display import input_records
from getvalue import query_values
import pymysql

global table
table = ['payment', 'drivers', 'loaders', 'vehicles', 'office staff', 'orders', 'members', 'vehicle_expense']


def change_dropdown(*args):
    viewrecords = tk.Tk()
    viewrecords.title("Flash Records")
    selected_table = tkvar.get()
    if selected_table == "payment":
        opent = 'SELECT * FROM payment;'
        cnames = ("Member_reg", "Order_no", "Payment_done", "Payment_mode", "Assigned_vehicle", "Distance")
        title = lbltitle = tk.Label(viewrecords, bd=1, relief=tk.RIDGE, text="Payment Records ", fg="black", bg="white",
                                    font=("Times new roman", 15,))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
    elif selected_table == "drivers":
        opent = 'SELECT * FROM drivers;'
        cnames = ("Driver_reg", "Category", "First_name", "Second_nam", "Id_no")
        title = lbltitle = tk.Label(viewrecords, bd=1, relief=tk.RIDGE, text="Drivers Records ", fg="black", bg="white",
                                    font=("Times new roman", 15,))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
    elif selected_table == "loaders":
        opent = 'SELECT * FROM loaders;'
        cnames = ("Loader_reg", "Category", "First_name", "Seconds_name", "Id_no")
        title = lbltitle = tk.Label(viewrecords, bd=1, relief=tk.RIDGE, text="Loaders Records ", fg="black", bg="white",
                                    font=("Times new roman", 15,))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
    elif selected_table == "vehicles":
        opent = 'SELECT * FROM vehicle;'
        cnames = ("Vehicle_reg", "Driver_reg", "Category", "Available")
        title = lbltitle = tk.Label(viewrecords, bd=1, relief=tk.RIDGE, text="Vehicles Records ", fg="black",
                                    bg="white",
                                    font=("Times new roman", 15,))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
    elif selected_table == "office staff":
        opent = 'SELECT * FROM `office staff`;'
        cnames = ("Staff_id", "Category", "First_Name", "Second_name", "ID_No")
        title = lbltitle = tk.Label(viewrecords, bd=1, relief=tk.RIDGE, text="Staff Records ", fg="black",
                                    bg="white",
                                    font=("Times new roman", 15,))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
    elif selected_table == "orders":
        opent = 'SELECT * FROM orders;'
        cnames = ("Order_no", "Member_reg", "Distance_KM", "Goods_type", "DateOrderd")
        title = lbltitle = tk.Label(viewrecords, bd=1, relief=tk.RIDGE, text="Orders Records ", fg="black",
                                    bg="white",
                                    font=("Times new roman", 15,))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
    elif selected_table == "members":
        opent = 'SELECT * FROM members;'
        cnames = ("Member_reg", "First_name", "Second_name", "Id_no")
        title = lbltitle = tk.Label(viewrecords, bd=1, relief=tk.RIDGE, text="Members Records ", fg="black",
                                    bg="white",
                                    font=("Times new roman", 15,))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
    else:
        opent = 'SELECT * FROM `vehicle expense`;'
        cnames = ("Category", "Tires_cost", "Fuel_km", "Service_cost")
        title = lbltitle = tk.Label(viewrecords, bd=1, relief=tk.RIDGE, text="Vehicle Expense Records ", fg="black",
                                    bg="white",
                                    font=("Times new roman", 15,))
        lbltitle.pack(side=tk.TOP, fill=tk.X)

    conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
    cursor = conn.cursor()
    query = opent
    cursor.execute(query)
    data = cursor.fetchall()
    columns = cnames
    title
    tree = ttk.Treeview(viewrecords, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    # Insert data into the Treeview
    for row in data:
        tree.insert("", "end", values=row)
    tree.pack()
    wrecords.destroy()

    def update_record():
        selected_item = tree.selection()
        if selected_item:
            selected_record = tree.item(selected_item, "values")
            primary_key = selected_record[0]
            update_window = tk.Toplevel(viewrecords)
            update_window.title("Update Record")
            entry_list = []
            for i, value in enumerate(selected_record):
                label = tk.Label(update_window, text=f"{cnames[i]}: ")
                label.grid(row=i, column=0)
                entry = tk.Entry(update_window)
                entry.grid(row=i, column=1)
                entry.insert(0, value)
                entry_list.append(entry)

            def update():
                try:
                    new_values = [entry.get() for entry in entry_list]
                    cursor = conn.cursor()
                    set_clause = ", ".join([f"{cnames[i]} = %s" for i in range(len(new_values))])
                    query = f"UPDATE `{selected_table}` SET {set_clause} WHERE `{cnames[0]}` = %s"
                    values = new_values + [primary_key]
                    cursor.execute(query, tuple(values))
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Success", "Record updated successfully")
                    viewrecords.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f": {e}")
            update_button = tk.Button(update_window, text="Update", command=update)
            update_button.grid(row=len(selected_record), columnspan=2)

        else:
            messagebox.showinfo("Action needed", "Select record to update")

    update_buttons = tk.Button(viewrecords, text="Update Record", command=update_record)
    update_buttons.pack()
    viewrecords.mainloop()


class expenditure:
    def drivers_pay(self):
        w =query_values()
        wdrivers = tk.Tk()
        wdrivers.title("Drivers Pay")
        lbltitle = tk.Label(wdrivers, bd=1, relief=tk.RIDGE, text="Drivers Pay Reports ", fg="black", bg="white",
                            font=("Times new roman", 15,))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()

        driverspay = 'SELECT `drivers`.`First_name`, `drivers`.`Second_nam`, `drivers`.`Id_no`, ' \
                     '`workers pay`.`Category`, `workers pay`.`Amount` FROM `drivers` LEFT JOIN ' \
                     '`workers pay` ON `drivers`.`Category` = `workers pay`.`Category`;'

        cursor.execute(driverspay)
        result = cursor.fetchall()
        columns = ("First name", "Second name", "ID No", "Category", "Amount",)
        tree = ttk.Treeview(wdrivers, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=250)



        for row in result:
            tree.insert("", "end", values=row)
        tree.pack()
        tree = ttk.Treeview(wdrivers, columns=('name', 'value'))
        tree.insert('', 'end', values=('Total', w.drivers_totalpay() ))
        tree.pack()

        cursor.close()
        conn.close()
        wdrivers.mainloop()

    def loaders_pay(self):
        wloarders = tk.Tk()
        wloarders.title("Loaders pay")
        lbltitle = tk.Label(wloarders, bd=1, relief=tk.RIDGE, text="Loaders Pay Reports ", fg="black", bg="white",
                            font=("Times new roman", 15,))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()
        loaderspay = 'SELECT `loaders`.`First_name`, `loaders`.`Second_name`, `loaders`.`Id_no`, ' \
                     '`workers pay`.`Category`, `workers pay`.`Amount` FROM `loaders` LEFT JOIN ' \
                     '`workers pay` ON `loaders`.`Category` = `workers pay`.`Category`;'
        cursor.execute(loaderspay)
        result = cursor.fetchall()
        columns = ("First name", "Second name", "ID No", "Category", "Amount",)
        tree = ttk.Treeview(wloarders, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=250)

        # Insert data into the Treeview

        for row in result:
            tree.insert("", "end", values=row)

        tree.pack()
        w = query_values()
        tree = ttk.Treeview(wloarders, columns=('name', 'value'))
        tree.insert('', 'end', values=('Total', w.loaders_totalpay()))
        tree.pack()
        cursor.close()
        conn.close()
        wloarders.mainloop()

    def staff_pay(self):
        wstaff = tk.Tk()
        wstaff.title("Staff Pay")
        lbltitle = tk.Label(wstaff, bd=1, relief=tk.RIDGE, text="Staff Pay Reports ", fg="black", bg="white",
                            font=("Times new roman", 15,))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()
        staffpay = 'SELECT `office staff`.`First_Name`, `office staff`.`Second_name`, `office staff`.`Staff_id`, ' \
                   '`workers pay`.`Category`, `workers pay`.`Amount` FROM `office staff` LEFT JOIN ' \
                   '`workers pay` ON `office staff`.`Category` = `workers pay`.`Category`;'
        cursor.execute(staffpay)
        result = cursor.fetchall()
        columns = ("First name", "Second name", "ID No", "Category", "Amount",)
        tree = ttk.Treeview(wstaff, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=250)

        # Insert data into the Treeview

        for row in result:
            tree.insert("", "end", values=row)

        tree.pack()
        w = query_values()
        tree = ttk.Treeview(wstaff, columns=('name', 'value'))
        tree.insert('', 'end', values=('Total', w.staff_totalpay()))
        tree.pack()
        cursor.close()
        conn.close()
        wstaff.mainloop()

    def vehicletotal(self):
        y = query_values()
        # multiply the distance coverd with the cost of fuel per km
        fuel_cost = float(y.sum_Distance() * 100)
        # add fuel and service cost
        Vehicle_cost = fuel_cost + float(y.totalservice_cost()) + float(y.tires_cost())
        return Vehicle_cost

    def workersvehicletotals(self):
        w = query_values()
        total = float(w.drivers_totalpay()) + float(w.loaders_totalpay()) + float(w.staff_totalpay()) + float(self.vehicletotal())
        return total

    def total_expenditure(self):
        y = query_values()
        try:
            totalwind = tk.Tk()
            totalwind.title("Total Spendings")
            lbltitle = tk.Label(totalwind, bd=1, relief=tk.RIDGE, text="Total Employees and vehicle Expenditure", fg="black", bg="white",
                            font=("Times new roman", 15,))
            lbltitle.pack(side=tk.TOP, fill=tk.X)
            tree = ttk.Treeview(totalwind, columns=('name', 'value'), show='headings')
            tree.heading('name', text='Category')
            tree.heading('value', text='Total Amount')

            tree.insert('', 'end', values=('Drivers', y.drivers_totalpay()))
            tree.insert('', 'end', values=('Loader', y.loaders_totalpay()))
            tree.insert('', 'end', values=('Staff', y.staff_totalpay()))
            tree.insert('', 'end', values=('Vehicle ', self.vehicletotal()))
            tree.insert('', 'end', values=('Total', self.workersvehicletotals()))
            tree.insert('', 'end', values=('profite', self.profit()))


            tree.pack()
            totalwind.mainloop()
        except:
            #totalwind.destroy()
            messagebox.showinfo("Action needed", "please view all of the above reports to proceed ")
    def revenue(self):
        y= query_values()
        revenue = y.sum_Distance() * y.cost_km()
        return revenue
    def profit(self):
        y = query_values()
        global charges
        charges = float(y.sum_Distance() * y.cost_km())
        profite_made = charges - self.workersvehicletotals()
        return profite_made

    def profite_report(self):
        y = query_values()
        totalwind = tk.Tk()
        totalwind.title("Total Spendings")
        lbltitle = tk.Label(totalwind, bd=1, relief=tk.RIDGE, text="PROFIT MADE",
                                fg="black", bg="white",
                                font=("Times new roman", 15,))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
        tree = ttk.Treeview(totalwind, columns=('name', 'value'), show='headings')
        tree.heading('name', text='Category')
        tree.heading('value', text='Total Amount')

        tree.insert('', 'end', values=('Distance Coverd', y.sum_Distance()))
        tree.insert('', 'end', values=('Cost per KM ', y.cost_km()))
        tree.insert('', 'end', values=('Revenue Collected', self.revenue()))
        tree.insert('', 'end', values=('Spending', self.workersvehicletotals()))
        tree.insert('', 'end', values=('Profit', self.profit()))

        tree.pack()
        totalwind.mainloop()


    def spend_buttons(self):
        global wroot
        wroot = tk.Tk()
        wroot.title("Reports")
        lbltitle = tk.Label(wroot, bd=3, relief=tk.RIDGE, text="Flash Transport Reports ", fg="gold", bg="black",
                            font=("Times new roman", 35, "bold"))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
        driverpay = tk.Button(wroot, text="Drivers pay", command=self.drivers_pay)
        driverpay.place(x=300, y=100)

        loaderpay = tk.Button(wroot, text="loaders", command=self.loaders_pay)
        loaderpay.place(x=300, y=200)

        staffpay = tk.Button(wroot, text="staff", command=self.staff_pay)
        staffpay.place(x=300, y=150)

        totalexp = tk.Button(wroot, text="Total expenditure", command=self.total_expenditure)
        totalexp.place(x=300, y=250)

        profitbutton = tk.Button(wroot, text="Profit", command=self.profite_report)
        profitbutton.place(x=300, y=300)

        wroot.mainloop()


def rootmain():
    global root
    root = tk.Tk()
    root.title("Main Window")
    root.configure(bg="black")
    lbltitle = tk.Label(root, bd=4, relief=tk.RIDGE, text="Flash Transport Main Window ", fg="gold", bg="blue",
                        font=("Times new roman", 40, "italic"))
    lbltitle.pack(side=tk.TOP, fill=tk.X)
    pay = expenditure()
    update = input_records()

    label_select = tk.Label(root, text="Select Record to open")
    label_select.place(x=1000, y=200)

    def records():
        global wrecords
        wrecords = tk.Tk()
        wrecords.title("View Records")
        wrecords.configure(background="black")
        lbltitle = tk.Label(wrecords, bd=2, relief=tk.RIDGE, text="Flash Transport Records ", fg="gold", bg="black",
                            font=("Times new roman", 25))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
        lablewelcome = tk.Label(wrecords, bd=2, relief=tk.RIDGE,
                                text="Welcome to Flash transport company records. Select record to open ",
                                fg="black", bg="white",
                                font=("Times new roman", 15, "italic"))
        lablewelcome.pack()
        lbltitle.pack(side=tk.TOP, fill=tk.X)
        global tkvar
        tkvar = tk.StringVar(wrecords)
        tkvar.set(table[0])
        table_dropdown = tk.OptionMenu(wrecords, tkvar, *table)
        table_dropdown.place(x=300, y=350)
        table_button = tk.Button(root, text="View Records", command=tkvar.trace('w', change_dropdown))
        wrecords.mainloop()

    records = tk.Button(root, text="View Records", command=records)
    records.place(x=1000, y=250)

    Expe = tk.Button(root, text="View Reports", command=pay.spend_buttons)
    Expe.place(x=300, y=200)

    membersbutton = tk.Button(root, text="Register Member", command=update.members_layout)
    membersbutton.place(x=300, y=250)

    ordersbutton = tk.Button(root, text="Make order ", command=update.o_layout)
    ordersbutton.place(x=100, y=200)

    updatebutton = tk.Button(root, text="Add Employee", command=update.inputbuttons)
    updatebutton.place(x=100, y=250)
    vehiclebutton = tk.Button(root, text="Add Vehicle", command=update.v_layout)
    vehiclebutton.place(x=100, y=300)

    root.mainloop()


def check_password():
    passkey = query_values()
    entered_password = password_entry.get()
    stored_password = passkey.get_passord()

    if entered_password == stored_password:
        messagebox.showinfo("Successfully", "Correct password")
        close = login()
        close.closeapp()
        rootmain()
    else:

        messagebox.showerror("Error", "Incorrect password. Try again.")


class login:
    def loginn(self):
        global password_entry
        lablewelcome = tk.Label(app, bd=2, relief=tk.RIDGE,
                                text="Welcome to Flash transport company. Enter password to continue. ",
                                fg="black", bg="white",
                                font=("Times new roman", 20, "italic"))
        lablewelcome.pack()

        lablepassword = tk.Label(app, text="Enter Password ")
        lablepassword.place(x=600, y=150)

        password_entry = tk.Entry(app, show="*")
        password_entry.place(x=600, y=200)

        # Create a button to submit the password
        submit_button = tk.Button(app, text="LOG IN", width=15, height=2, command=check_password)
        submit_button.place(x=600, y=250)

    def closeapp(self):
        app.destroy()


global app
app = tk.Tk()
app.configure(bg="grey")
app.title("FLASH TRANSPORT SYSTEM")
lbltitle = tk.Label(app, bd=2, relief=tk.RIDGE, text="Flash Transport System", fg="black", bg="brown",
                    font=("Times new roman", 45, "bold"))
lbltitle.pack(side=tk.TOP, fill=tk.X)
backimage = ImageTk.PhotoImage(file='truck.jpg')
bgLabel = tk.Label(app, image=backimage)
bgLabel.place(x=100, y=150)

right_image = ImageTk.PhotoImage(file='lorry.jpg')
rhtlabel = tk.Label(app, image=right_image)
rhtlabel.place()

lgin = login()
lgin.loginn()
Close_button = tk.Button(app, text="Close", width=15, height=2, command=lgin.closeapp)
Close_button.place(x=1000, y=250)
app.mainloop()

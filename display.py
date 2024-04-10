import tkinter as tk

import pymysql
from tkinter import messagebox
global root
class input_records:

    def E_drivers(self):
        # get input from user
        reg = entry_reg.get()
        cat = entry_dcat.get()
        fname = entry_fname.get()
        sname = entry_sname.get()
        Id_no = entry_idno.get()

        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()
        query = 'INSERT INTO `drivers`(`Driver_reg`, `Category`, `First_name`, `Second_nam`, `Id_no`)VALUES(%s,%s,%s,%s,%s)'
        values = (reg, cat, fname, sname, Id_no)
        try:
            # Execute the query
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Successfully", "Record saved")

        except Exception as e:
            messagebox.showerror("Error", f": {e}")

        conn.rollback()
        # Close the database connection
        conn.close()

    def layout(self):
        root = tk.Tk()
        root.title("Save Data to Database")

        # Create input fields
        label_reg = tk.Label(root, text="reg:")
        global entry_reg
        entry_reg = tk.Entry(root)
        label_cat = tk.Label(root, text="Category:")
        global entry_dcat
        entry_dcat = tk.Entry(root)
        label_fname = tk.Label(root, text="First name:")
        global entry_fname
        entry_fname = tk.Entry(root)
        label_sname = tk.Label(root, text="Second name:")
        global entry_sname
        entry_sname = tk.Entry(root)
        label_idno = tk.Label(root, text="Id no:")
        global entry_idno
        entry_idno = tk.Entry(root)

        # Create a button to save data
        button_save = tk.Button(root, text="Save", command=self.E_drivers)

        # Grid layout
        label_reg.grid(row=0, column=0, padx=10, pady=5)
        entry_reg.grid(row=0, column=1, padx=10, pady=5)
        label_cat.grid(row=1, column=0, padx=10, pady=5)
        entry_dcat.grid(row=1, column=1, padx=10, pady=5)
        label_fname.grid(row=2, column=0, padx=10, pady=5)
        entry_fname.grid(row=2, column=1, padx=10, pady=5)
        label_sname.grid(row=3, column=0, padx=10, pady=5)
        entry_sname.grid(row=3, column=1, padx=10, pady=5)
        label_idno.grid(row=4, column=0, padx=10, pady=5)
        entry_idno.grid(row=4, column=1, padx=10, pady=5)
        button_save.grid(row=5, columnspan=2, padx=10, pady=10)

        root.mainloop()

    def E_loaders(self):
        # get input from user
        reg = entry_reg.get()
        cat = entry_lcat.get()
        fname = entry_fname.get()
        sname = entry_sname.get()
        Id_no = entry_idno.get()

        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()
        query = 'INSERT INTO `loaders`(`Loader_reg`, `Category`, `First_name`, `Second_name`, `Id_no`)VALUES(%s,%s,%s,%s,%s)'
        values = (reg, cat, fname, sname, Id_no)
        try:
            # Execute the query
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Successfully", "Record saved")

        except Exception as e:
            messagebox.showerror("Error", f": {e}")

        conn.rollback()
        # Close the database connection
        conn.close()

    def l_layout(self):
        root = tk.Tk()
        root.title("Save Data to Database")

        # Create input fields
        label_reg = tk.Label(root, text="reg:")
        global entry_reg
        entry_reg = tk.Entry(root)
        label_cat = tk.Label(root, text="Category:")
        global entry_lcat
        entry_lcat = tk.Entry(root)
        label_fname = tk.Label(root, text="First name:")
        global entry_fname
        entry_fname = tk.Entry(root)
        label_sname = tk.Label(root, text="Second name:")
        global entry_sname
        entry_sname = tk.Entry(root)
        label_idno = tk.Label(root, text="Id no:")
        global entry_idno
        entry_idno = tk.Entry(root)

        # Create a button to save data
        button_save = tk.Button(root, text="Save", command=self.E_loaders)

        # Grid layout
        label_reg.grid(row=0, column=0, padx=10, pady=5)
        entry_reg.grid(row=0, column=1, padx=10, pady=5)
        label_cat.grid(row=1, column=0, padx=10, pady=5)
        entry_lcat.grid(row=1, column=1, padx=10, pady=5)
        label_fname.grid(row=2, column=0, padx=10, pady=5)
        entry_fname.grid(row=2, column=1, padx=10, pady=5)
        label_sname.grid(row=3, column=0, padx=10, pady=5)
        entry_sname.grid(row=3, column=1, padx=10, pady=5)
        label_idno.grid(row=4, column=0, padx=10, pady=5)
        entry_idno.grid(row=4, column=1, padx=10, pady=5)
        button_save.grid(row=5, columnspan=2, padx=10, pady=10)

        root.mainloop()

    def E_staff(self):
        # get input from user
        reg = entry_reg.get()
        cat = entry_scat.get()
        fname = entry_fname.get()
        sname = entry_sname.get()


        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()
        query = 'INSERT INTO `office staff`(`Staff_id`, `Category`, `First_Name`, `Second_name`, `ID_NO`)'
        values = (reg, cat, fname, sname,)
        try:
            # Execute the query
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Successfully", "Record saved")

        except Exception as e:
            messagebox.showerror("Error", f": {e}")

        conn.rollback()
        # Close the database connection
        conn.close()

    def s_layout(self):
        root = tk.Tk()
        root.title("Save Data to Database")

        # Create input fields
        label_reg = tk.Label(root, text="reg:")
        global entry_reg
        entry_reg = tk.Entry(root)
        label_cat = tk.Label(root, text="Category:")
        global entry_scat
        entry_scat = tk.Entry(root)
        label_fname = tk.Label(root, text="First name:")
        global entry_fname
        entry_fname = tk.Entry(root)
        label_sname = tk.Label(root, text="Second name:")
        global entry_sname
        entry_sname = tk.Entry(root)

        # Create a button to save data
        button_save = tk.Button(root, text="Save", command=self.E_staff)

        # Grid layout
        label_reg.grid(row=0, column=0, padx=10, pady=5)
        entry_reg.grid(row=0, column=1, padx=10, pady=5)
        label_cat.grid(row=1, column=0, padx=10, pady=5)
        entry_scat.grid(row=1, column=1, padx=10, pady=5)
        label_fname.grid(row=2, column=0, padx=10, pady=5)
        entry_fname.grid(row=2, column=1, padx=10, pady=5)
        label_sname.grid(row=3, column=0, padx=10, pady=5)
        entry_sname.grid(row=3, column=1, padx=10, pady=5)
        button_save.grid(row=5, columnspan=2, padx=10, pady=10)

        root.mainloop()

    def E_members(self):
        # get input from user
        reg = entry_reg.get()
        fname = entry_fname.get()
        sname = entry_sname.get()
        Id_no = entry_idno.get()

        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()
        query = 'INSERT INTO `members`(`Member_reg`, `First_name`, `Second_name`, `Id_no`)VALUES(%s,%s,%s,%s)'
        values = (reg, fname, sname, Id_no)
        try:
            # Execute the query
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Successfully", "Record saved")

        except Exception as e:
            messagebox.showerror("Error", f": {e}")

        conn.rollback()
        # Close the database connection
        conn.close()

    def members_layout(self):
        root = tk.Tk()
        root.title("Save Data to Database")

        # Create input fields
        label_reg = tk.Label(root, text="Member reg:")
        global entry_reg
        entry_reg = tk.Entry(root)
        label_fname = tk.Label(root, text="First name:")
        global entry_fname
        entry_fname = tk.Entry(root)
        label_sname = tk.Label(root, text="Second name:")
        global entry_sname
        entry_sname = tk.Entry(root)
        label_idno = tk.Label(root, text="Id no:")
        global entry_idno
        entry_idno = tk.Entry(root)

        # Create a button to save data
        button_save = tk.Button(root, text="Save", command=self.E_members)

        # Grid layout
        label_reg.grid(row=0, column=0, padx=10, pady=5)
        entry_reg.grid(row=0, column=1, padx=10, pady=5)
        label_fname.grid(row=2, column=0, padx=10, pady=5)
        entry_fname.grid(row=2, column=1, padx=10, pady=5)
        label_sname.grid(row=3, column=0, padx=10, pady=5)
        entry_sname.grid(row=3, column=1, padx=10, pady=5)
        label_idno.grid(row=4, column=0, padx=10, pady=5)
        entry_idno.grid(row=4, column=1, padx=10, pady=5)
        button_save.grid(row=5, columnspan=2, padx=10, pady=10)

        root.mainloop()
    def E_order(self):
        # get input from user
        order = entry_orderno.get()
        reg = entry_reg.get()
        distance = entry_distance.get()
        goods_type = entry_goods_type.get()
        date_ordered = entry_date_ordered.get()

        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()
        query = 'INSERT INTO `orders`(`Order_no`, `Member_reg`, `Distance_KM`, `Goods_type`, `DateOrderd`)VALUES(%s,%s,%s,%s,%s)'
        values = (order, reg, distance, goods_type, date_ordered)
        try:
            # Execute the query
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Successfully", "Record saved")

        except Exception as e:
            messagebox.showerror("Error", f": {e}")

        conn.rollback()
        # Close the database connection
        conn.close()

    def o_layout(self):
        root = tk.Tk()
        root.title("Save Data to Database")

        # Create input fields
        label_order = tk.Label(root, text="Order no:")
        global entry_orderno
        entry_orderno= tk.Entry(root)
        label_reg = tk.Label(root, text="reg:")
        global entry_reg
        entry_reg = tk.Entry(root)
        label_cat = tk.Label(root, text="Category:")
        global entry_cat
        entry_cat = tk.Entry(root)
        label_distance = tk.Label(root, text="Distance:")
        global entry_distance
        entry_distance = tk.Entry(root)
        label_goods = tk.Label(root, text="Type of goods:")
        global entry_goods_type
        entry_goods_type = tk.Entry(root)
        label_date = tk.Label(root, text="Date:")
        global entry_date_ordered
        entry_date_ordered = tk.Entry(root)

        # Create a button to save data
        button_save = tk.Button(root, text="Save", command=self.E_order)

        # Grid layout
        label_order.grid(row=0, column=0, padx=10, pady=5)
        entry_orderno.grid(row=0, column=1, padx=10, pady=5)
        label_reg.grid(row=1, column=0, padx=10, pady=5)
        entry_reg.grid(row=1, column=1, padx=10, pady=5)
        label_distance.grid(row=2, column=0, padx=10, pady=5)
        entry_distance.grid(row=2, column=1, padx=10, pady=5)
        label_goods.grid(row=3, column=0, padx=10, pady=5)
        entry_goods_type.grid(row=3, column=1, padx=10, pady=5)
        label_date.grid(row=4, column=0, padx=10, pady=5)
        entry_date_ordered.grid(row=4, column=1, padx=10, pady=5)
        button_save.grid(row=5, columnspan=2, padx=10, pady=10)

        root.mainloop()
    def E_vehicle(self):
        # get input from user
        vreg = Vehicle_reg.get()
        dreg = Driver_reg.get()
        category = Category.get()
        available = Available.get()


        conn = pymysql.connect(user='root', password='', host='localhost', database='transport company')
        cursor = conn.cursor()
        query = 'INSERT INTO `vehicle`(`Vehicle_reg`, `Driver_reg`, `Category`, `Available`)VALUES(%s,%s,%s,%s)'
        values = (vreg, dreg, category, available)
        try:
            # Execute the query
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Successfully", "Record saved")

        except Exception as e:
            messagebox.showerror("Error", f": {e}")

        conn.rollback()
        # Close the database connection
        conn.close()

    def v_layout(self):
        root = tk.Tk()
        root.title("Save Data to Database")

        # Create input fields
        label_vreg = tk.Label(root, text="Vehicle reg:")
        global Vehicle_reg
        Vehicle_reg = tk.Entry(root)
        label_dreg = tk.Label(root, text="Driver reg:")
        global Driver_reg
        Driver_reg = tk.Entry(root)
        label_cat = tk.Label(root, text="Category:")
        global Category
        Category = tk.Entry(root)
        label_available = tk.Label(root, text="Available:")
        global Available
        Available = tk.Entry(root)


        # Create a button to save data
        button_save = tk.Button(root, text="Save", command=self.E_vehicle)

        # Grid layout
        label_vreg.grid(row=0, column=0, padx=10, pady=5)
        Vehicle_reg.grid(row=0, column=1, padx=10, pady=5)
        label_dreg.grid(row=1, column=0, padx=10, pady=5)
        Driver_reg.grid(row=1, column=1, padx=10, pady=5)
        label_cat.grid(row=2, column=0, padx=10, pady=5)
        Category.grid(row=2, column=1, padx=10, pady=5)
        label_available.grid(row=3, column=0, padx=10, pady=5)
        Available.grid(row=3, column=1, padx=10, pady=5)
        button_save.grid(row=5, columnspan=2, padx=10, pady=10)

        root.mainloop()

    def inputbuttons(self):
        root = tk.Tk()
        root.title("CATEGORY")
        lbltitle = tk.Label(root, bd=3, relief=tk.RIDGE, text="Flash Transport Employees ", fg="gold", bg="black",
                            font=("Times new roman", 35, "bold"))
        lbltitle.pack(side=tk.TOP, fill=tk.X)
        lbltitle = tk.Label(root, bd=1, relief=tk.RIDGE, text="Click On Record To Add ", fg="gold", bg="black",
                            font=("Times new roman", 20, "italic"))
        lbltitle.place(x=300, y=400)


        drivers = tk.Button(root, text="Drivers", command=self.layout)
        drivers.place(x=300, y=250)
        loaders = tk.Button(root, text="Loaders", command=self.l_layout)
        loaders.place(x=300, y=200)
        staff = tk.Button(root, text="Staff", command=self.s_layout)
        staff.place(x=300, y=150)


        root.mainloop()
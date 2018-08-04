import tkinter
from  tkinter import *
import os
import tkinter as tk
import pymysql
import collections
import random

dataF = []
data0 = ["ID", "Age", "Gender", "Ethnicity", "Income", "Family", "Political Affiliation", "Religion", "Education"]
dataFilter0 = []
dataT = [data0]
dataMinMax = [data0]
Table = "Placeholder"
BS = ""
BSNum = 0
Filter = False

#This code won't do much without a database set. Suffice to say, a simple MySQL table should work once the parameters are met however.

class ExampleApp(Tk):  ##Makes Table and buttons come together
    def __init__(self):
        tk.Tk.__init__(self)
        t = test(self)
        t.pack(side="top", fill="x")
        def clock():
            self.after(10, clock)

class ButtonApp(tk.Tk):  ##Opening code
    def __init__(self, root):
        scrollbar = Scrollbar()
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(yscrollcommand=scrollbar.set)
        mbutton = Menubutton(text='Database')
        picks = Menu(mbutton)
        mbutton.config(menu=picks)
        picks.add_command(label='Default Database', command=NameSet1)
        picks.add_command(label='Test Database', command=NameSet2)
        mbutton.place(anchor=S)
        mbutton.pack(padx=4, pady=3, side=LEFT)

class CutWindow(tk.Tk):
    def __init__(self, root):
        def enter_click(event):
            x = str(value_entry.get())
            print(x)
            col = str(col_entry.get())

            if (x != ""):
                print(len(dataT))
                conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='****', db=Table,
                                       autocommit=True)
                cur = conn.cursor()
                cur.execute("DELETE FROM " + Table + " WHERE '" + col + "' = " + x + "'")
                cur.close()
                conn.close()
                value_entry.delete(0, END)
                col_entry.delete(0, END)
                # DefaultDatabase()

            else:
                print("Error")

        def finish_click(event):
            DefaultDatabase()

        value_entry = Entry(root)
        value_entry.pack()
        col_entry = Entry(root)
        col_entry.pack()

        enter_button = Button(root, text="Enter")
        enter_button.pack()
        enter_button.bind("<Button-1>", enter_click)
        enter_button.bind("<Return>", enter_click)
        finish_button = Button(root, text="Finish")
        finish_button.pack()
        finish_button.bind("<Button-1>", finish_click)
        finish_button.bind("<Return>", enter_click)

class AddWindow(tk.Tk):
    def __init__(self, root):
        global DataT

        def enter_click(event):
            NewAge = str(Age_entry.get())
            NewGen = str(Gen_entry.get())
            NewEth = str(Eth_entry.get())
            NewIn = str(Income_entry.get())
            NewFam = str(Family_entry.get())
            NewPol = str(Pol_entry.get())
            NewRel = str(Rel_entry.get())
            NewEdu = str(Edu_entry.get())

            if ((NewAge) == ""):
                NewAge = "'NA'"
            else:
                NewAge = "'" + NewAge + "'"

            if ((NewGen) == ""):
                NewGen = "'NA'"
            else:
                NewGen = "'" + NewGen + "'"

            if ((NewEth) == ""):
                NewEth = "'NA'"
            else:
                NewEth = "'" + NewEth + "'"

            if ((NewIn) == ""):
                NewIn = "'NA'"
            else:
                NewIn = "'" + NewIn + "'"

            if ((NewFam) == ""):
                NewFam = "'NA'"
            else:
                NewFam = "'" + NewFam + "'"

            if ((NewPol) == ""):
                NewPol = "'NA'"
            else:
                NewPol = "'" + NewPol + "'"

            if ((NewRel) == ""):
                NewRel = "'NA'"
            else:
                NewRel = "'" + NewRel + "'"

            if ((NewEdu) == ""):
                NewEdu = "'NA'"
            else:
                NewEdu = "'" + NewEdu + "'"

            conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='****', db=Table,
                                   autocommit=True)
            cur = conn.cursor()

            cur.execute(
                "insert into " + Table + " (id, Age, Gender, Ethnicity, Income, Family, Political, Religion, Education) values (" + str(
                    len(
                        dataT)) + ", " + NewAge + ", " + NewGen + ", " + NewEth + ", " + NewIn + ", " + NewFam + ", " + NewPol + ", " + NewRel + ", " + NewEdu + ");")
            cur.execute(
                "SELECT id, Age, Gender, Ethnicity, Income, Family, Political, Religion, Education FROM " + Table)

            print(len(dataT))
            dataF = []
            for row in cur:
                print(row)
                for col in row:
                    dataF.append(col)
                dataT.append(dataF)
                dataF = []
                dataP = row
            print(len(dataT))
            cur.close()
            conn.close()
            Age_entry.delete(0, END)
            Gen_entry.delete(0, END)
            Eth_entry.delete(0, END)
            Income_entry.delete(0, END)
            Family_entry.delete(0, END)
            Pol_entry.delete(0, END)
            Rel_entry.delete(0, END)
            Edu_entry.delete(0, END)
            ExampleApp.clock()

        def quit():
            self.root.destroy()

        Age_label = Label(root, text="Age")
        Gen_label = Label(root, text="Gender")
        Eth_label = Label(root, text="Ethnicity")
        Income_label = Label(root, text="Income")
        Family_label = Label(root, text="Family")
        Pol_label = Label(root, text="Political Affiliaton")
        Rel_label = Label(root, text="Religion")
        Edu_label = Label(root, text="Education")

        Age_entry = Entry(root)
        Gen_entry = Entry(root)
        Eth_entry = Entry(root)
        Income_entry = Entry(root)
        Family_entry = Entry(root)
        Pol_entry = Entry(root)
        Rel_entry = Entry(root)
        Edu_entry = Entry(root)

        Age_label.pack()
        Age_entry.pack()
        Gen_label.pack()
        Gen_entry.pack()
        Eth_label.pack()
        Eth_entry.pack()
        Income_label.pack()
        Income_entry.pack()
        Family_label.pack()
        Family_entry.pack()
        Pol_label.pack()
        Pol_entry.pack()
        Rel_label.pack()
        Rel_entry.pack()
        Edu_label.pack()
        Edu_entry.pack()

        enter_button = Button(root, text="Enter")
        enter_button.pack()
        enter_button.bind("<Button-1>", enter_click)
        enter_button.bind("<Return>", enter_click)

class UpdateWindow(tk.Tk):
    def __init__(self, root):
        def enter_click(event):
            print("Yay")
            OldE = str(Old_Entry.get())
            OldE = "'" + OldE + "'"
            NewE = str(New_Entry.get())
            NewE = "'" + NewE + "'"
            Row = str(Row_Entry.get())


            conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='****', db=Table,
                                   autocommit=True)
            cur = conn.cursor()
            cur.execute("update " + Table + " set " + Row + " = " + NewE + " where " + Row + " = " + OldE)



            cur.close()
            conn.close()


        Row_Entry = Entry(root)
        Old_Entry = Entry(root)
        New_Entry = Entry(root)
        Extra_Param1 = Entry(root)
        Extra_Param2 = Entry(root)
        Old_Label = Label(root, text="Old Label")
        New_Label = Label(root, text="New Label")
        Row_Label = Label(root, text="Row changed")
        E1 = Label(root, text="Specific Col Change")
        E2 = Label(root, text="Specific Col Quality")


        Old_Label.pack()
        Old_Entry.pack()
        New_Label.pack()
        New_Entry.pack()
        Row_Label.pack()
        Row_Entry.pack()


        enter_button = Button(root, text="Enter")
        enter_button.pack()
        enter_button.bind("<Button-1>", enter_click)
        enter_button.bind("Return", enter_click)

class FilterWindow(tk.Tk):
    def __init__(self, root):
        def enter_click(event):
            global BS
            global dataFilter0
            datalol = []
            BS = ("Select ")

            NewID = str(ID_entry.get())
            NewAge = str(Age_entry.get())
            NewGen = str(Gen_entry.get())
            NewEth = str(Eth_entry.get())
            NewIn = str(Income_entry.get())
            NewFam = str(Family_entry.get())
            NewPol = str(Pol_entry.get())
            NewRel = str(Rel_entry.get())
            NewEdu = str(Edu_entry.get())

            # cur.execute("SELECT id, Age, Gender, Ethnicity, Income, Family, Political, Religion, Education FROM " + Table)

            if (NewID != ""):
                BS += ("id, ")
                datalol.append("ID")

            if ((NewAge) != ""):
                BS += ("Age, ")
                datalol.append("Age")
            if ((NewGen) != ""):
                BS += ("Gender, ")
                datalol.append("Gender")
            if ((NewEth) != ""):
                BS += ("Ethnicity, ")
                datalol.append("Ethnicity")
            if ((NewIn) != ""):
                BS += ("Income, ")
                datalol.append("Income")
            if ((NewFam) != ""):
                BS += ("Family, ")
                datalol.append("Family")
            if ((NewPol) != ""):
                BS += ("Political, ")
                datalol.append("Political")
            if ((NewRel) != ""):
                BS += ("Religion, ")
                datalol.append("Religion")
            if ((NewEdu) != ""):
                BS += ("Education, ")
                datalol.append("Education")

            print(datalol)
            dataFilter0 = datalol
            BS = BS[0:len(BS) - 2]
            BS = BS + (" FROM " + Table)
            print(BS)

            tk.Tk.__init__(self)
            t = FilterTable(self)

        ID_label = Label(root, text="ID")
        Age_label = Label(root, text="Age")
        Gen_label = Label(root, text="Gender")
        Eth_label = Label(root, text="Ethnicity")
        Income_label = Label(root, text="Income")
        Family_label = Label(root, text="Family")
        Pol_label = Label(root, text="Political Affiliaton")
        Rel_label = Label(root, text="Religion")
        Edu_label = Label(root, text="Education")

        ID_entry = Entry(root)
        Age_entry = Entry(root)
        Gen_entry = Entry(root)
        Eth_entry = Entry(root)
        Income_entry = Entry(root)
        Family_entry = Entry(root)
        Pol_entry = Entry(root)
        Rel_entry = Entry(root)
        Edu_entry = Entry(root)

        ID_label.pack()
        ID_entry.pack()
        Age_label.pack()
        Age_entry.pack()
        Gen_label.pack()
        Gen_entry.pack()
        Eth_label.pack()
        Eth_entry.pack()
        Income_label.pack()
        Income_entry.pack()
        Family_label.pack()
        Family_entry.pack()
        Pol_label.pack()
        Pol_entry.pack()
        Rel_label.pack()
        Rel_entry.pack()
        Edu_label.pack()
        Edu_entry.pack()

        enter_button = Button(root, text="Enter")
        enter_button.pack()
        enter_button.bind("<Button-1>", enter_click)
        enter_button.bind("Return", enter_click)

class Update(Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = UpdateWindow(self)

class Delete(Tk):  ##Delete Row. No User Input
    def __init__(self):
        tk.Tk.__init__(self)
        t = CutWindow(self)

class Add(Tk):  ##Adds line. No user input atm.
    def __init__(self):
        tk.Tk.__init__(self)
        t = AddWindow(self)

class Filter(Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = FilterWindow(self)

class MaxFind(Tk):  ##Finds Most Reccuring Value
    def __init__(self):

        global Table
        global dataMinMax
        global data0

        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='****', db=Table, autocommit=True)
        cur = conn.cursor()
        Age = []
        Gender = []
        Eth = []
        Income = []
        Family = []
        Pol = []
        Rel = []
        Edu = []

        AgeP = []
        GenderP = []
        EthP = []
        IncomeP = []
        FamilyP = []
        PolP = []
        RelP = []
        EduP = []

        ####
        cur.execute("SELECT Age FROM " + Table)
        for row in cur:
            Age.append(row)
        Age1 = max(set(Age), key=Age.count)
        Age2 = str(Age1)
        Age2 = Age2.replace(',', '')
        Age2 = Age2.replace('(', '')
        Age2 = Age2.replace(')', '')

        cur.execute("SELECT Age FROM " + Table + " WHERE Age = " + Age2)
        for row in cur:
            AgeP.append(row)
        AgePer = len(AgeP) / len(Age)

        ####
        cur.execute("SELECT Gender FROM " + Table)
        for row in cur:
            Gender.append(row)
        Gender1 = max(set(Gender), key=Gender.count)
        Gender2 = str(Gender1)
        Gender2 = Gender2.replace(',', '')
        Gender2 = Gender2.replace('(', '')
        Gender2 = Gender2.replace(')', '')

        cur.execute("SELECT Gender FROM " + Table + " WHERE Gender = " + Gender2)
        for row in cur:
            GenderP.append(row)
        GenderPer = len(GenderP) / len(Gender)
        ####
        cur.execute("SELECT Ethnicity FROM " + Table)
        for row in cur:
            Eth.append(row)
        Eth1 = max(set(Eth), key=Eth.count)
        Eth2 = str(Eth1)
        Eth2 = Eth2.replace(',', '')
        Eth2 = Eth2.replace('(', '')
        Eth2 = Eth2.replace(')', '')

        cur.execute("SELECT Ethnicity FROM " + Table + " WHERE Ethnicity = " + Eth2)
        for row in cur:
            EthP.append(row)
        EthPer = len(EthP) / len(Eth)
        ####
        cur.execute("SELECT Income FROM " + Table)
        for row in cur:
            Income.append(row)
        Income1 = max(set(Income), key=Income.count)
        Income2 = str(Income1)
        Income2 = Income2.replace(',', '')
        Income2 = Income2.replace('(', '')
        Income2 = Income2.replace(')', '')

        cur.execute("SELECT Income FROM " + Table + " WHERE Income = " + Income2)
        for row in cur:
            IncomeP.append(row)
        IncomePer = len(IncomeP) / len(Income)
        ####

        cur.execute("SELECT Family FROM " + Table)
        for row in cur:
            Family.append(row)
        Family1 = max(set(Family), key=Family.count)
        Family2 = str(Family1)
        Family2 = Family2.replace(',', '')

        cur.execute("SELECT Family FROM " + Table + " WHERE Family = " + Family2)
        for row in cur:
            FamilyP.append(row)
        FamilyPer = len(FamilyP) / len(Family)
        ####

        cur.execute("SELECT Political FROM " + Table)
        for row in cur:
            Pol.append(row)
        Pol1 = max(set(Pol), key=Pol.count)
        Pol2 = str(Pol1)
        Pol2 = Pol2.replace(',', '')
        Pol2 = Pol2.replace('(', '')
        Pol2 = Pol2.replace(')', '')

        cur.execute("SELECT Political FROM " + Table + " WHERE Political = " + Pol2)
        for row in cur:
            PolP.append(row)
        PolPer = len(PolP) / len(Pol)
        ####

        cur.execute("SELECT Religion FROM " + Table)
        for row in cur:
            Rel.append(row)
        Rel1 = max(set(Rel), key=Rel.count)
        Rel2 = str(Rel1)
        Rel2 = Rel2.replace(',', '')
        Rel2 = Rel2.replace('(', '')
        Rel2 = Rel2.replace(')', '')

        cur.execute("SELECT Religion FROM " + Table + " WHERE Religion = " + Rel2)
        for row in cur:
            RelP.append(row)
        RelPer = len(RelP) / len(Rel)
        ####

        cur.execute("SELECT Education FROM " + Table)
        for row in cur:
            Edu.append(row)
        Edu1 = max(set(Edu), key=Edu.count)
        Edu2 = str(Edu1)
        Edu2 = Edu2.replace(',', '')
        Edu2 = Edu2.replace(',', '')
        Edu2 = Edu2.replace('(', '')
        Edu2 = Edu2.replace(')', '')

        cur.execute("SELECT Education FROM " + Table + " WHERE Education = " + Edu2)
        for row in cur:
            EduP.append(row)
        EduPer = len(EduP) / len(Edu)
        ####




        dataMax = ["Max Values", Age2, Gender2, Eth2, Income2, Family2, Pol2, Rel2, Edu2]
        dataPer = ["Percents", AgePer, GenderPer, EthPer, IncomePer, FamilyPer, PolPer, RelPer, EduPer]

        dataMinMax = [data0, dataMax, dataPer]



        cur.close()
        conn.close()
        tk.Tk.__init__(self)
        t = NewTable(self)

class MinFind(Tk):  ##Finds least recurring value
    def __init__(self):
        global Table
        global dataMinMax
        global data0

        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='****', db=Table, autocommit=True)
        cur = conn.cursor()
        Age = []
        Gender = []
        Eth = []
        Income = []
        Family = []
        Pol = []
        Rel = []
        Edu = []

        AgeP = []
        GenderP = []
        EthP = []
        IncomeP = []
        FamilyP = []
        PolP = []
        RelP = []
        EduP = []

        ####
        cur.execute("SELECT Age FROM " + Table)
        for row in cur:
            Age.append(row)
        Age1 = min(set(Age), key=Age.count)
        Age2 = str(Age1)
        Age2 = Age2.replace(',', '')
        Age2 = Age2.replace('(', '')
        Age2 = Age2.replace(')', '')

        cur.execute("SELECT Age FROM " + Table + " WHERE Age = " + Age2)
        for row in cur:
            AgeP.append(row)
        AgePer = len(AgeP) / len(Age)

        ####
        cur.execute("SELECT Gender FROM " + Table)
        for row in cur:
            Gender.append(row)
        Gender1 = min(set(Gender), key=Gender.count)
        Gender2 = str(Gender1)
        Gender2 = Gender2.replace(',', '')
        Gender2 = Gender2.replace('(', '')
        Gender2 = Gender2.replace(')', '')

        cur.execute("SELECT Gender FROM " + Table + " WHERE Gender = " + Gender2)
        for row in cur:
            GenderP.append(row)
        GenderPer = len(GenderP) / len(Gender)
        ####
        cur.execute("SELECT Ethnicity FROM " + Table)
        for row in cur:
            Eth.append(row)
        Eth1 = min(set(Eth), key=Eth.count)
        Eth2 = str(Eth1)
        Eth2 = Eth2.replace(',', '')
        Eth2 = Eth2.replace('(', '')
        Eth2 = Eth2.replace(')', '')

        cur.execute("SELECT Ethnicity FROM " + Table + " WHERE Ethnicity = " + Eth2)
        for row in cur:
            EthP.append(row)
        EthPer = len(EthP) / len(Eth)
        ####
        cur.execute("SELECT Income FROM " + Table)
        for row in cur:
            Income.append(row)
        Income1 = min(set(Income), key=Income.count)
        Income2 = str(Income1)
        Income2 = Income2.replace(',', '')
        Income2 = Income2.replace('(', '')
        Income2 = Income2.replace(')', '')

        cur.execute("SELECT Income FROM " + Table + " WHERE Income = " + Income2)
        for row in cur:
            IncomeP.append(row)
        IncomePer = len(IncomeP) / len(Income)
        ####

        cur.execute("SELECT Family FROM " + Table)
        for row in cur:
            Family.append(row)
        Family1 = min(set(Family), key=Family.count)
        Family2 = str(Family1)
        Family2 = Family2.replace(',', '')

        cur.execute("SELECT Family FROM " + Table + " WHERE Family = " + Family2)
        for row in cur:
            FamilyP.append(row)
        FamilyPer = len(FamilyP) / len(Family)
        ####

        cur.execute("SELECT Political FROM " + Table)
        for row in cur:
            Pol.append(row)
        Pol1 = min(set(Pol), key=Pol.count)
        Pol2 = str(Pol1)
        Pol2 = Pol2.replace(',', '')
        Pol2 = Pol2.replace('(', '')
        Pol2 = Pol2.replace(')', '')

        cur.execute("SELECT Political FROM " + Table + " WHERE Political = " + Pol2)
        for row in cur:
            PolP.append(row)
        PolPer = len(PolP) / len(Pol)
        ####

        cur.execute("SELECT Religion FROM " + Table)
        for row in cur:
            Rel.append(row)
        Rel1 = min(set(Rel), key=Rel.count)
        Rel2 = str(Rel1)
        Rel2 = Rel2.replace(',', '')
        Rel2 = Rel2.replace('(', '')
        Rel2 = Rel2.replace(')', '')

        cur.execute("SELECT Religion FROM " + Table + " WHERE Religion = " + Rel2)
        for row in cur:
            RelP.append(row)
        RelPer = len(RelP) / len(Rel)
        ####

        cur.execute("SELECT Education FROM " + Table)
        for row in cur:
            Edu.append(row)
        Edu1 = min(set(Edu), key=Edu.count)
        Edu2 = str(Edu1)
        Edu2 = Edu2.replace(',', '')
        Edu2 = Edu2.replace(',', '')
        Edu2 = Edu2.replace('(', '')
        Edu2 = Edu2.replace(')', '')

        cur.execute("SELECT Education FROM " + Table + " WHERE Education = " + Edu2)
        for row in cur:
            EduP.append(row)
        EduPer = len(EduP) / len(Edu)
        ####


        dataMin = ["Max Values", Age2, Gender2, Eth2, Income2, Family2, Pol2, Rel2, Edu2]
        dataPer = ["Percents", AgePer, GenderPer, EthPer, IncomePer, FamilyPer, PolPer, RelPer, EduPer]

        dataMinMax = [data0, dataMin, dataPer]


        cur.close()
        conn.close()
        tk.Tk.__init__(self)
        t = NewTable(self)

class NewTable(tk.Tk):  # create new table for min/max
    global dataMinMax

    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.canvas = tk.Canvas(root, borderwidth=0, bg="white")
        self.frame = tk.Frame(self.canvas, background="white")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.vsb2 = tk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vsb.set)  # ConnectScrollertoCanvas
        self.canvas.configure(xscrollcommand=self.vsb2.set)
        self.vsb.pack(side="right", fill="y")  # Insert
        self.vsb2.pack(side="bottom", fill="x")
        self.canvas.pack(side="bottom", fill="both", expand=True)  # Insert
        self.canvas.create_window((20, 4), window=self.frame, anchor="nw", tags="self.frame")  # Create Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()

    # CreatesFrameandCanvas

    def populate(self):

        rowc = 0
        colc = 0

        for row in range(len(dataMinMax)):
            tempdata = dataMinMax.__getitem__(row)
            for col in range(len(tempdata)):
                info = tempdata.__getitem__(col)
                tk.Label(self.frame, text=info, width=18, borderwidth="1", relief="solid").grid(row=row, column=col)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

class FilterTable(tk.Tk):
    global dataFilter0
    global BS
    global BSNum


    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.canvas = tk.Canvas(root, borderwidth=0, bg="white")
        self.frame = tk.Frame(self.canvas, background="white")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.vsb2 = tk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vsb.set)  # ConnectScrollertoCanvas
        self.canvas.configure(xscrollcommand=self.vsb2.set)
        self.vsb.pack(side="right", fill="y")  # Insert
        self.vsb2.pack(side="bottom", fill="x")
        self.canvas.pack(side="bottom", fill="both", expand=True)  # Insert
        self.canvas.create_window((20, 4), window=self.frame, anchor="nw", tags="self.frame")  # Create Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.populate()

        # CreatesFrameandCanvas

    def populate(self):

        dataFTHold = []  # Holds array of filtered data
        dataFHold = []  # holds filtered data

        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='****', db=Table, autocommit=True)
        cur = conn.cursor()

        cur.execute(BS)

        for row in cur:

            for col in row:
                dataFHold.append(col)
            dataFTHold.append(dataFHold)
            dataFHold = []

        cur.close()
        conn.close()

        print(dataFilter0)
        print(dataFTHold)

        for row in range(len(dataFTHold)):

            tempdata = dataFTHold.__getitem__(row)
            for col in range(len(tempdata)):
                info = tempdata.__getitem__(col)
                tk.Label(self.frame, text=info, width=18, borderwidth="1", relief="solid").grid(row=row, column=col)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

class test(tk.Frame, tk.Tk):  # Makes main table
    global dataT
    global BS
    global dataFilter0

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.grid = tk.Label.grid(self, row=1, column=6)

        self.button1 = tk.Button(self, text="Add", command=self.Add)
        self.button2 = tk.Button(self, text="Delete", command=Delete)
        self.button3 = tk.Button(self, text="Most Common", command=MaxFind)
        self.button4 = tk.Button(self, text="Least Common", command=MinFind)
        self.button5 = tk.Button(self, text="Update Row", command=Update)
        self.button6 = tk.Button(self, text="Filter Columns", command=Filter)


        self.button1.grid(row=1, column=1)
        self.button2.grid(row=1, column=2)
        self.button3.grid(row=1, column=3)
        self.button4.grid(row=1, column=4)
        self.button5.grid(row=1, column=5)
        self.button6.grid(row=1, column=6)

        self.canvas = tk.Canvas(root, borderwidth=0, bg="white")
        self.frame = tk.Frame(self.canvas, background="white")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.vsb2 = tk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vsb.set)  # ConnectScrollertoCanvas
        self.canvas.configure(xscrollcommand=self.vsb2.set)
        self.vsb.pack(side="right", fill="y")  # Insert
        self.vsb2.pack(side="bottom", fill="x")
        self.canvas.pack(side="bottom", fill="both", expand=True)  # Insert
        self.canvas.create_window((20, 4), window=self.frame, anchor="nw", tags="self.frame")  # Create Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.populate()

    # CreatesFrameandCanvas

    def populate(self):

        rowc = 0
        colc = 0
        print(dataT)
        print("DataFilter =" + str(dataFilter0))
        for row in range(len(dataT)):

            tempdata = dataT.__getitem__(row)

            for col in range(len(data0)):
                info = tempdata.__getitem__(col)
                tk.Label(self.frame, text=info, width=18, borderwidth="1", relief="solid").grid(row=row, column=col)

    # Actually Makes Grid and Inserts Data

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def Add(self):
      Add()
      self.destroy()


class DefaultDatabase():
    def __init__(self):
        global dataF
        global dataT
        global data0
        global Table
        global BS
        global Filter
        global dataFilter0

        data0 = ["ID", "Age", "Gender", "Ethnicity", "Income", "Family", "Political Affiliation", "Religion",
                 "Education"]

        dataT = [data0]
        rowc = 0
        colc = 0

        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='****', db=Table, autocommit=True)
        cur = conn.cursor()

        cur.execute("SELECT id, Age, Gender, Ethnicity, Income, Family, Political, Religion, Education FROM " + Table)

        for row in cur:

            for col in row:
                dataF.append(col)
            dataT.append(dataF)
            dataF = []
            dataP = row

        cur.close()
        conn.close()
        ExampleApp()

class NameSet1():
    def __init__(self):
        global Table
        Table = "MOCK_DATA"
        DefaultDatabase()

class NameSet2():
    def __init__(self):
        global Table
        Table = "MOCKER_DATA"
        DefaultDatabase()

if __name__ == "__main__":
    root = tk.Tk()
    ButtonApp(root)
    root.mainloop()

    #
    #  self.populate(dataMinT)
    #
    # def populate(self, dataMinT):
    #     print("Confirm")
    #     self.canvas = tk.Canvas(root, borderwidth=0, bg="white")
    #     self.frame = tk.Frame(self.canvas, background="white")
    #     self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
    #     self.vsb2 = tk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)
    #     self.canvas.configure(yscrollcommand=self.vsb.set)  # ConnectScrollertoCanvas
    #     self.canvas.configure(xscrollcommand=self.vsb2.set)
    #     self.vsb.pack(side="right", fill="y")  # Insert
    #     self.vsb2.pack(side="bottom", fill="x")
    #     self.canvas.pack(side="bottom", fill="both", expand=True)  # Insert
    #     self.canvas.create_window((20, 4), window=self.frame, anchor="nw", tags="self.frame")  # Create Frame
    #     self.frame.bind("<Configure>", self.canvas.configure(scrollregion=self.canvas.bbox("all")))
    #
    #     rowc = 0
    #     colc = 0
    #
    #     for row in range(len(dataMinT)):
    #         tempdata = dataMinT.__getitem__(row)
    #         for col in range(len(data0)):
    #             info = tempdata.__getitem__(col)
    #             tk.Label(self.frame, text=info, width=18, borderwidth="1", relief="solid").grid(row=row, column=col)
    #
    #     self.canvas.configure(scrollregion=self.canvas.bbox("all"))

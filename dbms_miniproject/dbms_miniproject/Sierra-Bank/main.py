### PROGRAM CODE ###

import mysql.connector
from tkinter import *
from tkinter import ttk, font, messagebox
from random import randrange
from datetime import date
import bank_gui_elements_library as el

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='secret_password') 
mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE IF NOT EXISTS bank')
mycursor.execute('USE bank')
mycursor.execute('CREATE TABLE IF NOT EXISTS bank_master'
                 '''(acc_no INT(8) PRIMARY KEY,
                 pin INT(4),
                 first_name VARCHAR(15),
                 last_name VARCHAR(15),
                 balance INT(6),
                 phone_no INT(10))''')
mycursor.execute('CREATE TABLE IF NOT EXISTS bank_trans'
                 '''(acc_no INT(8),
                 amount INT(6),
                 dot DATE,
                 trans_type CHAR(1),
                 FOREIGN KEY(acc_no) REFERENCES bank_master(acc_no))''')
mydb.commit()


LINE_COLOUR = '#EBEBEB'
BGCOLOUR = '#002441'
FGCOLOUR = '#F3F4EA'
ENTITY_BGCOLOUR = '#203657'

createAccount_BGCOLOUR = '#AFCEDA'
createAccount_ACTIVE_BGCOLOUR = '#9AADB2'

dispAccount_BGCOLOUR = '#7F9BA8'
dispAccount_ACTIVE_BGCOLOUR = '#636D70'

makewithdrawal_BGCOLOUR = '#76625D'
makewithdrawal_ACTIVE_BGCOLOUR = '#594F4D'

makeDeposit_BGCOLOUR = '#E2A394'
makeDeposit_ACTIVE_BGCOLOUR = '#B58379'

exitButton_BGCOLOUR = '#F0DFDD'
exitButton_ACTIVE_BGCOLOUR = '#C6B3B0'


window = Tk()
el.centreWindow(window)
window.title('Sierra Bank Management System')
window.configure(bg=BGCOLOUR)
window.resizable(width=FALSE, height=FALSE)


def check_valid_acc(acc_no):
    mycursor.execute('SELECT acc_no FROM bank_master')
    accounts = [account[0] for account in mycursor]
    if acc_no.isdigit() and int(acc_no) not in accounts:
        messagebox.showerror('Error 420', 'Account does not exist')
        return False
    return True


headFont = font.Font(family='Geometos', size=52)
smallHeadFont = font.Font(family='Geometos', size=45)
subHeadFont = font.Font(family='Geometos', size=31)
textFont = font.Font(family='Poppins', size=18)
entryFont = font.Font(family='Poppins', size=14)


class HomeFrameClass():

    @staticmethod
    def homeFrameCreator():
        global homeFrame
        homeFrame = Frame(
            window,
            height=600,
            width=800,
            bg=BGCOLOUR)
        homeFrame.pack()

        titleLabel = Label(
            homeFrame,
            text='SIERRA\nBANK',
            font=headFont,
            justify=LEFT,
            bg=BGCOLOUR,
            fg=FGCOLOUR)
        titleLabel.place(relx=0.035, rely=0.356)

        createAccount = el.homeButton(
            frame=homeFrame,
            font=textFont,
            text='Create an account',
            bg=createAccount_BGCOLOUR,
            activebg=createAccount_ACTIVE_BGCOLOUR,
            command=makeAccountFrameClass.accountFrameCreator)

        dispAccount = el.homeButton(
            frame=homeFrame,
            font=textFont,
            text='Display account',
            bg=dispAccount_BGCOLOUR,
            activebg=dispAccount_ACTIVE_BGCOLOUR,
            command=displayAccountFrameClass.displayAccountFrameCreator)

        makewithdrawal = el.homeButton(
            frame=homeFrame,
            font=textFont,
            text='Make a withdrawal',
            bg=makewithdrawal_BGCOLOUR,
            activebg=makewithdrawal_ACTIVE_BGCOLOUR,
            command=withdrawalFrameClass.withdrawalFrameCreator)

        makeDeposit = el.homeButton(
            frame=homeFrame,
            font=textFont,
            text='Make a deposit',
            bg='#E2A394',
            activebg='#B58379',
            command=depositFrameClass.depositFrameCreator)

        exitButton = el.homeButton(
            frame=homeFrame,
            font=textFont,
            text='Exit',
            bg='#F0DFDD',
            activebg='#C6B3B0',
            command=window.destroy)

        homeButtons = [createAccount, dispAccount, makewithdrawal, makeDeposit,
                        exitButton]
        s = 0
        for button in homeButtons:
            button.place(anchor=NE, relx=1, rely=0 + s, width=298, height=120.4)
            s += 0.2

        lineLabel = Label(homeFrame, text='', bg=LINE_COLOUR)
        lineLabel.place(relx=0.62, rely=0, height=600, width=10)



class makeAccountFrameClass():

    @staticmethod
    def accountFrameCreator():

        homeFrame.pack_forget()

        accountFrame = Frame(
            window,
            height=600,
            width=800,
            bg=BGCOLOUR)
        accountFrame.pack()

        genericHeadLabel = el.genericHeadLabel(accountFrame, smallHeadFont)
        genericHeadLabel.place(relx=0.035, rely=0.03775)

        subHeadLabel = el.subHeadLabel(
            frame=accountFrame, font=subHeadFont, text='Create an\naccount')
        subHeadLabel.place(relx=0.648, rely=0.03775)

        firstNameLabel = el.genericLabel(
            frame=accountFrame, text='First name', font=textFont)
        firstNameLabel.place(relx=0.185, rely=0.346, width=222, height=44)

        lastNameLabel = el.genericLabel(
            frame=accountFrame, text='Last name', font=textFont)
        lastNameLabel.place(relx=0.185, rely=0.446, width=222, height=44)

        pinLabel = el.genericLabel(
            frame=accountFrame, text='Create a PIN', font=textFont)
        pinLabel.place(relx=0.185, rely=0.546, width=222, height=44)

        phoneNumberLabel = el.genericLabel(
            frame=accountFrame, text='Phone number', font=textFont)
        phoneNumberLabel.place(relx=0.185, rely=0.646, width=222, height=44)

        ### entry boxes ###

        Eb_bg , Eb_fg =ENTITY_BGCOLOUR, FGCOLOUR
        borderwidth = bw = 6

        firstNameEntry = Entry(
            accountFrame,
            relief=FLAT,
            bg=Eb_bg,
            fg=Eb_fg,
            font=entryFont,
            borderwidth=bw)

        lastNameEntry = Entry(
            accountFrame,
            relief=FLAT,
            bg=Eb_bg,
            fg=Eb_fg,
            font=entryFont,
            borderwidth=bw)

        pinEntry = Entry(
            accountFrame,
            relief=FLAT,
            bg=Eb_bg,
            fg=Eb_fg,
            font=entryFont,
            borderwidth=bw)

        phoneNumEntry = Entry(
            accountFrame,
            relief=FLAT,
            bg=Eb_bg,
            fg=Eb_fg,
            font=entryFont,
            borderwidth=bw)

        entryBoxes = [firstNameEntry, lastNameEntry, pinEntry, phoneNumEntry]
        i = 0
        for entryBox in entryBoxes:
            entryBox.place(relx=0.52, rely=0.353 + i, width=222, height=30)
            i += 0.1
        pinEntry.insert(0, str(randrange(1000, 10000)))

        def create_account():
            f_name = firstNameEntry.get()
            l_name = lastNameEntry.get()
            pin = pinEntry.get()
            phone_no = phoneNumEntry.get()

            checks = []
            if not f_name.isalpha():
                checks.append('The first name must only contain letters.')
            if not l_name.isalpha():
                checks.append('The last name must only contain letters.')
            if not phone_no.isdigit():
                checks.append('The mobile number must only contain digits.')
            if not pin.isdigit():
                checks.append('The PIN must only contain digits.')
            if len(pin) != 4:
                checks.append('The PIN must contain exactly 4 digits.')
            if checks:
                checks.append('''Please make sure the data entered follows the 
above mentioned guidelines and try again.''')
                err_msg = '\n'.join(checks)
                messagebox.showerror("Invalid Input", err_msg)
                return

            mycursor.execute('SELECT acc_no FROM bank_master')
            accounts = [account[0] for account in mycursor]
            while True:
                acc_no = randrange(10000000, 100000000)
                if acc_no not in accounts:
                    break
            mycursor.execute(f"""INSERT INTO bank_master VALUES(
                {acc_no}, {pin}, '{f_name}', '{l_name}', 0, {phone_no})""")
            mydb.commit()
            messagebox.showinfo('Your account was succesfully created',
                                f'''Your account number is {acc_no}\n.Your PIN is 
                                {pin}\n.Please make a note of these.''')

        createAccountButton = el.genericButton(
            accountFrame,
            text='CREATE',
            font=entryFont,
            command=create_account)
        createAccountButton.place(relx=0.38, rely=0.79, width=190, height=42)

        def goBack():
            if accountFrame.winfo_ismapped():
                accountFrame.pack_forget()
            if not homeFrame.winfo_ismapped():
                homeFrame.pack()

        backButton = el.backButton(accountFrame, font=textFont, command=goBack)
        backButton.place(relx=0.02, rely=0.92, height=30)



class displayAccountFrameClass():

    @staticmethod
    def displayAccountFrameCreator():

        homeFrame.pack_forget()

        displayAccountFrame = Frame(
            window,
            height=600,
            width=800,
            bg=BGCOLOUR)
        displayAccountFrame.pack()

        genericHeadLabel = el.genericHeadLabel(displayAccountFrame, smallHeadFont)
        genericHeadLabel.place(relx=0.035, rely=0.03775)

        subHeadLabel = el.subHeadLabel(
            frame=displayAccountFrame, font=subHeadFont, text='Display Your\naccount')
        subHeadLabel.place(relx=0.56, rely=0.03775)

        accountNumberLabel = el.genericLabel(
            frame=displayAccountFrame, text='Account number', font=textFont)
        fullNameLabel = el.genericLabel(
            frame=displayAccountFrame, text='Full name', font=textFont)
        balanceLabel = el.genericLabel(
            frame=displayAccountFrame, text='Balance', font=textFont)
        phoneNumberLabel = el.genericLabel(
            frame=displayAccountFrame, text='Phone number', font=textFont)

        s=0
        labels = [accountNumberLabel, fullNameLabel, balanceLabel, phoneNumberLabel]
        for label in labels:
            label.place(relx=0.185, rely=0.346+s, width=222, height=44)
            s+=0.1

        accNumEntry = Entry(
            displayAccountFrame,
            relief=FLAT,
            bg=ENTITY_BGCOLOUR,
            fg=FGCOLOUR,
            font=entryFont,
            borderwidth=6)
        accNumEntry.place(relx=0.52, rely=0.353, width=222, height=30)

        fullNameDisplayLabel = el.genericLabel(
            frame=displayAccountFrame, text='', font=textFont)
        fullNameDisplayLabel.place(relx=0.525, rely=0.446, height=44)

        balanceDisplayLabel = el.genericLabel(
            frame=displayAccountFrame, text='', font=textFont)
        balanceDisplayLabel.place(relx=0.525, rely=0.546, height=44)

        phoneNumDisplayLabel = el.genericLabel(
            frame=displayAccountFrame, text='', font=textFont)
        phoneNumDisplayLabel.place(relx=0.525, rely=0.646, height=44)

        def show_details():
            acc_no = accNumEntry.get()

            if not check_valid_acc(acc_no):
                return
            checks = []
            if not acc_no.isdigit():
                checks.append('The account number must only contain digits.')
            if len(acc_no) != 8:
                checks.append('The account number must contain exactly 8 digits.')
            if checks:
                err_msg = '\n'.join(checks)
                messagebox.showerror("Invalid Input", err_msg)
                return

            mycursor.execute(
                f"""SELECT CONCAT(first_name, ' ', last_name), balance, phone_no
                from bank_master where acc_no = {acc_no}""")
            full_name, balance, phone_no = mycursor.fetchone()
            fullNameDisplayLabel.config(text=full_name)
            balanceDisplayLabel.config(text=balance)
            phoneNumDisplayLabel.config(text=phone_no)

        getInfoButton = el.genericButton(
            displayAccountFrame,
            text='FETCH',
            font=entryFont,
            command=show_details)
        getInfoButton.place(relx=0.38, rely=0.79, width=190, height=42)

        def goBack():
            if displayAccountFrame.winfo_ismapped():
                displayAccountFrame.pack_forget()
            if not homeFrame.winfo_ismapped():
                homeFrame.pack()

        backButton = el.backButton(displayAccountFrame, font=textFont, command=goBack)
        backButton.place(relx=0.02, rely=0.92, height=30)



class withdrawalFrameClass():

    @staticmethod
    def withdrawalFrameCreator():

        homeFrame.pack_forget()

        withdrawalFrame = Frame(
            window,
            height=600,
            width=800,
            bg=BGCOLOUR)
        withdrawalFrame.pack()

        genericHeadLabel = el.genericHeadLabel(withdrawalFrame, smallHeadFont)
        genericHeadLabel.place(relx=0.035, rely=0.03775)

        subHeadLabel = el.subHeadLabel(
            frame=withdrawalFrame, font=subHeadFont, text='Make a\nwithdrawal')
        subHeadLabel.place(relx=0.59, rely=0.03775)

        accountNumberLabel = el.genericLabel(
            frame=withdrawalFrame, text='Account number', font=textFont)
        accountNumberLabel.place(relx=0.185, rely=0.4, width=222, height=44)

        PINLabel = el.genericLabel(
            frame=withdrawalFrame, text='PIN', font=textFont)
        PINLabel.place(relx=0.185, rely=0.5, width=222, height=44)

        amountLabel = el.genericLabel(
            frame=withdrawalFrame, text='Amount', font=textFont)
        amountLabel.place(relx=0.185, rely=0.6, width=222, height=44)

        ### entry boxes ###

        Eb_bg , Eb_fg = ENTITY_BGCOLOUR, FGCOLOUR
        borderwidth = bw = 6

        accNumEntry = Entry(
            withdrawalFrame,
            relief=FLAT,
            bg=Eb_bg,
            fg=Eb_fg,
            font=entryFont,
            borderwidth=bw)
        accNumEntry.place(relx=0.52, rely=0.409, width=222, height=30)

        PINEntry = Entry(
            withdrawalFrame,
            relief=FLAT,
            bg=Eb_bg,
            fg=Eb_fg,
            font=entryFont,
            borderwidth=bw)
        PINEntry.place(relx=0.52, rely=0.509, width=222, height=30)

        amountEntry = Entry(
            withdrawalFrame,
            relief=FLAT,
            bg=Eb_bg,
            fg=Eb_fg,
            font=entryFont,
            borderwidth=bw)
        amountEntry.place(relx=0.52, rely=0.609, width=222, height=30)

        def withdraw():
            acc_no = accNumEntry.get()
            pin = PINEntry.get()
            amount = amountEntry.get()

            if not check_valid_acc(acc_no):
                return

            checks = []
            if not acc_no.isdigit():
                checks.append('The account number must only contain digits.')
            if not amount.isdigit():
                checks.append('The amount must only contain digits.')
            if not pin.isdigit():
                checks.append('The PIN must only contain digits.')
            if len(acc_no) != 8:
                checks.append('The account number must contain exactly 8 digits.')
            if len(pin) != 4:
                checks.append('The PIN must contain exactly 4 digits.')
            if checks:
                err_msg = '\n'.join(checks)
                messagebox.showerror("Invalid Input", err_msg)
                return

            mycursor.execute(f'''SELECT balance 
                                FROM bank_master WHERE acc_no = {acc_no}''')
            if int(amount) > int(mycursor.fetchone()[0]):
                messagebox.showerror('Error', 'Insufficient funds.')
                return

            mycursor.execute(f'''UPDATE bank_master
                            SET balance = balance-{amount} where acc_no={acc_no}''')
            mycursor.execute(f"""INSERT INTO bank_trans
                            VALUES({acc_no}, {amount}, '{date.today()}', 'W')""")
            mycursor.execute(f'''SELECT balance 
                            FROM bank_master where acc_no = {acc_no}''')
            balance = mycursor.fetchone()[0]
            mydb.commit()
            messagebox.showinfo('Successful withdrawal',
                                f'''{amount} QR/- was withdrawn from your account.\nNew balance : {balance}''')

        withdrawButton = el.genericButton(
                withdrawalFrame,
                text='WITHDRAW',
                font=entryFont,
                command=withdraw)
        withdrawButton.place(relx=0.38, rely=0.76, width=190, height=42)

        def goBack():
            if withdrawalFrame.winfo_ismapped():
                withdrawalFrame.pack_forget()
            if not homeFrame.winfo_ismapped():
                homeFrame.pack()

        backButton = el.backButton(withdrawalFrame, font=textFont, command=goBack)
        backButton.place(relx=0.02, rely=0.92, height=30)



class depositFrameClass():

    @staticmethod
    def depositFrameCreator():

        homeFrame.pack_forget()

        depositFrame = Frame(
            window,
            height=600,
            width=800,
            bg=BGCOLOUR)
        depositFrame.pack()

        genericHeadLabel = el.genericHeadLabel(depositFrame, smallHeadFont)
        genericHeadLabel.place(relx=0.035, rely=0.03775)

        subHeadLabel = el.subHeadLabel(
            frame=depositFrame, font=subHeadFont, text='Make a\ndeposit')
        subHeadLabel.place(relx=0.72, rely=0.03775)

        accountNumberLabel = el.genericLabel(
            frame=depositFrame, text='Account number', font=textFont)
        accountNumberLabel.place(relx=0.185, rely=0.4, width=222, height=44)

        PINLabel = el.genericLabel(
            frame=depositFrame, text='PIN', font=textFont)
        PINLabel.place(relx=0.185, rely=0.5, width=222, height=44)

        amountLabel = el.genericLabel(
            frame=depositFrame, text='Amount', font=textFont)
        amountLabel.place(relx=0.185, rely=0.6, width=222, height=44)

        ### entry boxes ###

        Eb_bg , Eb_fg = ENTITY_BGCOLOUR, FGCOLOUR
        borderwidth = bw = 6

        accNumEntry = Entry(
            depositFrame,
            relief=FLAT,
            bg=Eb_bg,
            fg=Eb_fg,
            font=entryFont,
            borderwidth=bw)
        accNumEntry.place(relx=0.52, rely=0.409, width=222, height=30)

        PINEntry = Entry(
            depositFrame,
            relief=FLAT,
            bg=Eb_bg,
            fg=Eb_fg,
            font=entryFont,
            borderwidth=bw)
        PINEntry.place(relx=0.52, rely=0.509, width=222, height=30)

        amountEntry = Entry(
            depositFrame,
            relief=FLAT,
            bg=Eb_bg,
            fg=Eb_fg,
            font=entryFont,
            borderwidth=bw)
        amountEntry.place(relx=0.52, rely=0.609, width=222, height=30)

        def deposit():
            acc_no = accNumEntry.get()
            pin = PINEntry.get()
            amount = amountEntry.get()

            if not check_valid_acc(acc_no):
                return

            checks = []
            if not acc_no.isdigit():
                checks.append('The account number must only contain digits.')
            if not amount.isdigit():
                checks.append('The amount must only contain digits.')
            if not pin.isdigit():
                checks.append('The PIN must only contain digits.')
            if len(acc_no) != 8:
                checks.append('The account number must contain exactly 8 digits.')
            if len(pin) != 4:
                checks.append('The PIN must contain exactly 4 digits.')
            if checks:
                err_msg = '\n'.join(checks)
                messagebox.showerror("Invalid Input", err_msg)
                return

            mycursor.execute(f'''UPDATE bank_master
                            SET balance = balance+{amount} where acc_no={acc_no}''')
            mycursor.execute(f"""INSERT INTO bank_trans
                            VALUES({acc_no}, {amount}, '{date.today()}', 'D')""")
            mycursor.execute(f'''SELECT balance
                            FROM bank_master where acc_no = {acc_no}''')
            balance = mycursor.fetchone()[0]
            mydb.commit()
            messagebox.showinfo('Successful deposit',
                                f'''{amount} QR/- was deposited to your account.\nNew balance : {balance}''')

        depositButton = el.genericButton(
            depositFrame,
            text='DEPOSIT',
            font=entryFont,
            command=deposit)
        depositButton.place(relx=0.38, rely=0.76, width=190, height=42)

        def goBack():
            if depositFrame.winfo_ismapped():
                depositFrame.pack_forget()
            if not homeFrame.winfo_ismapped():
                homeFrame.pack()

        backButton = el.backButton(
            depositFrame,
            font=textFont,
            command=goBack)
        backButton.place(relx=0.02, rely=0.92, height=30)

if __name__ == '__main__':
    HomeFrameClass.homeFrameCreator()
    window.mainloop()

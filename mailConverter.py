from tkinter import *
from tkinter import messagebox
import smtplib
from email.message import EmailMessage
from tkinter import filedialog

def main ():
    # read from the text file
    f_content = read_text_file()

    if (f_content != False):
        if "gmail" in EMAIL_ADDRESS:
            send_gmail(f_content)
        elif "hotmail" or "outlook" in EMAIL_ADDRESS:
            send_outlook(f_content)
        else:
            return messagebox.showwarning(title="Warning", message="Unrecognizable email address")

def read_text_file ():
    try:
        with open(root_filename, "r") as f:
            f_content = f.read()
            f.close()
            return f_content
    except:
        return messagebox.showwarning(title="Warning", message="Error reading from file")

def send_gmail (f_content):
    print("in gmail")
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            msg = EmailMessage()
            msg['Subject'] = EMAIL_SUBJECT
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = RECIEVER_EMAIL
            msg.set_content(f_content)

            # log in to mail server
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
             # send mail
            smtp.send_message(msg)
            messagebox.showinfo(title="Success", message="Successfully sent email")
            smtp.quit()
    except:
        return messagebox.showwarning(title="Warning", message = "Error sending email")

def send_outlook (f_content):
    try:
        with smtplib.SMTP('smtp.office365.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            body = f_content

            msg = f'Subject: {EMAIL_SUBJECT} \n\n {body}'

            smtp.sendmail(EMAIL_ADDRESS, RECIEVER_EMAIL, msg)
            messagebox.showinfo(title="Success", message="Successfully sent email")
            smtp.quit()
    except:
       return messagebox.showwarning(title="Warning", message = "Error sending email")

root = Tk()
root.title("MailConverter")
root.configure(bg="white")
# set default size of root
root.geometry("400x300")
# change it so you cant resize
root.resizable(0,0)

# create black screen with app name
label = Label(root, text="MailConverter.exe", bg="#17a2b8", fg ="white")
label.config(font = ("Courier", 20))
label.pack(fill = BOTH, expand= 1)

def openWindow():
    root.destroy()
    window = Tk()
    window.title("MailConverter")
    window.geometry("600x400")
    window.config(bg="white")
    window.resizable(0,0)

    global e
    global e2
    global e3
    global e4
    global show_password
    global txt_file_label
    global frame_1

    frame_1 = Frame(window, width = 40).pack(padx=10, pady=8)
    txt_file_label = Label(frame_1, text="Select File to Convert",font = ("Helvetica", 12), bd =1, justify="left", bg="white", fg="black")
    txt_file_label.pack()
    choose_text = Button(frame_1, text="Choose File", command = get_text_root, font = ("Helvetica", 12), bg = "#009dff", fg ="white")
    choose_text.pack(pady=5)

    #get user email
    frame_2 = Frame(window, width = 40).pack(padx=10, pady=6)
    user_email_label = Label(frame_2, text="Your Email", font = ("Helvetica", 12), bd =1, bg="white", fg="black")
    user_email_label.pack()
    e = Entry(frame_2, width=35)
    e.config(highlightbackground="grey", highlightthickness=1)
    e.pack()

    # get user password
    frame_3 = Frame(window, width = 40).pack(padx=10, pady=8)
    user_password_label = Label(frame_3 , text="Your Email Password", font = ("Helvetica", 12), bd =1, bg="white", fg="black")
    user_password_label.pack()
    e2 = Entry(frame_3, width=35, show="*")
    e2.pack()
    e2.config(highlightbackground="grey", highlightthickness=1)
    show_password = Button(frame_3, text="Show Password", command = showPasswordField, bg = "#009dff", fg ="white")
    show_password.pack(pady=2)

    # get recipient email
    frame_4 = Frame(window, width = 40).pack(padx=10, pady=8)
    recipient_label = Label(frame_4, text="Recipients email", font = ("Helvetica", 12), bd =1, bg="white", fg="black")
    recipient_label.pack()
    e3= Entry(frame_4, width=35)
    e3.config(highlightbackground="grey", highlightthickness=1)
    e3.pack()

    # Get email subject
    frame_6 = Frame(window, width=40).pack(padx=10, pady=8)
    subject_label = Label(frame_6, text="Emails subject", font=("Helvetica", 12), bd=1, bg="white", fg="black")
    subject_label.pack()
    e4 = Entry(frame_6, width=35)
    e4.config(highlightbackground="grey", highlightthickness=1)
    e4.pack()

    frame_5 = Frame(window, width = 40).pack(padx=10, pady=8)
    button = Button(frame_5, text="Submit", command = handleSubmit, font = ("Helvetica", 12), padx=10, bg = "#009dff", fg ="white")
    button.pack()

    window.mainloop()

def handleSubmit():
    global EMAIL_ADDRESS
    global EMAIL_PASSWORD
    global RECIEVER_EMAIL
    global EMAIL_SUBJECT
    EMAIL_ADDRESS = e.get()
    EMAIL_PASSWORD = e2.get()
    RECIEVER_EMAIL = e3.get()
    EMAIL_SUBJECT = e4.get()
    main()

def hidePasswordField():
    e2.config(show="*")
    show_password.config(command= showPasswordField, text="Show Password")

def showPasswordField():
    e2.config(show="")
    show_password.config(command=hidePasswordField, text="Hide Password")

def get_text_root():
    global root_filename
    root_filename = filedialog.askopenfilename(initialdir="/",
                                             title="Choose File")
    txt_file_label.config(text = "File directory: " + root_filename)


# create button frame
frame = Frame(root)
frame.pack()

# start program button
start_button = Button(frame, text="Start", command = openWindow, padx=5)
start_button.config(font = ("Helvetica",13) , bg="#28a745", fg ="white")
start_button.pack(side=RIGHT)

# exit program button
button_quit = Button(frame, text="Quit", command=root.quit, padx=5)
button_quit.config(font = ("Helvetica", 13), bg="#dc3545", fg="white")
button_quit.pack(side=LEFT)

root.mainloop()
#
# print("Email: " + EMAIL_ADDRESS)
# print("Password: " + EMAIL_PASSWORD)
# print("Recipient: " +  RECIEVER_EMAIL)
# print("Email Subject " + EMAIL_SUBJECT)
# print(root_filename)

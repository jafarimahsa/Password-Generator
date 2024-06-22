from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers = ["1","2","3","4","5","6","7","8","9"]
    symbols = ["!","#","$","%","&","*","(",")","+"]


    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)


    password_letters = [random.choice(letters) for _ in range(nr_letters)]
        
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]   

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"your secure password is : {password}")
    password_entry.insert(0 , password)    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get().capitalize()
    email = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 :
        is_empty = messagebox.showinfo(title='Oops' , message="please make sure you haven't left any feilds empty!")
    else :
        is_ok = messagebox.askokcancel(title=website , message=f'These are the details entered : \nEmail : {email}'
                                                            f'\nPassword : {password} \nIs it ok to save?')
        if is_ok:
            with open("data.txt" , "a") as data_file :
                data_file.write(f"{website} | {email} | {password}\n")
                password_entry.delete(0 , END)
                website_entry.delete(0 , END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Generator')
window.config(padx=50 , pady=50)
window.config(padx=20 , pady=20)
image = PhotoImage(file='logo.png')
canvas = Canvas(width=200 , height=224)
canvas.create_image(100 , 100 , image=image)
website_label = Label(text='Website :')
website_entry = Entry(width=54)
website_entry.focus()
username_label = Label(text="Email/Username :")
username_entry = Entry(width=54)
password_label = Label(text='Password :')
password_entry = Entry(width=36)
generator_button = Button(text='Generate Password' , command=generate_password , width=14)
add_button = Button(text='Add' , width=45 , command=save)
username_entry.insert(0 , 'mahsajafaari007@gmail.com')
canvas.grid(row = 0 , column=1)
website_entry.grid(row=1 , column=1 , columnspan=2)
website_label.grid(row=1 , column=0)
username_entry.grid(row=2 , column=1 , columnspan=2)
username_label.grid(row=2 , column = 0)
password_entry.grid(row=3 , column=1 )
password_label.grid(row=3 , column=0)
generator_button.grid(row=3 , column=2)
add_button.grid(row=4 , column=1 , columnspan=2)

#canvas.pack()
window.mainloop()
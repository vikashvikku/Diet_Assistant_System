""" diet assistant system"""
from tkinter import *
import tkinter.font as font
from tkinter import messagebox

from random import randint

from functools import partial


# """ creating login  credential"""
def validate_login(user_name, pass_word):
    """ taking username """
    print("username entered :", user_name.get() == "viks")
    # taking password
    print("password entered :", pass_word.get() == "12345")
    # matching username and password
    if user_name.get() == "viks" and pass_word.get() == "12345":
        # if username and password matches then it will be login successfully
        print("Login Successful")
    else:
        # if credential don't match, it will show "Incorrect Credential"
        print("Incorrect Credential")


# window
tkWindow = Tk()

def calorie(weight, age):
    """ calculating calorie """
    return 6.84 * (weight + age)

# length and height of the login window
tkWindow.geometry('400x150')
tkWindow.title('Tkinter Login Form - python-examples.org')

# username label and text entry box
Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# password label and password entry box
Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()
Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validate_login = partial(validate_login, username, password)

# login button
Button(tkWindow, text="Login", command=validate_login).grid(row=4, column=0)

tkWindow.mainloop()

tk = Tk()
tk.configure(bg='#856ff8')
tk.title('Diet Assistant')


# Adding Exception Handling
class Error(Exception):
    """Base class for other exceptions"""
#    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
#    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
#    pass


def bmr():
    """ Declaring Functions """
    protein = ['Yogurt(1 cup)', 'Cooked meat(3 Oz)', 'Cooked fish(4 Oz)',
               '1 whole egg + 4 egg whites', 'Tofu(5 Oz)']
    fruit = ['Berries(80 Oz)', 'Apple', 'Orange', 'Banana',
             'Dried Fruits(Handful)', 'Fruit Juice(125ml)']
    vegetable = ['Any vegetable(80g)']
    grains = ['Cooked Grain(150g)', 'Whole Grain Bread(1 slice)',
              'Half Large Potato(75g)', 'Oats(250g)',
              '2 corn tortillas']
    pase = ['Soy nuts(i Oz)', 'Low fat milk(250ml)', 'Hummus(4 Tbsp)',
          'Cottage cheese (125g)', 'Flavored yogurt(125g)']
    taste_en = ['2 TSP (10 ml) olive oil',
                '2 TBSP (30g) reduced-calorie salad dressin', '1/4 medium avocado',
                'Small handful of nuts', '1/2 ounce  grated Parmesan cheese',
                '1 TBSP (20g) jam, jelly, honey, syrup, sugar']
    # while True:
    try:

        way_w = v3.get()
        hel_h = v4.get()
        age = v5.get()

        if way_w <= 1 or hel_h <= 20 or age <= 0:
            raise ValueTooSmallError
        if way_w >= 500 or hel_h >= 900 or age >= 200:
            raise ValueTooLargeError

        act = str(Lb.get(ACTIVE))
        if v1.get() == 1:
            cal = float()
            cal = 88.362 + (13.397 * float(way_w)) + (4.799 * float(hel_h)) - (5.677 * float(age))
            print(" Calculated Calorie is ", cal)
        if v1.get() == 2:
            cal = float()
            cal = 447.593 + (9.247 * float(way_w)) + (3.098 * float(hel_h)) - (4.330 * float(age))

        elif act == 'Sedentary(little or no exercise)':
            cal = cal * 1.2

        elif act == 'Lightly active(1-3 days/week)':
            cal = cal * 1.375

        elif act == 'Moderately active(3-5 days/week)':
            cal = cal * 1.55

        elif act == 'Very active(6-7 days/week)':
            cal = cal * 1.725

        elif act == 'Super active(twice/day)':
            cal = cal * 1.9

        print(" Your Calorie is ", cal)

        if cal < 1500:
            fin = StringVar()
            level_6 = Label(tk, textvariable=fin, relief=RAISED)
            fin.set("Breakfast: " + protein[randint(0, 5)] + " + " + fruit[randint(0, 5)])
            level_6.grid(row=0, column=3)

            fin2 = StringVar()
            level_8 = Label(tk, textvariable=fin2, relief=RAISED)
            fin2.set("Lunch: " + protein[randint(0, 5)] + " + " +
                     vegetable[0] + " + Leafy Greens" + grains[
                randint(0, 4)] + " + " + taste_en[randint(0, 5)])
            level_8.grid(row=1, column=3)

            fin3 = StringVar()
            level_9 = Label(tk, textvariable=fin3, relief=RAISED)
            fin3.set("Snack: " + pase[randint(0, 4)] + " + " + vegetable[0])
            level_9.grid(row=2, column=3)

            fin4 = StringVar()
            l10 = Label(tk, textvariable=fin4, relief=RAISED)
            fin4.set("Dinner: " + protein[randint(0, 5)] + " + 2 " +
            vegetable[0] + " + Leafy Greens" + grains[
                randint(0, 4)] + " + " + taste_en[randint(0, 5)])
            l10.grid(row=3, column=3)

            fin5 = StringVar()
            l11 = Label(tk, textvariable=fin5, relief=RAISED)
            fin5.set("Snack: " + fruit[randint(0, 5)])
            l11.grid(row=4, column=3)

        elif cal < 1800:
            fin = IntVar()
            level_6 = Label(tk, textvariable=fin, relief=RAISED)
            fin.set("Breakfast: " + protein[randint(0, 5)] + " + " + fruit[randint(0, 5)])
            level_6.grid(row=0, column=3)

            fin2 = StringVar()
            level_8 = Label(tk, textvariable=fin2, relief=RAISED)
            fin2.set("Lunch: " + protein[randint(0, 5)] + " + " +
                     vegetable[0] + " + Leafy Greens" + grains[
                randint(0, 4)] + " + " + taste_en[randint(0, 5)] + " + " + fruit[randint(0, 5)])
            level_8.grid(row=1, column=3)

            fin3 = StringVar()
            level_9 = Label(tk, textvariable=fin3, relief=RAISED)
            fin3.set("Snack: " + pase[randint(0, 4)] + " + " + vegetable[0])
            level_9.grid(row=2, column=3)

            fin4 = StringVar()
            l10 = Label(tk, textvariable=fin4, relief=RAISED)
            fin4.set("Dinner: 2 " + protein[randint(0, 5)] + " + " +
                     vegetable[0] + " + Leafy Greens" + grains[
                randint(0, 4)] + " + " + taste_en[randint(0, 5)])
            l10.grid(row=3, column=3)

            fin5 = StringVar()
            l11 = Label(tk, textvariable=fin5, relief=RAISED)
            fin5.set("Snack: " + fruit[randint(0, 5)])
            l11.grid(row=4, column=3)

        elif cal < 2200:
            fin = StringVar()
            level_6 = Label(tk, textvariable=fin, relief=RAISED)
            fin.set("Breakfast: " + protein[randint(0, 5)] + " + " + fruit[randint(0, 5)])
            level_6.grid(row=0, column=3)

            fin2 = StringVar()
            level_8 = Label(tk, textvariable=fin2, relief=RAISED)
            fin2.set("Lunch: " + protein[randint(0, 5)] + " + " +
                     vegetable[0] + " + Leafy Greens" + grains[
                randint(0, 4)] + " + " + taste_en[randint(0, 5)] + " + " + fruit[randint(0, 5)])
            level_8.grid(row=1, column=3)

            fin3 = StringVar()
            level_9 = Label(tk, textvariable=fin3, relief=RAISED)
            fin3.set("Snack: " + pase[randint(0, 4)] + " + " + vegetable[0])
            level_9.grid(row=2, column=3)

            fin4 = StringVar()
            l10 = Label(tk, textvariable=fin4, relief=RAISED)
            fin4.set("Dinner: 2 " + protein[randint(0, 5)] + " + 2 " +
                     vegetable[0] + " + Leafy Greens" + grains[
                randint(0, 4)] + " + " + taste_en[randint(0, 5)])
            l10.grid(row=3, column=3)

            fin5 = StringVar()
            l11 = Label(tk, textvariable=fin5, relief=RAISED)
            fin5.set("Snack: " + fruit[randint(0, 5)])
            l11.grid(row=4, column=3)

        elif cal >= 2200:
            fin = StringVar()
            level_6 = Label(tk, textvariable=fin, relief=RAISED)
            fin.set(
                "Breakfast: 2 " + protein[randint(0, 5)] + " + " +
                fruit[randint(0, 5)] + " + " + grains[randint(0, 4)])
            level_6.grid(row=0, column=3)

            fin2 = StringVar()
            level_8 = Label(tk, textvariable=fin2, relief=RAISED)
            fin2.set("Lunch: " + protein[randint(0, 5)] + " + " +
                     vegetable[0] + " + Leafy Greens" + grains[
                randint(0, 4)] + " + " +
                     taste_en[randint(0, 5)] + " + " + fruit[randint(0, 5)])
            level_8.grid(row=1, column=3)

            fin3 = StringVar()
            level_9 = Label(tk, textvariable=fin3, relief=RAISED)
            fin3.set("Snack: " + pase[randint(0, 4)] + " + " + vegetable[0])
            level_9.grid(row=2, column=3)

            fin4 = StringVar()
            l10 = Label(tk, textvariable=fin4, relief=RAISED)
            fin4.set("Dinner: 2 " + protein[randint(0, 5)] + " + 2 " +
                     vegetable[0] + " + Leafy Greens + 2 " + grains[
                randint(0, 4)] + " + 2 " + taste_en[randint(0, 5)])
            l10.grid(row=3, column=3)

            fin5 = StringVar()
            l11 = Label(tk, textvariable=fin5, relief=RAISED)
            fin5.set("Snack: " + fruit[randint(0, 5)])
            l11.grid(row=4, column=3)

    except ValueTooSmallError:
        messagebox.showwarning("Warning", "This value is too small try again!")
        messagebox.showinfo("information", "Try Again")

    except ValueTooLargeError:
        messagebox.showwarning("Warning", "This value is too large try again!")
        messagebox.showinfo("information", "Try Again")


v1 = IntVar()
c1 = Radiobutton(tk, text='Male', value=1, variable=v1)
c1.grid(row=0, column=1)

c2 = Radiobutton(tk, text="Female", value=2, variable=v1)
c2.grid(row=0, column=2)

l1 = Label(tk, text='Weight', bg='white')
l2 = Label(tk, text='Height(in cms)', bg='white')
l3 = Label(tk, text='Age', bg='white')
l4 = Label(tk, text='Gender', bg='white')
l5 = Label(tk, text='Activity', bg='white')

v3 = DoubleVar()
v4 = DoubleVar()
v5 = DoubleVar()

e3 = Entry(tk, textvariable=v3, width=30)
e4 = Entry(tk, textvariable=v4, width=30)
e5 = Entry(tk, textvariable=v5, width=30)

Lb = Listbox(tk, height=6, width=30)
Lb.insert(1, 'Sedentary (little or no exercise)')
Lb.insert(2, 'Lightly active (1-3 days/week)')
Lb.insert(3, 'Moderately active (3-5 days/week)')
Lb.insert(4, 'Very active (6-7 days/week)')
Lb.insert(5, 'Super active (twice/day)')

var = Lb.get(ACTIVE)
print(var)

l5 = Label(tk, text='Activity')
l5.grid(row=4, column=0)
myFont = font.Font(weight="bold")

b1 = Button(tk, text='Submit', width=25, bg='blue', fg='#ffffff', command=bmr)
b1['font'] = myFont

l1.grid(row=1, column=0)
l2.grid(row=2, column=0)
l3.grid(row=3, column=0)
l4.grid(row=0, column=0)
l5.grid(row=4, column=0)
e3.grid(row=1, column=1)
e4.grid(row=2, column=1)
e5.grid(row=3, column=1)
Lb.grid(row=4, column=1)
b1.grid(row=6, columns=3)

tk.mainloop()

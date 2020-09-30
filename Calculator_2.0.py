import math
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as msg

e_cut = ""
e_copy = ""


# Implementation of View Help option in Help Menu
def get_help():
    global my_img
    top = Toplevel()
    top.title("Help")
    top.iconbitmap('1.5.ico')
    my_img = ImageTk.PhotoImage(Image.open('Help.jpg'))
    Label(top, image=my_img).grid()
    Button(top, text="Close", command=top.destroy).grid(columnspan=5)


# Implementation of +/- Button
def button_opp():
    try:
        if '.' in e.get():
            x = float(e.get())
        else:
            x = int(e.get())
        opp = str(-x)
        e.delete(0, END)
        e.insert(0, opp)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of = Button
def button_equal():
    expression = e.get()
    e.delete(0, END)
    try:
        e.insert(0, eval(expression))
    except:
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Key binding function (if enter key is pressed)
def enter_press(event):
    expression = e.get()
    e.delete(0, END)
    if expression[-1] == "!":
        expression = expression[:-1]
        try:
            if "." not in expression and 0 < int(expression) < 1000:
                print(expression)
                fact = math.factorial(int(expression))
                e.insert(0, fact)
            else:
                e.insert(0, "Error: Invalid Input, Press Clear!")
        except:
            e.insert(0, "Error: Invalid Input, Press Clear!")

    else:
        try:
            e.insert(0, eval(expression))
        except:
            e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of Square Root Button
def button_sqrt():
    try:
        if '.' in e.get():
            x = float(e.get())
        else:
            x = int(e.get())
        sqrt = str(math.sqrt(x))
        e.delete(0, END)
        e.insert(0, sqrt)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of log10
def button_log10():
    try:
        log10 = str(math.log10(int(e.get())))
        e.delete(0, END)
        e.insert(0, log10)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of Square
def button_sqr():
    try:
        if '.' in e.get():
            x = float(e.get())
        else:
            x = int(e.get())
        sqr = str(x * x)
        e.delete(0, END)
        e.insert(0, sqr)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of Cube Button
def button_cube():
    try:
        if '.' in e.get():
            x = float(e.get())
        else:
            x = int(e.get())
        cube = str(x * x * x)
        e.delete(0, END)
        e.insert(0, cube)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of Inverse (1/x) Button
def button_inverse():
    try:
        inverse = str(1 / float(e.get()))
        e.delete(0, END)
        e.insert(0, inverse)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of log base 2 Button
def button_log2():
    try:
        log2 = str(math.log2(int(e.get())))
        e.delete(0, END)
        e.insert(0, log2)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of Mod(|x|) Button
def button_mod():
    if '.' in e.get():
        mod = abs(float(e.get()))
    else:
        mod = abs(int(e.get()))
    e.delete(0, END)
    e.insert(0, mod)


# Implementation of Cut option in Edit Menu
def cut():
    global e_cut
    e_cut = e.get()
    e.delete(0, END)


# Implementation of Copy option in Edit Menu
def copy():
    global e_copy
    e_copy = e.get()


# Implementation of Paste option in Edit Menu
def paste():
    global e_cut
    global e_copy
    x = e.get()
    e.delete(0, END)
    if len(e_cut) > 0:
        e.insert(0, x + e_cut)
    elif len(e_copy) > 0:
        e.insert(0, x + e_copy)


# Implementation of 10^n Button
def button_10power():
    power = 10 ** int(float(e.get()))
    e.delete(0, END)
    e.insert(0, power)


# Implementation of Floor Function
def button_floor():
    try:
        floor = math.floor(float(e.get()))
        e.delete(0, END)
        e.insert(0, floor)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of Ceil Function
def button_ceil():
    try:
        ceil = math.ceil(float(e.get()))
        e.delete(0, END)
        e.insert(0, ceil)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of Factorial Function
def button_factorial():
    # Putting a limit to the factorial
    e.delete(0, END)
    if "." not in e.get() and 0 < int(e.get()) < 1000:
        fact = math.factorial(int(e.get()))
        e.insert(0, fact)
    else:
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of Natural log Function
def button_ln():
    try:
        ln = math.log(float(e.get()))
        e.delete(0, END)
        e.insert(0, ln)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of CE button
def button_CE():
    e.delete(0, END)
    e.insert(0, "0")


# Implementation of cos Function
def button_cos():
    try:
        cos = math.cos(float(e.get()))
        e.delete(0, END)
        e.insert(0, cos)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of sin Function
def button_sin():
    try:
        sin = math.sin(float(e.get()))
        e.delete(0, END)
        e.insert(0, sin)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of cosh Function
def button_cosh():
    try:
        cosh = math.cosh(float(e.get()))
        e.delete(0, END)
        e.insert(0, cosh)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of sinh Function
def button_sinh():
    try:
        sinh = math.sinh(float(e.get()))
        e.delete(0, END)
        e.insert(0, sinh)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of tan Function
def button_tan():
    try:
        tan = math.tan(float(e.get()))
        e.delete(0, END)
        e.insert(0, tan)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of tanh Function
def button_tanh():
    try:
        tanh = math.tanh(float(e.get()))
        e.delete(0, END)
        e.insert(0, tanh)
    except:
        e.delete(0, END)
        e.insert(0, "Error: Invalid Input, Press Clear!")


# Implementation of pi Button (Clears screen and puts the value of pi on it)
def button_pi():
    e.delete(0, END)
    e.insert(0, math.pi)


# Implementation of 2pi Button (Clears screen and puts the value of tau(=2*pi) on it)
def button_tau():
    e.delete(0, END)
    e.insert(0, 2 * math.pi)


# Implementation of e Button (Clears screen and puts the value of e on it)
def button_e():
    e.delete(0, END)
    e.insert(0, math.e)


# Implementation of Clicking Operators and Operands
def button_click(x):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + x)


# Implementation of BackSpace Button
def button_backspace():
    x = e.get()
    x = x[:-1]
    e.delete(0, END)
    e.insert(0, x)


# Implementation of Exit Option in Type Menu
def press_exit():
    p_exit = msg.askyesno("Student's Calculator", "Confirm to exit")
    if p_exit != 0:
        root.destroy()
        return


# Implementation of Standard Calculator Option in Type Menu
def standard():
    root.resizable(width=False, height=False)
    root.iconbitmap('1.5.ico')
    root.geometry("480x535")


# Implementation of Scientific Calculator Option in Type Menu
def scientific():
    root.resizable(width=False, height=False)
    root.iconbitmap('1.5.ico')
    root.geometry("950x535")


# Defining root window
root = Tk()
root.title("Student's Calculator")
root.configure(background="white")
root.resizable(width=False, height=False)
root.bind("<Return>", enter_press)
root.iconbitmap('1.5.ico')
root.geometry("480x557")

calc = Frame(root)
calc.grid()

menu_bar = Menu(calc)

type_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Type", menu=type_menu)
type_menu.add_command(label="Standard", command=standard)
type_menu.add_command(label="Scientific", command=scientific)

type_menu.add_separator()
type_menu.add_command(label="Exit", command=press_exit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)

edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="View Help", command=get_help)

root.configure(menu=menu_bar)

# Defining and Showing Entry Widget
e = Entry(root, font=('arial', 20, 'bold'), width=30, bd=10, justify=LEFT)
e.focus()
e.grid(row=0, column=0, columnspan=4, padx=6, pady=5)

button_1 = Button(root, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text='1',
                  command=lambda: button_click('1'))
button_2 = Button(root, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text='2',
                  command=lambda: button_click('2'))
button_3 = Button(root, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text='3',
                  command=lambda: button_click('3'))
button_4 = Button(root, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text='4',
                  command=lambda: button_click('4'))
button_5 = Button(root, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text='5',
                  command=lambda: button_click('5'))
button_6 = Button(root, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text='6',
                  command=lambda: button_click('6'))
button_7 = Button(root, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text='7',
                  command=lambda: button_click('7'))
button_8 = Button(root, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text='8',
                  command=lambda: button_click('8'))
button_9 = Button(root, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text='9',
                  command=lambda: button_click('9'))

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_Clear = Button(root, text="←", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gold3",
                      command=button_backspace)
button_Clear.grid(row=1, column=2, pady=1)
button_AllClear = Button(root, text="CE", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gold3",
                         command=button_CE)
button_AllClear.grid(row=1, column=1, pady=1)
button_sqrt = Button(root, text="√", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gold3",
                     command=button_sqrt)
button_sqrt.grid(row=1, column=0, pady=1)

button_add = Button(root, text="+", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gold3",
                    command=lambda: button_click('+'))
button_add.grid(row=4, column=3, pady=1)
button_sub = Button(root, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gold3",
                    command=lambda: button_click('-'))
button_sub.grid(row=3, column=3, pady=1)
button_mul = Button(root, text="*", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gold3",
                    command=lambda: button_click('*'))
button_mul.grid(row=2, column=3, pady=1)
button_div = Button(root, text="/", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gold3",
                    command=lambda: button_click('/'))
button_div.grid(row=1, column=3, pady=1)

button_zero = Button(root, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     command=lambda: button_click('0'))
button_zero.grid(row=5, column=1, pady=1)
button_dot = Button(root, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gold3",
                    command=lambda: button_click('.'))
button_dot.grid(row=5, column=2, pady=1)
button_equal = Button(root, text="=", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gold3",
                      command=button_equal)
button_equal.grid(row=5, column=3, pady=1)
button_opp = Button(root, text="+/−", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gold3",
                    command=button_opp)
button_opp.grid(row=5, column=0, pady=1)

# Scientific Calculator Buttons
button_Pi = Button(root, text="π", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="goldenrod1",
                   command=button_pi)
button_Pi.grid(row=1, column=4, pady=1)
button_cos = Button(root, text="cos", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="goldenrod1",
                    command=button_cos)
button_cos.grid(row=1, column=5, pady=1)
button_sin = Button(root, text="sin", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="goldenrod1",
                    command=button_sin)
button_sin.grid(row=1, column=6, pady=1)
button_tan = Button(root, text="tan", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="goldenrod1",
                    command=button_tan)
button_tan.grid(row=1, column=7, pady=1)

button_2Pi = Button(root, text="2π", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="goldenrod1",
                    command=button_tau)
button_2Pi.grid(row=2, column=4, pady=1)
button_cosh = Button(root, text="cosh", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     bg="goldenrod1", command=button_cosh)
button_cosh.grid(row=2, column=5, pady=1)
button_sinh = Button(root, text="sinh", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     bg="goldenrod1", command=button_sinh)
button_sinh.grid(row=2, column=6, pady=1)
button_tanh = Button(root, text="tanh", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     bg="goldenrod1", command=button_tanh)
button_tanh.grid(row=2, column=7, pady=1)

button_log10 = Button(root, text="log10", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                      bg="goldenrod1", command=button_log10)
button_log10.grid(row=3, column=4, pady=1)
button_log2 = Button(root, text="log2", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     bg="goldenrod1", command=button_log2)
button_log2.grid(row=3, column=5, pady=1)
button_inverse = Button(root, text="1/x", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                        bg="goldenrod1", command=button_inverse)
button_inverse.grid(row=4, column=7, pady=1)
button_ln = Button(root, text="ln", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="goldenrod1",
                   command=button_ln)
button_ln.grid(row=3, column=6, pady=1)

button_sqr = Button(root, text=u"x\u00B2", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                    bg="goldenrod1", command=button_sqr)
button_sqr.grid(row=4, column=4, pady=1)
button_cube = Button(root, text=u"x\u00B3", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     bg="goldenrod1", command=button_cube)
button_cube.grid(row=4, column=5, pady=1)
button_10power = Button(root, text=u"10\u207F", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                        bg="goldenrod1", command=button_10power)
button_10power.grid(row=4, column=6, pady=1)
button_e = Button(root, text="e", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="goldenrod1",
                  command=button_e)
button_e.grid(row=3, column=7, pady=1)

button_mod = Button(root, text="|x|", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="goldenrod1",
                    command=button_mod)
button_mod.grid(row=5, column=5, pady=1)
button_floor = Button(root, text="⌊x⌋", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                      bg="goldenrod1", command=button_floor)
button_floor.grid(row=5, column=6, pady=1)
button_ceil = Button(root, text="⌈x⌉", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="goldenrod1",
                     command=button_ceil)
button_ceil.grid(row=5, column=7, pady=1)
button_factorial = Button(root, text="n!", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                          bg="goldenrod1", command=button_factorial)
button_factorial.grid(row=5, column=4, pady=1)

lblDisplay = Label(root, text="Scientific Calculator", font=('arial', 30, 'bold'), justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)

# event loop
root.mainloop()

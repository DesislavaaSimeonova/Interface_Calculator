
import tkinter as tk
import math

window = tk.Tk()
window.title("Python_GUI_Calculator")
window.geometry("400x450")
window.resizable(0,0)
window.configure(background = "burlywood1") 
button_frame = tk.Frame(window, bg = "burlywood1")
button_frame.pack()

equation = tk.StringVar()
display = tk.Entry(button_frame, textvariable = equation, justify = "right", font=("arial", 25, "bold"))
display.pack()
display.grid(row=0, column=0,columnspan=60,padx=15, pady = 15)
display.insert(0,"0")

expression = ""
memory = 0.0

def click_numb(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)

def fact():
    global expression
    
    try:
        expression = int(expression)
        expression = math.factorial(expression)
        expression = str(expression)
        equation.set(expression)
    except ValueError:
        error = "ERROR"
        equation.set(error)
        expression = ""

def clear_press():
    global expression
    expression = expression [:-1]
    equation.set(expression)

def press(num, equation):
    global expression
    expression = expression + str(num)
    equation.set(expression)
    
def equalpress():
    global expression
    
    try:
        global result
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def operations(num):
    #(+,-,*,/, %,**)
    global expression
    expression = expression + str(num)
    equation.set(expression)

def moperations(num):
    #(+,-,0)
    global result
    global expression
    global memory
    if num == "+":
        result = memory  + str(num) + expression
        equation.set(str(eval(result)))
        expression = result
    elif num == "-":
        result = memory  + str(num) + expression
        equation.set(str(eval(result)))
        expression = result
    elif num == "=":
        expression = memory
        equation.set(str(expression))
        expression = float(expression)
    elif num == "0":
        del memory
        memory = 0.0
        expression = float(memory)
        equation.set(str(expression))
    else:
        pass

def matfun(num):
    global expression
    global expression_two
    if num == "√":
        expression = float(expression)
        expression = math.sqrt(expression)
        expression = str(expression)
        equation.set(expression)
    elif num == "10^x":
        expression = float(expression)
        expression = math.pow(10, expression)
        expression = str(expression)
        equation.set(expression)
    elif num == "x^2":
        expression = float(expression)
        expression = math.pow(expression,2)
        expression = str(expression)
        equation.set(expression)

    elif num == "sin":
        expression = float(expression)
        expression = math.sin(expression)
        expression = str(expression)
        equation.set(expression)
    elif num == "cos":
        expression = float(expression)
        expression = math.cos(expression)
        expression = str(expression)
        equation.set(expression)
    elif num == "tan":
        expression = float(expression)
        expression = math.tan(expression)
        expression = str(expression)
        equation.set(expression)
    elif num == "log":
        expression = float(expression)
        expression = math.log(expression)
        expression = str(expression)
        equation.set(expression)
    elif num == "Deg":
        expression = float(expression)
        expression = math.degrees(expression)
        expression = str(expression)
        equation.set(expression)
    elif num == "Rad":
        expression = float(expression)
        expression = math.radians(expression)
        expression = str(expression)
        equation.set(expression)
    elif num == "π":
        expression = math.pi
        expression = str(expression)
        equation.set(expression)
    elif num == "±":
        if float(expression) > 0:
            expression = - float(expression)
        else:
            expression = abs(float(expression))
        equation.set(expression)
    elif num == "Exp":
        expression = float(expression)
        expression = math.exp(expression)
        expression = str(expression)
        equation.set(expression)
    else:
        pass

def clear(equation):
    global expression
    expression = ""
    equation.set("")

def memory (num):
    global memory
    global expression
    if num == "MS":        
        memory = expression
        equation.set(memory)
    else:
        pass

#first row
button_MC=tk.Button(button_frame, text="MC",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="khaki", width = 8, height = 1, command = lambda : moperations("0")).grid(row = 1, column = 0)
button_MR=tk.Button(button_frame, text="MR",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="khaki", width = 8, height = 1, command = lambda: moperations("=")).grid(row = 1, column = 1)
button_Mplus=tk.Button(button_frame, text="M+",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="khaki", width = 8, height = 1, command = lambda: moperations("+")).grid(row = 1, column = 2)
button_Mminus=tk.Button(button_frame, text="M-",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="khaki", width = 8, height = 1, command = lambda: moperations("-")).grid(row = 1, column =3)
button_MS=tk.Button(button_frame, text="MS",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="khaki", width = 8, height = 1, command = lambda: memory("MS")).grid(row = 1, column = 4)
#second row
button_power_two=tk.Button(button_frame, text="x^2",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="goldenrod1", width = 8, height = 2, command = lambda : matfun("x^2")).grid(row = 2, column =0)
button_power=tk.Button(button_frame, text="x^y",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="goldenrod1", width = 8, height = 2, command = lambda :  operations("**")).grid(row = 2, column = 1)
button_sin=tk.Button(button_frame, text="sin",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="goldenrod1", width = 8, height = 2, command = lambda :  matfun("sin")).grid(row = 2, column = 2)
button_cos=tk.Button(button_frame, text="cos",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="goldenrod1", width = 8, height = 2, command = lambda:  matfun("cos")).grid(row = 2, column = 3)
button_tan=tk.Button(button_frame, text="tan",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="goldenrod1", width = 8, height = 2, command = lambda:  matfun("tan")).grid(row = 2, column = 4)


#third row
button_sqrt=tk.Button(button_frame, text="√",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="OrangeRed", width = 8, height = 2, command = lambda : matfun("√")).grid(row = 3, column = 0)
button_power=tk.Button(button_frame, text="10^x",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="OrangeRed", width = 8, height = 2, command = lambda: matfun("10^x")).grid(row = 3, column = 1)
button_log=tk.Button(button_frame, text="log",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="OrangeRed", width = 8, height = 2, command = lambda : matfun("log")).grid(row = 3, column = 2)
button_exp=tk.Button(button_frame, text="Exp",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="OrangeRed", width = 8, height = 2, command = lambda : matfun("Exp")).grid(row = 3, column = 3)
button_Mod=tk.Button(button_frame, text="Mod",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="OrangeRed", width = 8, height = 2, command = lambda : operations("%")).grid(row = 3, column = 4)

#fourt row
button_empty=tk.Button(button_frame, text="",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="red", width = 8, height = 2).grid(row = 4, column = 0)
button_ce=tk.Button(button_frame, text="CE",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="red", width = 8, height = 2, command = lambda : clear_press()).grid(row = 4, column = 1)
button_c=tk.Button(button_frame, text="C",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="red", width = 8, height = 2, command = lambda : clear(equation)).grid(row = 4, column = 2)
button_empty=tk.Button(button_frame, text="",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="red", width = 8, height = 2).grid(row = 4, column = 3)
button_division=tk.Button(button_frame, text="÷",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="red", width = 8, height = 2, command =lambda : operations("/")).grid(row = 4, column = 4)

#fifth row
button_pi=tk.Button(button_frame, text="π",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="firebrick2", width = 8, height = 2, command =lambda: matfun("π")).grid(row = 5, column = 0)

button_seven=tk.Button(button_frame, text = "7",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="firebrick2", width = 8, height = 2, command = lambda :click_numb(7)).grid(row = 5, column = 1)

button_eight=tk.Button(button_frame, text="8",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="firebrick2", width = 8, height = 2, command = lambda : click_numb(8)).grid(row = 5, column = 2)

button_nine=tk.Button(button_frame, text="9",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="firebrick2", width = 8, height = 2, command = lambda : click_numb(9)).grid(row = 5, column = 3)

button_multipl=tk.Button(button_frame, text="x",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="firebrick2", width = 8, height = 2, command = lambda: operations("*")).grid(row = 5, column = 4)

#sixth row
button_perm=tk.Button(button_frame, text="n!",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="VioletRed", width = 8, height = 2, command = lambda  : fact()).grid(row = 6, column = 0)

button_four=tk.Button(button_frame, text="4",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="VioletRed", width = 8, height = 2, command = lambda : click_numb(4)).grid(row = 6, column = 1)

button_five=tk.Button(button_frame, text="5",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="VioletRed", width = 8, height = 2, command = lambda : click_numb(5)).grid(row = 6, column = 2)

button_six=tk.Button(button_frame, text="6",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="VioletRed", width = 8, height = 2, command = lambda : click_numb(6)).grid(row = 6, column = 3)

button_sub=tk.Button(button_frame, text="-",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="VioletRed", width = 8, height = 2, command = lambda: operations("-")).grid(row = 6, column = 4)

#seventh row
button_plusminus=tk.Button(button_frame, text="±",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="deepskyblue", width = 8, height = 2, command = lambda : matfun("±")).grid(row = 7, column = 0)

button_one=tk.Button(button_frame, text="1",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="deepskyblue", width = 8, height = 2, command = lambda : click_numb(1)).grid(row = 7, column = 1)

button_two=tk.Button(button_frame, text="2",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="deepskyblue", width = 8, height = 2, command = lambda : click_numb(2)).grid(row = 7, column = 2)

button_three=tk.Button(button_frame, text="3",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="deepskyblue", width = 8, height = 2, command = lambda : click_numb(3)).grid(row = 7, column = 3)

button_add=tk.Button(button_frame, text="+",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg = "deepskyblue", width = 8, height = 2, command = lambda :operations("+")).grid(row = 7, column = 4)

#eight row
button_deg=tk.Button(button_frame, text="Deg",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="lawngreen", width = 8, height = 3, command = lambda : press(math.degrees(float(expression)),equation)).grid(row = 8, column = 0)

button_rad=tk.Button(button_frame, text="Rad",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="lawngreen", width = 8, height = 3, command = lambda : press(math.radians(float(expression)),equation)).grid(row = 8, column = 1)

button_null=tk.Button(button_frame, text="0",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="lawngreen", width = 8, height = 3, command = lambda : click_numb(0)).grid(row = 8, column = 2)

button_point=tk.Button(button_frame, text=".",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="lawngreen", width = 8, height = 3, command = lambda : click_numb(".")).grid(row = 8, column = 3)

button_equal=tk.Button(button_frame, text="=",font=("arial",12), relief="ridge", 
                   borderwidth=1, bg="lawngreen", width =8, height = 3, command = lambda : equalpress()).grid(row = 8, column = 4)


window.mainloop()

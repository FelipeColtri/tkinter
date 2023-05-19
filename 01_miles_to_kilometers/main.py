import tkinter as tk
from tkinter import ttk

def Convert():
    kilo_value = float(et_field.get()) * 1.61
    lb_output_value.set(kilo_value)

# Window
window = tk.Tk()
window.title('Kilometers to Miles')
window.geometry('500x150')

# Title
lb_title = ttk.Label(window, text='Convert Miles to Kilometers', font='Calibri 25 bold')
lb_title.pack(pady=10)

# Input
fm_input = ttk.Frame(window)
fm_input.pack()

et_value = tk.IntVar()
et_field = ttk.Entry(fm_input, textvariable=et_value)
et_field.pack(side='left', padx=50)

bt_convert = ttk.Button(fm_input, text='Convert', command=Convert)
bt_convert.pack(side='right', padx=50)

# Output
fm_output = ttk.Frame(window)
fm_output.pack()

lb_output_value = tk.StringVar() 
lb_output = ttk.Label(fm_output, textvariable=lb_output_value, font='Calibri 20')
lb_output.pack(pady=10)

# Run
window.mainloop()

import ttkbootstrap as ttk

"""
    Tests with variables and different types of buttons.
"""

# Function Reset 
def Reset ():
    var_lable.set('Click in Check Button to enable Radio Buttons')
    var_check.set(False)
    var_radio.set(0)
    bt_rd1['state'] = 'disable'
    bt_rd2['state'] = 'disable'

def Enable_Options ():
    var_radio.set(0)
    
    if var_check.get():
        var_lable.set('Options Enabled')
        bt_rd1['state'] = 'enable'
        bt_rd2['state'] = 'enable'
    else:
        var_lable.set('Options Disabled')
        bt_rd1['state'] = 'disable'
        bt_rd2['state'] = 'disable'

def Select_Option ():
    if var_radio.get() == 1:
        var_lable.set('Option 1 Selected')
    else:
        var_lable.set('Option 2 Selected')

# Window
window = ttk.Window('Buttons And Variables', 'cyborg', size=(500, 300))

# Variables
var_lable = ttk.StringVar(value='Click in Check Button to enable Radio Buttons')
var_check = ttk.BooleanVar()
var_radio = ttk.IntVar()

# Widgets
lb_text = ttk.Label(window, textvariable=var_lable)
bt_ck = ttk.Checkbutton(window, text='Enable Options', variable=var_check, command=Enable_Options)
bt_rd1 = ttk.Radiobutton(window, text='Option 1', value=1, variable=var_radio, command=Select_Option)
bt_rd2 = ttk.Radiobutton(window, text='Option 2', value=2, variable=var_radio, command=Select_Option)
bt_simple = ttk.Button(window, text='Reset Button', command=Reset)

# Lauout
lb_text.pack(pady=10)
bt_ck.pack(pady=10)
bt_rd1.pack()
bt_rd2.pack()
bt_simple.pack(pady=20)

# Initial Configurations
var_check.set(False)
bt_rd1['state'] = 'disable'
bt_rd2['state'] = 'disable'

# Run
window.mainloop()

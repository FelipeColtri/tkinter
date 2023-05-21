import ttkbootstrap as ttk

"""
    Creates a window with a Label, an Entry and two Bottons. The first Button when pressed changes the Label's text to what is written in the Entry and deactivates it. The second Button when pressed resets to original settings. Using ttkbootstrap and anoter things.
"""

def Change_Text ():
    lb_text['text'] = var_text.get()
    et_text['state'] = 'disabled'
    bt_text['state'] = 'disabled'
    bt_reset['state'] = 'enabled'

def Reset_Conf ():
    lb_text['text'] = 'Hello!'
    et_text['state'] = 'enabled'
    bt_text['state'] = 'enabled'
    bt_reset['state'] = 'disabled'
    var_text.set('')
    et_text.focus()

# Window
window = ttk.Window(title='Change Configurations', themename='darkly', size=(250, 120))

# Widgets
lb_text = ttk.Label(window, text='Hello!')
lb_text.pack()

var_text = ttk.StringVar() 
et_text = ttk.Entry(window, textvariable=var_text)
et_text.pack()

bt_text = ttk.Button(window, text='Set', command=Change_Text)
bt_text.pack()

bt_reset = ttk.Button(window, text='Reset', command=Reset_Conf)
bt_reset.pack()

# Initial Confs
bt_reset['state'] = 'disabled'
et_text.focus()

# Run
window.mainloop()

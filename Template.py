from tkinter import *

# Create the main window
mainWindow = Tk()

# WINDOW SETTINGS
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
WINDOW_RESIZE = False
WINDOW_TITLE = "Window_Title_Goes_Here"
WINDOW_CURSOR = "arrow"
WINDOW_ICON = PhotoImage(file=r'Images\Icon.png')
WINDOW_SIZE = f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}"
WINDOW_HLTHICK = 2
WINDOW_HL_BACKGROUND = "white"
WINDOW_TAKE_FOCUS = True

# Apply window settings
mainWindow.title(WINDOW_TITLE)
mainWindow.geometry(WINDOW_SIZE)
mainWindow.iconphoto(True, WINDOW_ICON)
mainWindow.configure(cursor=WINDOW_CURSOR)                      # Set cursor
mainWindow.configure(highlightthickness=WINDOW_HLTHICK)         # Set highlight border width
mainWindow.configure(highlightbackground=WINDOW_HL_BACKGROUND)  # Set highlight border color
mainWindow.configure(takefocus=WINDOW_TAKE_FOCUS) 

# Label widget
label = Label(mainWindow, text="Label Widget")
label.config(bg="lightblue", fg="black", font=("Arial", 12))
label.pack()

# Entry widget
entry = Entry(mainWindow)
entry.pack()

# Text widget
text = Text(mainWindow, width=30, height=5)
text.pack()

# Frame widget
frame = Frame(mainWindow, bg="lightgray", width=200, height=100, bd=2, relief="groove")
frame.pack()

# Checkbutton widget
checkbutton = Checkbutton(mainWindow, text="Checkbutton")
checkbutton.pack()

# Radiobutton widget
radiobutton = Radiobutton(mainWindow, text="Radiobutton")
radiobutton.pack()

# Scale widget
scale = Scale(mainWindow, from_=0, to=10, orient=HORIZONTAL)
scale.pack()

# Listbox widget
listbox = Listbox(mainWindow)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
listbox.pack()

# Scrollbar widget
scrollbar = Scrollbar(mainWindow)
scrollbar.pack(side=RIGHT, fill=Y)

# Attach Scrollbar to Listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Menu widget
menu = Menu(mainWindow)
menu.add_command(label="File")
menu.add_command(label="Edit")
menu.add_command(label="View")
mainWindow.config(menu=menu)

mainWindow.mainloop()

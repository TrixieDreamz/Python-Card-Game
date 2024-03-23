import tkinter as tk
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
label = tk.Label(
    mainWindow,
    text="Hello, World!",            # Text to display
    anchor="center",                  # Alignment of text within the widget (N, NE, E, SE, S, SW, W, NW, or CENTER)
    background="black",          # Background color
    bd=3,                            # Border width
    bitmap="info",                   # Bitmap to display
    compound="left",                 # How to display the bitmap relative to the text
    cursor="hand2",                  # Cursor to display when mouse is over the widget
    font=("Arial", 12, "bold"),      # Font of the text
    fg="white",                      # Foreground color (text color)
    height=2,                        # Height of the widget in text lines
    highlightbackground="black",     # Color of the focus highlight when widget doesn't have focus
    highlightcolor="red",            # Color of the focus highlight when widget has focus
    highlightthickness=2,            # Thickness of the focus highlight
    image=None,                      # Image to display
    justify="center",                # Justification of text (LEFT, RIGHT, or CENTER)
    padx=10,                         # Horizontal padding
    pady=5,                          # Vertical padding
    relief="solid",                  # Border decoration (FLAT, SUNKEN, RAISED, GROOVE, or RIDGE)
    takefocus=True,                  # Whether the widget can take keyboard focus
    textvariable=None,               # Tkinter variable containing the text
    underline=1,                     # Index of the character to underline
    wraplength=200,                  # Maximum line length before wrapping
    width=100,                        # Width of the widget in characters
)
label.pack()

entry = tk.Entry(
    mainWindow,
    bd=3,                           # Border width
    bg="white",                 # Background color
    cursor="xterm",                 # Cursor to display when mouse is over the widget
    exportselection=True,           # Whether the selection is exported to the clipboard
    font=("Arial", 12),             # Font of the text
    fg="black",                     # Foreground color (text color)
    highlightbackground="black",    # Color of the focus highlight when widget doesn't have focus
    highlightcolor="red",           # Color of the focus highlight when widget has focus
    highlightthickness=2,           # Thickness of the focus highlight
    insertbackground="blue",        # Color of the insertion cursor
    insertborderwidth=2,            # Border width of the insertion cursor
    insertofftime=300,              # Time in milliseconds to wait before turning off the insertion cursor
    insertontime=600,               # Time in milliseconds to wait before turning on the insertion cursor
    insertwidth=4,                  # Width of the insertion cursor
    justify="center",               # Justification of text (LEFT, RIGHT, or CENTER)
    relief="solid",                 # Border decoration (FLAT, SUNKEN, RAISED, GROOVE, or RIDGE)
    selectbackground="yellow",     # Background color of the selected text
    selectborderwidth=2,            # Border width of the selected text
    selectforeground="green",      # Foreground color of the selected text
    show="*",                      # Character to display instead of the actual text (for password entry)
    state="normal",                # State of the widget (NORMAL, DISABLED, or READONLY)
    takefocus=True,                # Whether the widget can take keyboard focus
    textvariable=None,             # Tkinter variable containing the text
    width=30,                      # Width of the widget in characters
    xscrollcommand=None,           # Scrollbar command for horizontal scrolling
)
entry.pack()

# Creating a Text widget with many possible arguments
text_widget = tk.Text(
    mainWindow,
    bd=3,                           # Border width
    bg="lightblue",                 # Background color
    cursor="xterm",                 # Cursor to display when mouse is over the widget
    exportselection=True,           # Whether the selection is exported to the clipboard
    font=("Arial", 12),             # Font of the text
    fg="black",                     # Foreground color (text color)
    height=10,                      # Height of the widget in text lines
    highlightbackground="black",    # Color of the focus highlight when widget doesn't have focus
    highlightcolor="red",           # Color of the focus highlight when widget has focus
    highlightthickness=2,           # Thickness of the focus highlight
    insertbackground="blue",        # Color of the insertion cursor
    insertborderwidth=2,            # Border width of the insertion cursor
    insertofftime=300,              # Time in milliseconds to wait before turning off the insertion cursor
    insertontime=600,               # Time in milliseconds to wait before turning on the insertion cursor
    insertwidth=4,                  # Width of the insertion cursor
    padx=5,                         # Horizontal padding
    pady=5,                         # Vertical padding
    relief="solid",                 # Border decoration (FLAT, SUNKEN, RAISED, GROOVE, or RIDGE)
    selectbackground="yellow",     # Background color of the selected text
    selectborderwidth=2,            # Border width of the selected text
    selectforeground="green",      # Foreground color of the selected text
    spacing1=3,                    # Spacing above each line
    spacing2=3,                    # Spacing between wrapped lines
    spacing3=3,                    # Spacing below each line
    state="normal",                # State of the widget (NORMAL, DISABLED, or READONLY)
    takefocus=True,                # Whether the widget can take keyboard focus
    width=30,                      # Width of the widget in characters
    wrap="word",                   # How to wrap lines (NONE, CHAR, or WORD)
    xscrollcommand=None,           # Scrollbar command for horizontal scrolling
    yscrollcommand=None,           # Scrollbar command for vertical scrolling
)

text_widget.pack()

# Creating a Frame widget with many possible arguments
frame = tk.Frame(
    mainWindow,
    bd=3,                           # Border width
    bg="green",                 # Background color
    cursor="xterm",                 # Cursor to display when mouse is over the widget
    height=200,                     # Height of the widget
    highlightbackground="black",    # Color of the focus highlight when widget doesn't have focus
    highlightcolor="red",           # Color of the focus highlight when widget has focus
    highlightthickness=2,           # Thickness of the focus highlight
    padx=5,                         # Horizontal padding
    pady=5,                         # Vertical padding
    relief="solid",                 # Border decoration (FLAT, SUNKEN, RAISED, GROOVE, or RIDGE)
    takefocus=True,                # Whether the widget can take keyboard focus
    width=300,                      # Width of the widget
)
frame.pack()

# Checkbutton widget
checkbutton_var = tk.BooleanVar()
checkbutton_var.set(False)  # Initial state

checkbutton = tk.Checkbutton(
    mainWindow,
    text="Checkbutton",                 # Text to display next to the button
    variable=checkbutton_var,           # Tkinter variable linked to the button state
    onvalue=True,                       # Value when the button is checked
    offvalue=False,                     # Value when the button is unchecked
    anchor="w",                         # Alignment of the text (N, NE, E, SE, S, SW, W, NW)
    bg="lightblue",                     # Background color
    bd=3,                               # Border width
    command=lambda: print(checkbutton_var.get()),  # Function to call when the button is clicked
    cursor="hand2",                     # Cursor to display when mouse is over the widget
    font=("Arial", 12, "bold"),         # Font of the text
    fg="black",                         # Foreground color (text color)
    height=2,                           # Height of the widget
    highlightbackground="black",        # Color of the focus highlight when widget doesn't have focus
    highlightcolor="red",               # Color of the focus highlight when widget has focus
    highlightthickness=2,               # Thickness of the focus highlight
    image=None,                         # Image to display
    justify="left",                     # Justification of text (LEFT, RIGHT, or CENTER)
    offrelief="flat",                   # Relief style when button is unchecked (FLAT, RAISED, SUNKEN, GROOVE, RIDGE)
    overrelief="raised",                # Relief style when mouse is over the widget (RAISED, SUNKEN, GROOVE, RIDGE)
    padx=10,                            # Horizontal padding
    pady=5,                             # Vertical padding
    selectcolor="yellow",               # Color when button is selected
    selectimage=None,                   # Image to display when button is selected
    state="normal",                     # State of the widget (NORMAL, DISABLED, or ACTIVE)
    underline=0,                        # Index of the character to underline
    wraplength=200,                     # Maximum line length before wrapping
)
checkbutton.pack()


radio_var = tk.StringVar()
radio_var.set("Option 1")  # Initial value

radio_button1 = tk.Radiobutton(
    mainWindow,
    text="Option 1",                  # Text to display next to the button
    variable=radio_var,               # Tkinter variable linked to the button state
    value="Option 1",                 # Value of the button when selected
    indicatoron=1,                    # Display the indicator as a separate element
    anchor="w",                       # Alignment of the text (N, NE, E, SE, S, SW, W, NW)
    bg="lightblue",                   # Background color
    bd=3,                             # Border width
    command=lambda: print(radio_var.get()),  # Function to call when the button is clicked
    cursor="hand2",                   # Cursor to display when mouse is over the widget
    font=("Arial", 12, "bold"),       # Font of the text
    fg="black",                       # Foreground color (text color)
    height=2,                         # Height of the widget
    highlightbackground="black",      # Color of the focus highlight when widget doesn't have focus
    highlightcolor="red",             # Color of the focus highlight when widget has focus
    highlightthickness=2,             # Thickness of the focus highlight
    image=None,                       # Image to display
    justify="left",                   # Justification of text (LEFT, RIGHT, or CENTER)
    padx=10,                          # Horizontal padding
    pady=5,                           # Vertical padding
    relief="solid",                   # Border decoration (FLAT, SUNKEN, RAISED, GROOVE, or RIDGE)
    selectcolor="yellow",             # Color when button is selected
    selectimage=None,                 # Image to display when button is selected
    state="normal",                   # State of the widget (NORMAL, DISABLED, or ACTIVE)
    underline=0,                      # Index of the character to underline
    wraplength=200,                   # Maximum line length before wrapping
)

radio_button2 = tk.Radiobutton(
    mainWindow,
    text="Option 2",
    variable=radio_var,
    value="Option 2",
    indicatoron=1,
    anchor="w",
    bg="lightblue",
    bd=3,
    command=lambda: print(radio_var.get()),
    cursor="hand2",
    font=("Arial", 12, "bold"),
    fg="black",
    height=2,
    highlightbackground="black",
    highlightcolor="red",
    highlightthickness=2,
    image=None,
    justify="left",
    padx=10,
    pady=5,
    relief="solid",
    selectcolor="yellow",
    selectimage=None,
    state="normal",
    underline=0,
    wraplength=200,
)

radio_button1.pack()
radio_button2.pack()

scale = tk.Scale(
    mainWindow,
    from_=0,                        # Minimum value
    to=100,                         # Maximum value
    orient="horizontal",            # Orientation of the scale (HORIZONTAL or VERTICAL)
    length=200,                     # Length of the scale in pixels
    width=20,                       # Width of the scale in pixels
    showvalue=True,                 # Whether to display the current value next to the slider
    sliderlength=20,                # Length of the slider in pixels
    sliderrelief="flat",            # Relief style of the slider (FLAT, RAISED, SUNKEN, GROOVE, RIDGE)
    bd=3,                           # Border width
    bg="lightblue",                 # Background color
    fg="black",                     # Foreground color (text color)
    troughcolor="gray",             # Color of the trough (the area behind the slider)
    activebackground="lightgreen",  # Background color when the mouse is over the widget
    highlightbackground="black",    # Color of the focus highlight when widget doesn't have focus
    highlightcolor="red",           # Color of the focus highlight when widget has focus
    highlightthickness=2,           # Thickness of the focus highlight
    command=lambda value: print(value),  # Function to call when the slider value changes
    resolution=1,                   # Granularity of the values (e.g., if set to 0.1, the slider will stop at 0.1 increments)
    repeatdelay=500,                # Delay in milliseconds before repeating commands when slider is clicked and held
    repeatinterval=100,             # Interval in milliseconds between repeating commands when slider is clicked and held
    state="normal",                 # State of the widget (NORMAL, DISABLED, or ACTIVE)
    takefocus=True,                 # Whether the widget can take keyboard focus
    variable=None,                  # Tkinter variable to link the scale value
)
scale.pack()

# Creating a Listbox widget with many possible arguments
listbox = tk.Listbox(
    mainWindow,
    bd=3,                           # Border width
    bg="lightblue",                 # Background color
    cursor="arrow",                 # Cursor to display when mouse is over the widget
    exportselection=True,           # Whether the selection is exported to the clipboard
    font=("Arial", 12),             # Font of the text
    fg="black",                     # Foreground color (text color)
    height=5,                       # Height of the widget in lines
    highlightbackground="black",    # Color of the focus highlight when widget doesn't have focus
    highlightcolor="red",           # Color of the focus highlight when widget has focus
    highlightthickness=2,           # Thickness of the focus highlight
    justify="center",               # Justification of text (LEFT, RIGHT, or CENTER)
    relief="solid",                 # Border decoration (FLAT, SUNKEN, RAISED, GROOVE, or RIDGE)
    selectbackground="yellow",     # Background color of the selected item
    selectborderwidth=2,            # Border width of the selected item
    selectforeground="green",      # Foreground color of the selected item
    selectmode="extended",          # Selection mode (BROWSE, SINGLE, MULTIPLE, or EXTENDED)
    setgrid=False,                  # Whether to display gridlines
    takefocus=True,                # Whether the widget can take keyboard focus
    width=20,                       # Width of the widget in characters
    xscrollcommand=None,           # Scrollbar command for horizontal scrolling
    yscrollcommand=None,           # Scrollbar command for vertical scrolling
)
# Inserting items into the Listbox
for i in range(10):
    listbox.insert(tk.END, f"Item {i}")
listbox.pack()

# Creating a Scrollbar widget with many possible arguments
scrollbar = tk.Scrollbar(
    mainWindow,
    activebackground="lightgreen",  # Background color when the mouse is over the widget
    bd=3,                           # Border width
    bg="black",                 # Background color
    command=None,                   # Function to call when the scrollbar is moved
    cursor="arrow",                 # Cursor to display when mouse is over the widget
    elementborderwidth=2,           # Border width of the trough
    highlightbackground="black",    # Color of the focus highlight when widget doesn't have focus
    highlightcolor="red",           # Color of the focus highlight when widget has focus
    highlightthickness=2,           # Thickness of the focus highlight
    jump=1,                         # Whether to jump to the mouse position when clicked
    orient="vertical",              # Orientation of the scrollbar (VERTICAL or HORIZONTAL)
    relief="raised",                  # Border decoration (FLAT, SUNKEN, RAISED, GROOVE, or RIDGE)
    repeatdelay=500,                # Delay in milliseconds before repeating commands when pressed and held
    repeatinterval=100,             # Interval in milliseconds between repeating commands when pressed and held
    takefocus=True,                # Whether the widget can take keyboard focus
    troughcolor="blue",             # Color of the trough
    width=20,                       # Width of the scrollbar in pixels
)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
# Attach Scrollbar to Listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

menu = tk.Menu(
    mainWindow,
    activebackground="lightgreen",      # Background color when the mouse is over the widget
    activeborderwidth=2,                # Border width when the widget is active
    activeforeground="black",           # Foreground color when the widget is active
    bg="lightblue",                     # Background color
    bd=3,                               # Border width
    cursor="arrow",                     # Cursor to display when mouse is over the widget
    font=("Arial", 12),                 # Font of the text
    fg="black",                         # Foreground color (text color)
    postcommand=None,                   # Function to call when the menu is displayed
    relief="solid",                     # Border decoration (FLAT, SUNKEN, RAISED, GROOVE, or RIDGE)
    selectcolor="yellow",               # Background color when item is selected
    tearoff=0,                          # Whether the menu can be torn off
    takefocus=True,                    # Whether the widget can take keyboard focus
    tearoffcommand=None,               # Function to call when the menu is torn off
    title="Menu Title",                 # Title of the menu
    type="menubar",                     # Type of the menu (MENUBAR, TEAROFF, or NORMAL)

)

# Adding items to the menu
menu.add_command(label="Item 1", command=lambda: print("Item 1 selected"))
menu.add_command(label="Item 2", command=lambda: print("Item 2 selected"))

# Adding submenus
submenu = tk.Menu(menu, tearoff=0)
submenu.add_command(label="Subitem 1", command=lambda: print("Subitem 1 selected"))
submenu.add_command(label="Subitem 2", command=lambda: print("Subitem 2 selected"))
menu.add_cascade(label="Submenu", menu=submenu)

# Displaying the menu
mainWindow.config(menu=menu)

mainWindow.mainloop()

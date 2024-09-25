import pyautogui
import tkinter as tk
from tkinter.filedialog import *

# Initialize Tk widget
root = tk.Tk()

# Add Tk widget title
root.title("Screen Grabber")

# Add canvas
canvas1 = tk.Canvas(root, width=300, height=300)

# Define screenshot function
def takeScreenshot():
    # Take screenshot
    myscreenshot = pyautogui.screenshot()

    # Get screenshot name
    save_path = asksaveasfilename()

    # Save screenshot
    myscreenshot.save(save_path+"_screenshot.png")

# Add button
myButton = tk.Button(text="Take Screenshot", command=takeScreenshot, font=10)

# Create window
canvas1.create_window(150,150,window=myButton)

# Pack canvas
canvas1.pack(anchor="center")

# Call Tk mainloop
root.mainloop()
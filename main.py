import pyautogui

import time

import tkinter as tk
from tkinter.filedialog import asksaveasfilename

def main():
    # Initialize Tk widget
    root = tk.Tk()

    # Add Tk widget title
    root.title("Screen Grabber")

    # Add canvas
    canvas1 = tk.Canvas(root, width=300, height=300)

    # Add button
    myButton = tk.Button(text="Take Screenshot", command=lambda: takeScreenshot(root), font=10)

    # Create window
    canvas1.create_window(150,150,window=myButton)
    canvas1.pack(anchor="center")

    # Run app
    root.mainloop()

# Define screenshot function
def takeScreenshot(root):
    # Hide app
    root.withdraw()

    # Delay for window to hide
    time.sleep(0.1)

    # Take screenshot
    myscreenshot = pyautogui.screenshot()

    # Get screenshot name
    save_path = asksaveasfilename(title="Select Images", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    # Save screenshot
    myscreenshot.save(save_path+"_screenshot.png")

    # Unhide window
    root.deiconify()

if __name__ == "__main__":
    main()
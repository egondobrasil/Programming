import tkinter as tk

def get_window_size(window):
    # Update the window to ensure dimensions are current
    window.update() 
    width = window.winfo_width()
    height = window.winfo_height()
    return width, height

root = tk.Tk()
root.geometry("400x300") # Set an initial size
root.title("Window Size Example")

width, height = get_window_size(root)
print(f"Window size: {width}x{height} pixels")

# Example of getting size after a user-initiated resize (requires mainloop)
def on_resize(event):
    current_width = root.winfo_width()
    current_height = root.winfo_height()
    print(f"Window resized to: {current_width}x{current_height} pixels")

root.bind("<Configure>", on_resize)
root.mainloop()

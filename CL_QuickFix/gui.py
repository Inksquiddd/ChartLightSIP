import tkinter as tk

def countdown(time_left):
    if time_left > 0:
        label.config(text=f"{time_left} seconds remaining")
        root.after(1000, countdown, time_left - 1)  # Schedule the next update in 1 second
    else:
        label.config(text="Time's up!")

# Create the main Tkinter window
root = tk.Tk()
root.title("Countdown Timer")

# Create a label to display the countdown
label = tk.Label(root, text="5 seconds remaining", font=("Arial", 24))
label.pack(pady=20)

# Start the countdown
countdown(5)

# Run the Tkinter event loop
root.mainloop()

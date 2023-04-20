import tkinter as tk
import datetime
import math

# Create the window
window = tk.Tk()
window.title("Circle Clock")

# Create the canvas
canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()

# Draw the circle
canvas.create_oval(50, 50, 550, 550, fill='white', outline='black')

# Draw the center of the circle
canvas.create_oval(250, 250, 350, 350, fill='black', outline='black')

# Draw the hour hand
hour_hand = canvas.create_line(300, 300, 300, 200, width=15, fill='black')

# Draw the minute hand
minute_hand = canvas.create_line(300, 300, 300, 150, width=10, fill='black')

# Draw the second hand
second_hand = canvas.create_line(300, 300, 300, 100, width=5, fill='red')

# Draw the numbers
for i in range(12, 24):
    angle = (i / 12) * 2 * math.pi
    x = 300 + 225 * math.sin(angle)
    y = 300 - 225 * math.cos(angle)
    canvas.create_text(x, y, text=str(i + 1), font=("Arial", 16), fill='black')


# Update the hands with the current time
def update_time():
    # Get the current time
    current_time = datetime.datetime.now()

    # Get the hour, minute, and second as angles
    hour = current_time.hour % 12
    minute = current_time.minute
    second = current_time.second

    # Convert the angles to radians
    hour_angle = (hour / 12) * 2 * math.pi
    minute_angle = (minute / 60) * 2 * math.pi
    second_angle = (second / 60) * 2 * math.pi

    # Update the hour hand
    canvas.coords(hour_hand, 300, 300, 300 + 100 * math.sin(hour_angle), 300 - 100 * math.cos(hour_angle))

    # Update the minute hand
    canvas.coords(minute_hand, 300, 300, 300 + 150 * math.sin(minute_angle), 300 - 150 * math.cos(minute_angle))

    # Update the second hand
    canvas.coords(second_hand, 300, 300, 300 + 200 * math.sin(second_angle), 300 - 200 * math.cos(second_angle))

    # Schedule the next update
    window.after(1000, update_time)


# Start the update loop
update_time()

# Run the tkinter event loop
window.mainloop()

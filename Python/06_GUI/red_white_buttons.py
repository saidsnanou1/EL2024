import tkinter as tk

class LEDControlApp:
    
    def __init__(self, master):
        self.master = master
        self.master.title("LED Control")

        # Variables to track LED state
        self.led_state = tk.StringVar()
        self.led_state.set("OFF")  # Initial state

        # Canvas for drawing
        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack()

        # Draw the circle
        self.circle = self.canvas.create_oval(50, 50, 150, 150, fill="white")

        # Buttons to control the LED
        self.on_button = tk.Button(master, text="ON", command=lambda: self.toggle_led("on"))
        self.on_button.pack(side=tk.LEFT, padx=10)

        self.off_button = tk.Button(master, text="OFF", command=lambda: self.toggle_led("off"))
        self.off_button.pack(side=tk.RIGHT, padx=10)

        # Label to display LED state
        self.state_label = tk.Label(master, textvariable=self.led_state, font=("Arial", 18))
        self.state_label.pack(pady=20)

    def toggle_led(self, state):
        if state == "on":
            self.led_state.set("ON")
            self.canvas.itemconfig(self.circle, fill="red")
        elif state == "off":
            self.led_state.set("OFF")
            self.canvas.itemconfig(self.circle, fill="white")

# Create the main application window
root = tk.Tk()
app = LEDControlApp(root)

# Run the application
root.mainloop()

import tkinter as tk
from tkinter import messagebox

class FactorialCalculator:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Factorial Calculator")

        self.label = tk.Label(master, text="Enter an integer N:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.calculate_button = tk.Button(master, text="Calculate Factorial", command=self.calculate_factorial)
        self.calculate_button.pack()

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def calculate_factorial(self):
        try:
            num = int(self.entry.get())

            result = self.factorial(num)

            messagebox.showinfo("Factorial Result", f"The factorial of {num} is {result}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

# Create the main application window
root = tk.Tk()
app = FactorialCalculator(root)

# Run the application
root.mainloop()

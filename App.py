import tkinter as tk
import random

quotes = [
    "Life is what happens when you're busy making other plans. – John Lennon",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. – Nelson Mandela",
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
    "If life were predictable it would cease to be life, and be without flavor. – Eleanor Roosevelt",
]

def show_random_quote():
    """Display a random quote from the list."""
    quote = random.choice(quotes)
    label_quote.config(text=quote)

def create_quote_generator():
    """Create a simple random quote generator GUI."""
    root = tk.Tk()
    root.title("Random Quote Generator")

    global label_quote

    # Display random quote
    label_quote = tk.Label(root, text="", wraplength=300, justify="center", font=("Arial", 14))
    label_quote.pack(pady=20)

    # Button to generate random quote
    tk.Button(root, text="Generate Random Quote", command=show_random_quote).pack(pady=20)

    show_random_quote()  # Show a quote when the app starts

    root.mainloop()

if __name__ == "__main__":
    create_quote_generator()

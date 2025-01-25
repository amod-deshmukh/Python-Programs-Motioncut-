import random  # Importing the random module for random selections
import tkinter as tk  # Importing tkinter for GUI creation
from tkinter import messagebox  # Importing messagebox for dialog windows

# Predefined lists of adjectives and nouns to generate usernames
adjectives = ["Cool", "Happy", "Brave", "Charming", "Witty", "Silly", "Phantom", "Mystic","Celestial"]
nouns = ["Tiger", "Dragon", "Unicorn", "Phoenix", "Warrior", "Pirate","Raven","Serpent","Reaper"]

def generate_username(include_numbers=True, include_special_chars=True):
    """
    Generates a random username based on user preferences for numbers and special characters.
    """
    # Randomly choose one adjective and one noun
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    
    # Combine the adjective and noun to form the base of the username
    username = adj + noun
    
    # Optionally add random numbers to the username
    if include_numbers:
        username += str(random.randint(0, 999))
    
    # Optionally add a random special character to the username
    if include_special_chars:
        special_chars = "!@#$%^&*"
        username += random.choice(special_chars)
    
    return username

def save_to_file(username, filename="usernames.txt"):
    """
    Saves the generated username to a file.
    """
    with open(filename, "a") as file:  # Open the file in append mode
        file.write(username + "\n")  # Write the username followed by a newline

def generate_username_gui():
    """
    Handles the GUI action to generate a username based on the user's preferences.
    """
    # Get user preferences from the GUI checkboxes
    include_numbers = include_numbers_var.get()
    include_special_chars = include_special_chars_var.get()
    
    # Generate a username and display it in the label
    username = generate_username(include_numbers, include_special_chars)
    username_label.config(text=f"Generated Username: {username}")

def save_username_gui():
    """
    Handles the GUI action to save the currently displayed username to a file.
    """
    # Get the current username from the label
    username = username_label.cget("text").replace("Generated Username: ", "")
    
    # Check if there is a username to save
    if username:
        save_to_file(username)  # Save the username to a file
        messagebox.showinfo("Success", "Username saved to 'usernames.txt'.")  # Show success message
    else:
        # Show a warning if no username has been generated yet
        messagebox.showwarning("No Username", "No username to save! Generate one first.")

# Create the main GUI application window
root = tk.Tk()
root.title("Random Username Generator")  # Set the window title

# Create and display the title label
title_label = tk.Label(root, text="Random Username Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Variables to track the state of the checkboxes
include_numbers_var = tk.BooleanVar(value=True)  # Default to include numbers
include_special_chars_var = tk.BooleanVar(value=True)  # Default to include special characters

# Checkboxes for user preferences
numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=include_numbers_var)
special_chars_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=include_special_chars_var)

numbers_checkbox.pack()  # Display the checkbox for including numbers
special_chars_checkbox.pack()  # Display the checkbox for including special characters

# Button to generate a username
generate_button = tk.Button(root, text="Generate Username", command=generate_username_gui)
generate_button.pack(pady=10)

# Label to display the generated username
username_label = tk.Label(root, text="Generated Username: None", font=("Arial", 12))
username_label.pack(pady=10)

# Button to save the generated username
save_button = tk.Button(root, text="Save Username", command=save_username_gui)
save_button.pack(pady=10)

# Start the main event loop to display the GUI
root.mainloop()

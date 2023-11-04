import tkinter as tk
from tkinter import PhotoImage
from tkinter import font

# Create a function to start the game with the selected difficulty level
def start_game(difficulty):
    if difficulty == 'Dancing Queen by ABBA' or difficulty == 'Sorry by Justin Beiber' or difficulty == 'I Knew You Were Trouble by Taylor Swift' or difficulty == "Hips Don't Lie by Shakira" or difficulty == 'Something Just Like This by Coldplay and The Chainsmokers':
        print('hi')
        # startGame

# Create the main window
root = tk.Tk()
root.title("Just Dance Start Screen")

# Set the window size to be larger (e.g., 600x400)
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Load the image
image = PhotoImage(file="/Users/jennydong/Desktop/image-removebg-preview.png")  # Replace "logo.png" with your image file name

# Create a Label widget to display the image
# image_label = tk.Label(root, image=image)
# image_label.pack(pady=20)  # Add padding to separate the image from buttons

# Load the background image
background_image = background_image = PhotoImage(file="/Users/jennydong/Downloads/justDance3.png")  # Replace "background.png" with your image file name

# Create a label to display the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Make the label cover the entire window


# Create a frame to center the buttons
frame = tk.Frame(root)
frame.pack(expand=True)  # Expand the frame to fill the window


# Create a font object with your desired font properties
custom_font = font.Font(family="Times New Roman", size=20, weight="bold")

# Create and configure buttons for easy, medium, and hard difficulties
song_1 = tk.Button(root, text="Dancing Queen by ABBA", font = custom_font, command=lambda: start_game("Dancing Queen by ABBA"))
song_2 = tk.Button(root, text="Sorry by Justin Beiber", font = custom_font, command=lambda: start_game("Sorry by Justin Beiber"))
song_3 = tk.Button(root, text="I Knew You Were Trouble by Taylor Swift", font = custom_font, command=lambda: start_game("I Knew You Were Trouble by Taylor Swift"))
song_4 = tk.Button(root, text="Hips Don't Lie by Shakira", font = custom_font, command=lambda: start_game("Hips Don't Lie by Shakira"))
song_5 = tk.Button(root, text="Something Just Like This by Coldplay and The Chainsmokers", font = custom_font, command=lambda: start_game("Something Just Like This by Coldplay and The Chainsmokers"))


# Use the pack geometry manager to center the buttons
song_1.pack(side="top", pady=30)  # Add padding to separate the buttons
song_2.pack(side="top", pady=30)
song_3.pack(side="top", pady=30)
song_4.pack(side="top", pady=30)
song_5.pack(side="top", pady=30)


# Start the main loop
root.mainloop()

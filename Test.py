import tkinter as tk
from PIL import ImageTk, Image
import requests

# Create a window
window = tk.Tk()
window.title("Cake Time")

# Create a button
button = tk.Button(window, text="cake?")
button.pack()

# Create an empty label to display the image
image_label = tk.Label(window)
image_label.pack()

# Define a function to generate or retrieve a cake image
def generate_cake():
    # Get a random cake image from an API call
    response = requests.get("https://api.giphy.com/v1/gifs/random?api_key=YOUR_API_KEY")
    image_url = response.json()["data"]["images"]["original"]["url"]

    # Create an Image object from the URL
    image = Image.open(requests.get(image_url, stream=True).raw)

    # Create an ImageTk object from the Image object
    image_tk = ImageTk.PhotoImage(image)

    # Display the image in the label
    image_label.configure(image=image_tk)
    image_label.image = image_tk

# Bind the button to the generate_cake function
button.bind("<Button-1>", lambda event: generate_cake())

# Run the window
window.mainloop()
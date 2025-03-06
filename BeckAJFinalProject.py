#Author: AJ Beck
#Date written: 2/28/2025
#Assignment: Module 08 Final Project
#App that allows users to roll a dice for combat in DnD. Also prints out a message to the user showing the outcome of their roll.

import tkinter as tk #Import tkinter library for GUI development
from tkinter import Toplevel #Import specific widget
from PIL import Image, ImageTk #Import Image and ImageTk for handling image display and tkinter

import random #Import random function to be used for dice rolling

#Function to open the d20 window
def open_d20_window():
    d20_window = Toplevel(window) #Create a new window for d20 rolling
    d20_window.title("Rolling a d20") #Set the title of the d20 window
    d20_window.geometry("500x300") #Set the size of the d20 window
    d20_window.configure(bg='lightblue') #Set the background color of the d20 window

    #Load and display a JPEG image
    try:
        img = Image.open("C:/Users/ajbec/OneDrive/Desktop/DnD Coding Project/DnDd20.jpg").resize((150,150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img) #Convert the image into a format suitable for tkinter
        img_label = tk.Label(d20_window, image=photo) #Create a label to display the image
        img_label.image = photo #Keep a reference to avoid the image being garbage collected
        img_label.pack() #Pack the image label into the d20 window
    except FileNotFoundError: #Handle case where the image is not found
        tk.Label(d20_window, text="Image not found!", fg="red").pack() #Show an error message if the image is not found
    
    #Label for modifier input
    d20_modifier_label = tk.Label(d20_window, text="Enter a modifier in the range of -5 to +10:")
    d20_modifier_label.pack()

    #Function to roll a d20
    def d20():
        roll_d20 = random.randrange(1,21) #Roll number between 1 and 20
        modifier = int(d20_modifier_entry.get()) #Input modifier from what user enters
        if (modifier > 10) | (modifier < -5): #Checks that the modifier entered is within the range of -5 to +10
            d20_result_label.config(text=f"The value you entered is not in the range of -5 to +10.") #Update result label
        else:
            add_modifier = roll_d20 + modifier #Add the modifier to the roll
            if modifier >= 0: #Makes it so that + will be printed in front of the modifier for positive modifiers
                final_modifier = "+" + str(modifier)
            else:
                final_modifier = str(modifier)
            if add_modifier >= 19: #Displays different results depending on how high or low a user rolls
                d20_result_label.config(text=f"You rolled a {roll_d20} with a modifier of {final_modifier}.\nYou rolled high enough to deal some extra damage!") #Update result label
            elif (add_modifier < 19) & (add_modifier >= 13):
                d20_result_label.config(text=f"You rolled a {roll_d20} with a modifier of {final_modifier}.\nYou rolled high enough to deal damage!") #Update result label
            elif (add_modifier < 13) & (add_modifier >= 7):
                d20_result_label.config(text=f"You rolled a {roll_d20} with a modifier of {final_modifier}.\nYour roll was not very high, so your damage will be reduced.") #Update result label
            else:
                d20_result_label.config(text=f"You rolled a {roll_d20} with a modifier of {final_modifier}.\nYour roll was so low that your attack missed!") #Update result label

    #Entry widget to input modifier
    d20_modifier_entry = tk.Entry(d20_window)
    d20_modifier_entry.pack()
    
    #Button to roll d20
    roll_d20_button = tk.Button(d20_window, text="Roll", command=d20, bg="black", fg="white")
    roll_d20_button.pack()

    #Label to show result of roll
    d20_result_label = tk.Label(d20_window, text="", font=("Arial", 12, "bold", ))
    d20_result_label.pack()

    #Exit Button
    exit_button = tk.Button(d20_window, text="Exit", command=d20_window.destroy, bg='red') #Exit button to close the d20 window
    exit_button.pack(pady=5)

#Function to open the d12 window
def open_d12_window():
    d12_window = Toplevel(window) #Create a new window for d12 rolling
    d12_window.title("Rolling a d12") #Set the title of the d12 window
    d12_window.geometry("500x300") #Set the size of the d12 window
    d12_window.configure(bg='yellow') #Set the background color of the d12 window

    #Load and display a JPEG image
    try:
        img = Image.open("C:/Users/ajbec/OneDrive/Desktop/DnD Coding Project/DnDd12.jpg").resize((150,150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img) #Convert the image into a format suitable for tkinter
        img_label = tk.Label(d12_window, image=photo) #Create a label to display the image
        img_label.image = photo #Keep a reference to avoid the image being garbage collected
        img_label.pack() #Pack the image label into the d12 window
    except FileNotFoundError: #Handle case where the image is not found
        tk.Label(d12_window, text="Image not found!", fg="red").pack() #Show an error message if the image is not found

    #Label for modifier input
    d12_modifier_label = tk.Label(d12_window, text="Enter a modifier in the range of -5 to +10:")
    d12_modifier_label.pack()

    #Function to roll a d12
    def d12():
        roll_d12 = random.randrange(1,13) #Roll number between 1 and 12
        modifier = int(d12_modifier_entry.get()) #Input modifier from what user enters
        if (modifier > 10) | (modifier < -5): #Checks that the modifier entered is within the range of -5 to +10
            d12_result_label.config(text=f"The value you entered is not in the range of -5 to +10.") #Update result label
        else:
            d12_damage = roll_d12 + modifier #Add the modifier to the roll
            if modifier >= 0: #Makes it so that + will be printed in front of the modifier for positive modifiers
                final_modifier = "+" + str(modifier)
            else:
                final_modifier = str(modifier)
            d12_result_label.config(text=f"You rolled a {roll_d12} with a modifier of {final_modifier}.\nYou dealt {d12_damage} damage!") #Update result label

    #Entry widget to input modifier
    d12_modifier_entry = tk.Entry(d12_window)
    d12_modifier_entry.pack()
    
    #Button to roll d12
    roll_d12_button = tk.Button(d12_window, text="Roll", command=d12, bg="black", fg="white")
    roll_d12_button.pack()

    #Label to show result of roll
    d12_result_label = tk.Label(d12_window, text="", font=("Arial", 12, "bold", ))
    d12_result_label.pack()

    #Exit Button
    exit_button = tk.Button(d12_window, text="Exit", command=d12_window.destroy, bg='red') #Exit button to close the d12 window
    exit_button.pack(pady=5)

#Function to open the d10 window
def open_d10_window():
    d10_window = Toplevel(window) #Create a new window for d10 rolling
    d10_window.title("Rolling a d10") #Set the title of the d10 window
    d10_window.geometry("500x300") #Set the size of the d10 window
    d10_window.configure(bg='green') #Set the background color of the d10 window

    #Load and display a JPEG image
    try:
        img = Image.open("C:/Users/ajbec/OneDrive/Desktop/DnD Coding Project/DnDd10.jpg").resize((150,150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img) #Convert the image into a format suitable for tkinter
        img_label = tk.Label(d10_window, image=photo) #Create a label to display the image
        img_label.image = photo #Keep a reference to avoid the image being garbage collected
        img_label.pack() #Pack the image label into the d10 window
    except FileNotFoundError: #Handle case where the image is not found
        tk.Label(d10_window, text="Image not found!", fg="red").pack() #Show an error message if the image is not found

    #Label for modifier input
    d10_modifier_label = tk.Label(d10_window, text="Enter a modifier in the range of -5 to +10:")
    d10_modifier_label.pack()

    #Function to roll a d10
    def d10():
        roll_d10 = random.randrange(1,11) #Roll number between 1 and 10
        modifier = int(d10_modifier_entry.get()) #Input modifier from what user enters
        if (modifier > 10) | (modifier < -5): #Checks that the modifier entered is within the range of -5 to +10
            d10_result_label.config(text=f"The value you entered is not in the range of -5 to +10.") #Update result label
        else:
            d10_damage = roll_d10 + modifier #Add the modifier to the roll
            if modifier >= 0: #Makes it so that + will be printed in front of the modifier for positive modifiers
                final_modifier = "+" + str(modifier)
            else:
                final_modifier = str(modifier)
            d10_result_label.config(text=f"You rolled a {roll_d10} with a modifier of {final_modifier}.\nYou dealt {d10_damage} damage!") #Update result label

    #Entry widget to input modifier
    d10_modifier_entry = tk.Entry(d10_window)
    d10_modifier_entry.pack()

    #Button to roll d10
    roll_d10_button = tk.Button(d10_window, text="Roll", command=d10, bg="black", fg="white")
    roll_d10_button.pack()

    #Label to show result of roll
    d10_result_label = tk.Label(d10_window, text="", font=("Arial", 12, "bold", ))
    d10_result_label.pack()

    #Exit Button
    exit_button = tk.Button(d10_window, text="Exit", command=d10_window.destroy, bg='red') #Exit button to close the d10 window
    exit_button.pack(pady=5)

#Function to open the d8 window
def open_d8_window():
    d8_window = Toplevel(window) #Create a new window for d8 rolling
    d8_window.title("Rolling a d8") #Set the title of the d8 window
    d8_window.geometry("500x300") #Set the size of the d8 window
    d8_window.configure(bg='purple') #Set the background color of the d8 window

    #Load and display a JPEG image
    try:
        img = Image.open("C:/Users/ajbec/OneDrive/Desktop/DnD Coding Project/DnDd8.jpg").resize((150,150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img) #Convert the image into a format suitable for tkinter
        img_label = tk.Label(d8_window, image=photo) #Create a label to display the image
        img_label.image = photo #Keep a reference to avoid the image being garbage collected
        img_label.pack() #Pack the image label into the d8 window
    except FileNotFoundError: #Handle case where the image is not found
        tk.Label(d8_window, text="Image not found!", fg="red").pack() #Show an error message if the image is not found

    #Label for modifier input
    d8_modifier_label = tk.Label(d8_window, text="Enter a modifier in the range of -5 to +10:")
    d8_modifier_label.pack()

    #Function to roll a d8
    def d8():
        roll_d8 = random.randrange(1,9) #Roll number between 1 and 8
        modifier = int(d8_modifier_entry.get()) #Input modifier from what user enters
        if (modifier > 10) | (modifier < -5): #Checks that the modifier entered is within the range of -5 to +10
            d8_result_label.config(text=f"The value you entered is not in the range of -5 to +10.") #Update result label
        else:
            d8_damage = roll_d8 + modifier #Add the modifier to the roll
            if modifier >= 0: #Makes it so that + will be printed in front of the modifier for positive modifiers
                final_modifier = "+" + str(modifier)
            else:
                final_modifier = str(modifier)
            d8_result_label.config(text=f"You rolled a {roll_d8} with a modifier of {final_modifier}.\nYou dealt {d8_damage} damage!") #Update result label

    #Entry widget to input modifier
    d8_modifier_entry = tk.Entry(d8_window)
    d8_modifier_entry.pack()

    #Button to roll d8
    roll_d8_button = tk.Button(d8_window, text="Roll", command=d8, bg="black", fg="white")
    roll_d8_button.pack()

    #Label to show result of roll
    d8_result_label = tk.Label(d8_window, text="", font=("Arial", 12, "bold", ))
    d8_result_label.pack()

    #Exit Button
    exit_button = tk.Button(d8_window, text="Exit", command=d8_window.destroy, bg='red') #Exit button to close the d8 window
    exit_button.pack(pady=5)

#Function to open the d6 window
def open_d6_window():
    d6_window = Toplevel(window) #Create a new window for d6 rolling
    d6_window.title("Rolling a d6") #Set the title of the d6 window
    d6_window.geometry("500x300") #Set the size of the d6 window
    d6_window.configure(bg='orange') #Set the background color of the d6 window

    #Load and display a JPEG image
    try:
        img = Image.open("C:/Users/ajbec/OneDrive/Desktop/DnD Coding Project/DnDd6.jpg").resize((150,150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img) #Convert the image into a format suitable for tkinter
        img_label = tk.Label(d6_window, image=photo) #Create a label to display the image
        img_label.image = photo #Keep a reference to avoid the image being garbage collected
        img_label.pack() #Pack the image label into the d6 window
    except FileNotFoundError: #Handle case where the image is not found
        tk.Label(d6_window, text="Image not found!", fg="red").pack() #Show an error message if the image is not found

    #Label for modifier input
    d6_modifier_label = tk.Label(d6_window, text="Enter a modifier in the range of -5 to +10:")
    d6_modifier_label.pack()

    #Function to roll a d6
    def d6():
        roll_d6 = random.randrange(1,7) #Roll number between 1 and 6
        modifier = int(d6_modifier_entry.get()) #Input modifier from what user enters
        if (modifier > 10) | (modifier < -5): #Checks that the modifier entered is within the range of -5 to +10
            d6_result_label.config(text=f"The value you entered is not in the range of -5 to +10.") #Update result label
        else:
            d6_damage = roll_d6 + modifier #Add the modifier to the roll
            if modifier >= 0: #Makes it so that + will be printed in front of the modifier for positive modifiers
                final_modifier = "+" + str(modifier)
            else:
                final_modifier = str(modifier)
            d6_result_label.config(text=f"You rolled a {roll_d6} with a modifier of {final_modifier}.\nYou dealt {d6_damage} damage!") #Update result label

    #Entry widget to input modifier
    d6_modifier_entry = tk.Entry(d6_window)
    d6_modifier_entry.pack()

    #Button to roll d6
    roll_d6_button = tk.Button(d6_window, text="Roll", command=d6, bg="black", fg="white")
    roll_d6_button.pack()

    #Label to show result of roll
    d6_result_label = tk.Label(d6_window, text="", font=("Arial", 12, "bold", ))
    d6_result_label.pack()

    #Exit Button
    exit_button = tk.Button(d6_window, text="Exit", command=d6_window.destroy, bg='red') #Exit button to close the d6 window
    exit_button.pack(pady=5)

#Function to open the d4 window
def open_d4_window():
    d4_window = Toplevel(window) #Create a new window for d4 rolling
    d4_window.title("Rolling a d4") #Set the title of the d4 window
    d4_window.geometry("500x300") #Set the size of the d4 window
    d4_window.configure(bg='blue') #Set the background color of the d4 window

    #Load and display a JPEG image
    try:
        img = Image.open("C:/Users/ajbec/OneDrive/Desktop/DnD Coding Project/DnDd4.jpg").resize((150,150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img) #Convert the image into a format suitable for tkinter
        img_label = tk.Label(d4_window, image=photo) #Create a label to display the image
        img_label.image = photo #Keep a reference to avoid the image being garbage collected
        img_label.pack() #Pack the image label into the d4 window
    except FileNotFoundError: #Handle case where the image is not found
        tk.Label(d4_window, text="Image not found!", fg="red").pack() #Show an error message if the image is not found

    #Label for modifier input
    d4_modifier_label = tk.Label(d4_window, text="Enter a modifier in the range of -5 to +10:")
    d4_modifier_label.pack()

    #Function to roll a d4
    def d4():
        roll_d4 = random.randrange(1,5) #Roll number between 1 and 4
        modifier = int(d4_modifier_entry.get()) #Input modifier from what user enters
        if (modifier > 10) | (modifier < -5): #Checks that the modifier entered is within the range of -5 to +10
            d4_result_label.config(text=f"The value you entered is not in the range of -5 to +10.") #Update result label
        else:
            d4_damage = roll_d4 + modifier #Add the modifier to the roll
            if modifier >= 0: #Makes it so that + will be printed in front of the modifier for positive modifiers
                final_modifier = "+" + str(modifier)
            else:
                final_modifier = str(modifier)
            d4_result_label.config(text=f"You rolled a {roll_d4} with a modifier of {final_modifier}.\nYou dealt {d4_damage} damage!") #Update result label

    #Entry widget to input modifier
    d4_modifier_entry = tk.Entry(d4_window)
    d4_modifier_entry.pack()

    #Button to roll d4
    roll_d4_button = tk.Button(d4_window, text="Roll", command=d4, bg="black", fg="white")
    roll_d4_button.pack()

    #Label to show result of roll
    d4_result_label = tk.Label(d4_window, text="", font=("Arial", 12, "bold", ))
    d4_result_label.pack()

    #Exit Button
    exit_button = tk.Button(d4_window, text="Exit", command=d4_window.destroy, bg='red') #Exit button to close the d4 window
    exit_button.pack(pady=5)

#Create the main window
window = tk.Tk() #Create the main window
window.title("Dungeons and Dragons Dice Roller for Combat") #Title
window.geometry("500x650") #Set the size of the main window
window.configure(bg='red') #Set the background color of the main window

#Load and display a JPEG image
try:
    img = Image.open("C:/Users/ajbec/OneDrive/Desktop/DnD Coding Project/DnDHomePage.jpg").resize((300,300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img) #Convert the image into a format suitable for tkinter
    img_label = tk.Label(window, image=photo) #Create a label to display the image
    img_label.image = photo #Keep a reference to avoid the image being garbage collected
    img_label.pack() #Pack the image label into the main window
except FileNotFoundError: #Handle case where the image is not found
    tk.Label(window, text="Image not found!", fg="red").pack() #Show an error message if the image is not found

#Instructions
instruction_label = tk.Label(window, text="This program allows you to simulate rolling dice for combat in DnD.\nThe d20 is used to determine if your attack hits.\nThe other dice determine the amount of damage you deal.\nUse the buttons below to select the die you would like to roll:") #Label for distance input
instruction_label.pack()

#Button to go to d20 window
d20_button = tk.Button(window, text="Roll a d20", command=open_d20_window, bg="lightblue")
d20_button.pack(pady=10)

#Button to go to d12 window
d12_button = tk.Button(window, text="Roll a d12", command=open_d12_window, bg="yellow")
d12_button.pack(pady=10)

#Button to go to d10 window
d10_button = tk.Button(window, text="Roll a d10", command=open_d10_window, bg="green", fg="white")
d10_button.pack(pady=10)

#Button to go to d8 window
d8_button = tk.Button(window, text="Roll a d8", command=open_d8_window, bg="purple", fg="white")
d8_button.pack(pady=10)

#Button to go to d6 window
d6_button = tk.Button(window, text="Roll a d6", command=open_d6_window, bg="orange")
d6_button.pack(pady=10)

#Button to go to d4 window
d4_button = tk.Button(window, text="Roll a d4", command=open_d4_window, bg="blue")
d4_button.pack(pady=10)

#Run the application
window.mainloop() #Start the tkinter event loop to display the window and wait for user interactions
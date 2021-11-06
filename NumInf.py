
"""

import tkinter as tk
from tkinter import simpledialog

application_window = tk.Tk()

answer = simpledialog.askstring("Input", "What is your first name?",
                                parent=application_window)
if answer is not None:
	messagebox.showinfo("Information","Your first name is "+ answer)
else:
    print("You don't have a first name?")

"""

import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import phonemetadata

n = (input("Introduce the phone number you want to analize: \n"))
#n = "+34646556456"

phoneNumber = phonenumbers.parse(n)

print("The phone number is " + n)
print(geocoder.description_for_number(phoneNumber,'es'))
print(carrier.name_for_number(phoneNumber,'es'))
print(phonemetadata.NumberFormat(phoneNumber,'es'))
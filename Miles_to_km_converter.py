from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=30,pady=30)

def miles_to_km_conversion():
    '''Converts a users input from miles to Km'''
    miles = float(user_input.get())
    km = round(miles * 1.609, 1)
    output_label.config(text=km)
    

user_input = Entry(width=7)
user_input.insert(END, string="0")
user_input.grid(column=2,row=1)


miles_label = Label(text="Miles")
miles_label.grid(column=3,row=1)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=1,row=2)

output_label = Label(text="0")
output_label.grid(column=2,row=2)

km_label = Label(text="Km")
km_label.grid(column=3,row=2)

calculate_button = Button(text="Calculate", command=miles_to_km_conversion)
calculate_button.grid(column=2,row=3)

window.mainloop()

import tkinter as tk
from tkinter import Entry

from currency_converter import CurrencyConverter




root= tk.Tk()
root.geometry("700x500")
root.maxsize(700,500)
root.title("Currency Converter")

c=CurrencyConverter()
def convert():
    try:

        amount = float(entry1.get())
        curr1 = entry2.get()
        curr2 = entry3.get()


        result_value = c.convert(amount, curr1, curr2)


        result.config(text=f"Result: {result_value:f} ")

    except Exception as e:
        result.config(text="Error in conversion. Please check the inputs.")


#create a label
label=tk.Label(root, text= "Currency Convertor" , font="Times 19 bold ",bg="grey" )
label.place(x=200,y=30)

label1=tk.Label(root,text="Enter your Amount :",font="Comicsansms 13 bold ")
label1.place(x=110,y=120)
entry1=tk.Entry(root)
entry1.place(x=340,y=125)



label2=tk.Label(root,text="From Currency :",font="Comicsansms 13 bold ")
label2.place(x=110,y=180)
entry2=tk.StringVar(root)
entry2.set("USD")
currency_from=tk.OptionMenu(root,entry2,"USD","EUR","GBP","JPY","INR")
currency_from.place(x=340,y=175)



label3=tk.Label(root,text="To Currency :",font="Comicsansms 13 bold ")
label3.place(x=110,y=240)
entry3=tk.StringVar(root)
entry3.set("INR")
currency_to=tk.OptionMenu(root,entry3,"INR","USD","EUR","GBP","JPY")
currency_to.place(x=340,y=240)

#create a button
button=tk.Button(root,text="Convert",font="Comicsansms 13 bold ",command=convert)
button.place(x=220,y=320)

result=tk.Label(root,text="Result :",font="Comicsansms 13 bold ")
result.place(x=300,y=400)

root.mainloop()


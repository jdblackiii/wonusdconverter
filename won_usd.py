import tkinter as tk
#from tkinter import ttk #boo ugly
from forex_python.converter import CurrencyRates
import ttkbootstrap as ttk

class converter:
    window = None
    usd_to_krw = True
    title_text = None
    output_var = None
    
    won = None
    usd = None
    
    curr_rates = CurrencyRates()
    rate_won_to_usd = curr_rates.get_rate(base_cur= 'KRW', dest_cur= 'USD')
    rate_usd_to_won = curr_rates.get_rate(base_cur= 'USD', dest_cur= 'KRW')
    
    def convert_currency(self, inp):
        c = CurrencyRates()

        if self.usd_to_krw:
            self.usd = inp
            self.krw = self.rate_usd_to_won * inp
            self.output_var.set(f'${self.usd:,.2f} is ₩{self.krw:,.2f}')
        else:
            self.krw = inp
            self.usd = self.rate_won_to_usd * inp
            self.output_var.set(f'₩{self.krw:,.2f} is ${self.usd:,.2f}')
        
        
    def switch_conversion(self):
        self.usd_to_krw = not self.usd_to_krw
        
        if self.usd_to_krw:
            self.title_text.set('USD ➡️ KRW')
            self.convert_currency(self.usd)
        else:
            self.title_text.set('KRW ➡️ USD')
            self.convert_currency(self.krw)
        
    def execute(self):
        self.window.mainloop()
    
    def __init__(self):
        #title
        self.window = ttk.Window(themename= 'flatly')
        self.window.title('₩ / $')
        self.window.geometry('400x150')

        #title
        self.title_text = ttk.StringVar()
        self.title_text.set('USD ➡️ KRW')
        title_label = ttk.Label(
            master= self.window, 
            textvariable= self.title_text, 
            font= 'Calibri 24 bold').pack()
        usd_to_krw = True

        #input field
        input_frame = ttk.Frame(master= self.window)
        entry_val = tk.DoubleVar()
        entry = ttk.Entry(master= input_frame, textvariable= entry_val)
        convert_button = ttk.Button(
            master= input_frame, 
            text= 'Convert', 
            command= lambda: self.convert_currency(float(entry_val.get())))
        switch_button = ttk.Button(
            master= input_frame, 
            text= '🔄', 
            command= lambda: self.switch_conversion())

        entry.pack(side= 'left', padx= 3)
        convert_button.pack(side= 'left', padx= 3)
        switch_button.pack(side= 'right', padx= 3)
        input_frame.pack(pady= 10)

        #output
        self.output_var = ttk.StringVar()
        output_label = ttk.Label(
            master= self.window,
            font= 'Calibri 18 bold', 
            textvariable= self.output_var)
        output_label.pack(pady= 10)

def main():
    converter_obj = converter()
    converter_obj.execute()
    
if __name__ == '__main__':
    main()
               
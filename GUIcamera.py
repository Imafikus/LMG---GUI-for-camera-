
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Button, Style
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import *

from PIL import ImageTk, Image


                                                                        

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()

        
    def initUI(self):
      
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=True, pady=5)
	
        frames = []
        
        
        frame0 = Frame(self)
        frame0.pack(fill=X, padx=15)
        
        labelDay1 = Label(frame0, text = "Date 1").grid(row=0, column=0, padx=10)        

        varDay1 = StringVar(frame0)
        varDay1.set("1")
        optionDay1 = OptionMenu(frame0, varDay1, "1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.", "11.", "12.", "13.", "14.", "15.", "16.", "17.", "18.", "19.", "20.", "21.", "22.", "23.", "24.", "25.","26.", "27.", "28.", "29.", "30.", "31.")
        optionDay1.grid(row=0, column=1)
        

        varMonth1 = StringVar(frame0)
        varMonth1.set("1.")
        optionMonth1 = OptionMenu(frame0, varMonth1, "1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.", "11.", "12.")
        optionMonth1.grid(row=0, column=2)

        
        varYear1 = StringVar(frame0)
        varYear1.set("2010.")
        optionYear1 = OptionMenu(frame0, varYear1, "2010.","2011.","2012.","2013.","2014.","2015.","2016.","2017.","2018.","2019.","2020.",
"2021.","2022.","2023.","2024.","2025.","2026.","2027.","2028.","2029.","2030.")      
        optionYear1.grid(row=0, column=3)

        lblSpace = Label(frame0, text="").grid(row=0, column=3, padx=25) 
        lblDate2 = Label(frame0, text="Date 2").grid(row=0, column=4, padx=15) 
        varDay2 = StringVar(frame0)
        varDay2.set("1")
        optionDay2 = OptionMenu(frame0, varDay2, "1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.", "11.", "12.", "13.", "14.", "15.", "16.", "17.", "18.", "19.", "20.", "21.", "22.", "23.", "24.", "25.","26.", "27.", "28.", "29.", "30.", "31.")
        optionDay2.grid(row=0, column=5)
        

        varMonth2 = StringVar(frame0)
        varMonth2.set("1.")
        optionMonth2 = OptionMenu(frame0, varMonth2, "1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.", "11.", "12.")
        optionMonth2.grid(row=0, column=6)

        
        varYear2 = StringVar(frame0)
        varYear2.set("2010.")
        optionYear2 = OptionMenu(frame0, varYear2, "2010.","2011.","2012.","2013.","2014.","2015.","2016.","2017.","2018.","2019.","2020.",
"2021.","2022.","2023.","2024.","2025.","2026.","2027.","2028.","2029.","2030.")      
        optionYear2.grid(row=0, column=7)
              
        settings = Button(frame0, text="Settings", command=self.create_window)
        settings.grid(row=0, column=8, padx=50)
        
	

        frame2 = Frame(self)
        frame2.pack(fill=X)
        calculate = Button(frame2, text = "Calculate")
        calculate.pack(pady = 30)
        calculate.config(height=15, width = 30)
        

        
    def create_window(self):
        newWindow = Toplevel(self)

        

        newWindow.title("Settings")
        lblCVP = Label(newWindow, text="CVP").grid(row=0, column=0, padx=5)
        entryCVP1 = Entry(newWindow, width=10).grid(row=0, column=1, padx=5)
        entryCVP2 = Entry(newWindow, width=10).grid(row=0, column=2, padx=5)

        lblFOV = Label(newWindow, text="FOV").grid(row=1, column=0, padx=5, pady=5)
        entryFOV1 = Entry(newWindow, width=10).grid(row=1, column=1, padx=5, pady=5)
        entryFOV2 = Entry(newWindow, width=10).grid(row=1, column=2, padx=5, pady=5)
        newWindow.geometry("400x400+200+200")

        """browse = Button(newWindow, text = "Browse...")
	browse.grid =
        newWindow.geometry("250x200+200+200")
	"""
                
        	      

        
        


def main():
  
    root = Tk()
    root.geometry("700x150+300+50")
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()  

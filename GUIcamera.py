
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Button, Style
from tkinter import messagebox
from tkinter import Toplevel

from PIL import ImageTk, Image


                                                                        

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()

        
    def initUI(self):
      
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=True, pady=5)
	
        frames = []
                
        frame1 = Frame(self)
        frame1.pack(fill=X)
            
        lbl_date1 = Label(frame1, text="Start").grid(row=0, column=0)
        date1 = Entry(frame1)
        date1.grid(row=0, column=1)

        lbl_date2 = Label(frame1, text="End").grid(row=0, column=2)
        date2 = Entry(frame1)
        date2.grid(row=0, column=3)

        settings = Button(frame1, text="Settings")
        settings.grid(row=0, column=4)
        

        
        


def main():
  
    root = Tk()
    root.geometry("500x200+300+50")
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()  

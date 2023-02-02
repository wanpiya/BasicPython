#GUI mouse
from tkinter import* # lip:tk interface
from tkinter import ttk
import webbrowser
import pyautogui as pg

GUI = Tk()
GUI.title('โปรแกรมสั่งกดปฎิทิน')
GUI.geometry('300x400')

def calender():
    pg.click(1838,1067)


B1 = Button(GUI,text='Calender1',command=calender)
B1.pack(ipadx=20, ipady=10, pady=10)

B2 = ttk.Button(GUI,text='Calender2',command=calender)
B2.pack(ipadx=20, ipady=10, pady=10)

def Google():
    webbrowser.open('https://www.google.co.th')


B3 = ttk.Button(GUI,text='Google',command=Google)
B3.pack(ipadx=20, ipady=10, pady=10)


def Youtube():
    webbrowser.open('https://www.youtube.com')

B3 = Button(GUI,text='Youtube',command=Youtube)
B3.pack(ipadx=20, ipady=10)

GUI.mainloop()

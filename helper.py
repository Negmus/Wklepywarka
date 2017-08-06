from tkinter import *
import pyautogui
from pymouse import PyMouseEvent
import sys


class DetectMouseClick(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)
    def click(self, x, y, button, press):
        if button == 1:
            if press:
                print("click")
            else:
                pyautogui.typewrite(gnumer)
                pyautogui.press("tab")
                pyautogui.typewrite(gopis)
                sys.exit("Koniec")
        else:
            sys.exit("Koniec")


def wpisz():
    nr= str(Entry.get(n1))
    ntest=nr[0:1]
    global gnumer
    global gopis
    if ntest == "5":
        numer="8"+nr[1:3]
        print (numer)
        lnr = len(nr)
        opis = (nr[4:lnr - 1])
        gnumer = numer
        gopis = opis
        O = DetectMouseClick()
        O.run()
    else:
        numer=(nr[0:3])
        lnr = len(nr)
        opis=(nr[4:lnr-1])
        gnumer = numer
        gopis = opis
        O = DetectMouseClick()
        O.run()

root = Tk()
x= Entry(root)
Label(root, text="Dane:").grid(row=0, column=0)
n1= Entry(root)
n1.grid(row=0, column=2)
Button(root, text="Wpisuj", command=wpisz).grid(row=0, column=4)
root.mainloop()

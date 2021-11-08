import tkinter as tk
from tkinter import *

blacklist = ['debil', 'retard', 'idiota']

root = Tk()
root.geometry("400x350")
root.resizable(FALSE,FALSE)
root.title(" Nadajnik  ")

l = Label(root, text=" Wpisz tekst wiadomosci ")

inputtxt = Text(root, height=5,
                width=40,
                bg="light yellow")

l2 = Label(root, text=" Wiadomosc ASCII ")

Output = Text(root, height=5,
              width=40,
              bg="light cyan")

b1 = Button(root, height=2,
                 width=20,
                 text="Konwertuj",
                 command=lambda: Take_input())

b2 = Button(root, height = 2,
                width=20,
                text="Wyczysc",
                command = lambda: inputtxt.delete(1.0,END))

b3 = Button(root, height = 2,
                width=20,
                text="Przeslij do odbiornika",
                command = lambda: Take_output())

l.pack()
b3.pack(side = BOTTOM)
Output.pack(side = BOTTOM)
l2.pack(side = BOTTOM)
inputtxt.pack()
b1.pack()
b2.pack()

def Take_input():
    INPUT = inputtxt.get("1.0", "end")
    Output.insert(END, toBinary(INPUT))

def Take_output():
    window1 = tk.Toplevel(root)
    window1.geometry("400x300")
    window1.resizable(FALSE, FALSE)
    window1.title("Odbiornik")

    l1 = Label(window1, text=" Zakodowana wiadomosc : ")
    l1.pack()

    odbior = Text(window1, height=5,
                  width=40,
                  bg="light cyan")
    odbior.pack()

    odbiorc = inputtxt.get("1.0", "end")
    cenzura = censor(odbiorc, blacklist)
    odbior.insert(END, cenzura)

def censor(t,l):
    words = t.split()
    for i in range(len(words)):
        if words[i] in l:
            words[i] = "*"*len(words[i])
    a = " ".join(words)
    return a

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(bin(2)[2:])
    m.append(int(bin(i)[2:]))
    m.append(bin(3)[2:])
    m.append(bin(3)[2:])
  return m

mainloop()
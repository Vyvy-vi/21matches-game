from tkinter import *
from tkinter import messagebox
wind= Tk()
wind.title('21 Matches')
ls=['|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|']
def press(inp):
    user_edit(inp)
    messagebox.showinfo('User Choice',f'You chose to pick up {inp} matches.')
    if inp==2:
        out=1
    else:
        out=2
    mac_edit(out)
def mac_edit(o):
    global ls
    global play
    ls = ls[:len(ls)-o]
    if ls==[]:
        messagebox.showwarning('HAHAH','I win.')
        ls=['|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|']
        playui()
    else:
        play.grid_forget()
        play= Label(wind, text= ' '.join(ls))
        play.grid(row=0, column=0, columnspan=2)
        messagebox.showinfo('My Choice',f'I picked up {o} matches.')


def user_edit(i):
    global ls
    global play
    ls = ls[:len(ls)-i]
    play.grid_forget()
    play= Label(wind, text= ' '.join(map(str,ls)))
    play.grid(row=0, column=0, columnspan=2)

def playui():
    global play
    play.grid_forget()
    play= Label(wind, text= ' '.join(map(str,ls)))
    play.grid(row=0, column=0, columnspan=2)
    but1= Button(wind, text='1', command = lambda: press(1))
    but1.grid(row=1, column=0)
    but2= Button(wind, text='2',command = lambda: press(2))
    but2.grid(row=1, column=1)

play= Button(wind, text="Click to play:", command= playui)
play.grid(row=0, column=0)
wind.mainloop()

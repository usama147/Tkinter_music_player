from tkinter import *
import pygame
import os
import tkinter.font as font

window = Tk()
window.geometry("570x300")

pygame.mixer.init()

n = 0


# -----------------------------------------------------------------------------------------------

def start_stop():
    global n
    n = n + 1

    if n == 1:
        song_name = songs_listbox.get()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(0)
        print("music started ")


def stop():
    pygame.mixer.music.pause()


def quit():
    window.destroy()


myFont = font.Font(family='Robotto')

myFont1 = font.Font(family='Robotto', size=20)
# -----------------------------------------------------------------------------------------------

l1 = Label(window, text="Music Player", font=myFont1)
l1.grid(row=1, column=1)

# -----------------------------------------------------------------------------------------------

b2 = Button(window, text='Play', width=20, command=start_stop, bg='lightgreen', font=myFont)
b2.grid(row=4, column=1)
b3 = Button(window, text='Pause', width=20, command=stop, bg='lightblue', font=myFont)
b3.grid(row=5, column=1)
b4 = Button(window, text='Exit', width=20, command=quit, bg='salmon', font=myFont)
b4.grid(row=6, column=1)
songs_list = os.listdir()
songs_listbox = StringVar(window)
songs_listbox.set("select song")
menu = OptionMenu(window, songs_listbox, *songs_list)
menu.grid(row=4, column=4)

window.mainloop()

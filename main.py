from tkinter import *
import tkinter.ttk as ttk
import random
import time
from tkinter import messagebox

# DEVELOPER:
# KONSTANTIN EHMANN

root = Tk()
root.resizable(False, False)
root.title("Python Spielautomat")

Developers = "Konstantin Ehmann"
always_big_win = False
start_money = 14
rounds_played = 0

def Advert():
    advert_frame = Frame(root, bg="grey", width=400, height=17)
    advert_frame.pack(side=BOTTOM)

    devs = Label(advert_frame, text="Developed by " + Developers, bg="grey")
    devs.place(x=200, y=-2)

def Settingframe():
    global always_big_win_button, always_big_win
    settings = Tk()
    settings.title("Settings & Info")
    settings.geometry("400x300")
    settings.resizable(False, False)

    always_big_win_button = Button(settings, text="Always <Big win>", command=alw_b_w)
    always_big_win_button.place(x=10,y=10)
    if always_big_win == False:
        always_big_win_button.config(bg="orange red")
    else:
        always_big_win_button.config(bg="lightgreen")

def alw_b_w():
    global always_big_win
    if always_big_win == False:
        always_big_win = True
        always_big_win_button.config(bg="lightgreen")
    else:
        always_big_win = False
        always_big_win_button.config(bg="orange red")


def Gameframe():
    global c1, c2, c3, spin1, spin2, spin3, game_frame, money_label
    game_frame = Frame(root, width=400, height=250, bg="white")
    game_frame.pack(side=TOP)

    settings_button = ttk.Button(game_frame, text="Settings", command=Settingframe)
    settings_button.place(x=320, y=0)

    money_label = Label(game_frame, text="Money: " + str(start_money) + "$", fg="gold4", font=("Arial", 16), bg="white")
    money_label.place(x=0, y=0)

    spin1 = Canvas(game_frame, width=80, height=80, bd=3, relief=SUNKEN, bg="lightgrey")
    spin2 = Canvas(game_frame, width=80, height=80, bd=3, relief=SUNKEN, bg="lightgrey")
    spin3 = Canvas(game_frame, width=80, height=80, bd=3, relief=SUNKEN, bg="lightgrey")

    spin1.place(x=70, y=80)
    spin2.place(x=150, y=80)
    spin3.place(x=230, y=80)

    c1 = spin1.create_oval(75, 75, 10, 10)
    c2 = spin2.create_oval(75, 75, 10, 10)
    c3 = spin3.create_oval(75, 75, 10, 10)



def Startframe():
    global starting_button
    global win_label
    global round_label
    start_frame = Frame(root, bg="lightgrey", width=400, height=25)
    start_frame.pack(side=BOTTOM)

    round_label = Label(start_frame, text="Rounds played: " + str(rounds_played), bg="lightgrey", fg="green", font=("Arial", 12))
    round_label.place(x=220, y=2)
    starting_button = ttk.Button(start_frame, text="Start", command=Roll)
    starting_button.place(x=0, y=0)
    win_label = Label(start_frame, text="Press Start to play", bg="lightgrey", font=("Arial", 12))
    win_label.place(x=75, y=2)

def small_win():
    global start_money
    win_label.config(text="SMALL WIN! +2$")
    start_money += 2
    money_label.config(text="Money: " + str(start_money) + "$")

def big_win():
    global start_money
    win_label.config(text="BIG WIN! +10$", fg="gold4")
    game_frame.config(bg="gold2")
    start_money += 10
    money_label.config(text="Money: " + str(start_money) + "$")

def loose():
    win_label.config(text="You lost")

def Roll():
    global counter, start_money, rounds_played
    if start_money > 1:
        start_money -= 2
        rounds_played += 1
        money_label.config(text="Money: " + str(start_money) + "$")
        round_label.config(text="Rounds played: " + str(rounds_played))
        win_label.config(text="", fg="black")
        game_frame.config(bg="white")
        starting_button.config(text="Restart")
        spin1.itemconfig(c1, fill="red")
        counter = 0
        Animation()
        starting_button.config(state=DISABLED)

    else:
        messagebox.showerror("The End", "You dont have any money left! :(\nYou played " + str(rounds_played) + " Rounds")


def Animation():
    global counter, s1, s2, s3
    color_list = ["red", "green", "blue", "yellow", "orange"]
    if counter < 15:
        print(counter)
        s1 = random.choice(color_list)
        s2 = random.choice(color_list)
        s3 = random.choice(color_list)

        if always_big_win == True and counter == 14:
            s1 = "green"
            s2 = "green"
            s3 = "green"

        spin1.itemconfig(c1, fill=s1)
        spin2.itemconfig(c2, fill=s2)
        spin3.itemconfig(c3, fill=s3)
        counter += 1
        root.after(100, Animation)

    elif s1 == s2 and s1 == s3 and s2 == s3:
        big_win()
        starting_button.config(state=ACTIVE)
    elif s1 == s2 or s2 == s3 or s1 == s3:
        small_win()
        starting_button.config(state=ACTIVE)
    else:
        loose()
        starting_button.config(state=ACTIVE)
Advert()
Startframe()
Gameframe()


root.mainloop()
# PROGRAMMED BY KONSTANTIN EHMANN
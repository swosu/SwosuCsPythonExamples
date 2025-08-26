from tkinter import *
import time
import random

winner      = False
white_cat_x = 0
white_cat_y = 20

black_cat_x = -28
black_cat_y = 90

def start_game():
    global black_cat_x
    global white_cat_x
    global winner

    while winner == False:
        time.sleep(0.05)
        random_move_black_cat = random.randint(0,20)
        random_move_white_cat = random.randint(0,20)
        black_cat_x += random_move_black_cat
        white_cat_x += random_move_white_cat

        move_cats(random_move_white_cat,random_move_black_cat)
        main_screen.update()
        winner = check_winner()

    if winner == "Tie":
        Label(main_screen,text=winner,font=('calibri',20),fg="green",bg='white').place(x=200,y=450)
    else:
        Label(main_screen,text=winner+" Wins !!",font=('calibri',20),fg="green",bg='white').place(x=200,y=450)

def move_cats(white_cat_random_move,black_cat_random_move):
    canvas.move(white_cat,white_cat_random_move,0)
    canvas.move(black_cat,black_cat_random_move,0)

def check_winner():
    if black_cat_x >= 550 and white_cat_x >= 550:
        return "Tie"
    if black_cat_x >= 550:
        return "Black Cat"
    if white_cat_x >= 550:
        return "White Cat"
    return False

main_screen = Tk()
main_screen.title('Cat Racing')
main_screen.geometry('600x500')
main_screen.config(background='white')

canvas = Canvas(main_screen,width=600,height=200,bg="white")
canvas.pack(pady=20)

white_cat_img = PhotoImage(file="./images/white_cat.png")
black_cat_img = PhotoImage(file="./images/black_cat.png")

white_cat_img = white_cat_img.zoom(5)
white_cat_img = white_cat_img.subsample(65)
black_cat_img = black_cat_img.zoom(13)
black_cat_img = black_cat_img.subsample(90)

white_cat = canvas.create_image(white_cat_x,white_cat_y,anchor=NW,image=white_cat_img)
black_cat = canvas.create_image(black_cat_x,black_cat_y,anchor=NW,image=black_cat_img)

l1 = Label(main_screen,text='Select your cat', font=('calibri',20),bg="white")
l1.place(x=230,y=280)
l2 = Label(main_screen,text='Click play when ready!',font=('calibri',20),bg='white')
l2.place(x=200,y=330)

b1 = Button(main_screen,text='Play!',height=2,width=15,font=('calibri',10),bg='white',command=start_game)
b1.place(x=250,y=390)



main_screen.mainloop()


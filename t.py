import turtle
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from tkinter import *


def draw_field():
    window = turtle.getscreen()
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(-1)
    t.up()
    t.goto(-338, 300)
    style = ('Courier', 30, 'italic')
    t.write('Игра Крестики Нолики', font=style)
    t.goto(0, 0)
    t.down()
    turtle.bgcolor('purple')
    turtle.title('Крестики нолики')
    t.pensize(10)
    for i in range(4):
        t.forward(300)
        t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(300)
    t.left(90)
    for i in range(2):
        t.forward(100)
        t.left(90)
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(300)
    return window


root = Tk()
root.withdraw()
username = askstring(title='Игра крестики нолики',
                     prompt='Вбейте имя игрока 1')
username2 = askstring(title='Игра крестики нолики',
                      prompt='Вбейте имя игрока 2')

krestwin = 0
krugwin = 0
t = draw_field()
t_once = turtle.Turtle()
t_once.hideturtle()
t_once.speed(-1)
t_once.up()
style = ('Courier', 50, 'bold')
t_once.goto(-148, -207)
t_once.write(f'{username} {krestwin}:{krugwin} {username2}', font=style)
t_once.down()
b = 0
win_lst = {'position1': '', 'position2': '', 'position3': '', 'position4': '', 'position5': '', 'position6': '',
           'position7': '', 'position8': '', 'position9': ''}


def func(x, y):
    t_new = turtle.Turtle()
    t_new.hideturtle()
    t_new.pensize(10)
    t_new.speed(-1)
    global b, win_lst, krestwin, krugwin, t, username, username2
    x_list = {}
    y_list = {}
    x_list2 = {}
    y_list2 = {}
    endvallist = []
    endvallist2 = []
    positiondicti = {'position1': (30, 270), 'position2': (130, 270), 'position3': (230, 270), 'position4': (30, 170),
                     'position5': (130, 170), 'position6': (230, 170), 'position7': (30, 70), 'position8': (130, 70),
                     'position9': (230, 70)}
    sum1 = x - positiondicti['position1'][0], y - positiondicti['position1'][1]
    sum2 = x - positiondicti['position2'][0], y - positiondicti['position2'][1]
    sum3 = x - positiondicti['position3'][0], y - positiondicti['position3'][1]
    sum4 = x - positiondicti['position4'][0], y - positiondicti['position4'][1]
    sum5 = x - positiondicti['position5'][0], y - positiondicti['position5'][1]
    sum6 = x - positiondicti['position6'][0], y - positiondicti['position6'][1]
    sum7 = x - positiondicti['position7'][0], y - positiondicti['position7'][1]
    sum8 = x - positiondicti['position8'][0], y - positiondicti['position8'][1]
    sum9 = x - positiondicti['position9'][0], y - positiondicti['position9'][1]
    if b % 2 == 0:
        t_new.up()
        for i in range(1, 10):
            x_list[f'sum {i}'] = abs(eval(f'sum{i}')[0])
            y_list[f'sum {i}'] = abs(eval(f'sum{i}')[1])
        for keys, items, keys2, items2 in zip(x_list.keys(), x_list.values(), y_list.keys(), y_list.values()):
            endvallist.append(items + items2)
        win_lst[str(f'position{endvallist.index(min(endvallist)) + 1}')] = 'крест'
        t_new.goto(eval(f'positiondicti["position{endvallist.index(min(endvallist)) + 1}"]'))
        t_new.down()
        t_new.right(45)
        t_new.forward(80)
        t_new.left(180)
        t_new.forward(40)
        t_new.right(90)
        t_new.forward(40)
        t_new.left(180)
        t_new.forward(80)
        t_new.left(45)
    else:
        t_new.up()
        for i in range(1, 10):
            x_list2[f'sum {i}'] = abs(eval(f'sum{i}')[0])
            y_list2[f'sum {i}'] = abs(eval(f'sum{i}')[1])
        for keys, items, keys2, items2 in zip(x_list2.keys(), x_list2.values(), y_list2.keys(), y_list2.values()):
            endvallist2.append(items + items2)
        win_lst[str(f'position{endvallist2.index(min(endvallist2)) + 1}')] = 'круг'
        t_new.goto(eval(f'positiondicti["position{endvallist2.index(min(endvallist2)) + 1}"][0]+15'),
                   eval(f'positiondicti["position{endvallist2.index(min(endvallist2)) + 1}"][1]-55'))
        t_new.down()
        t_new.circle(30)
    b += 1
    if (win_lst['position1'] == 'крест' and win_lst['position2'] == 'крест' and win_lst['position3'] == 'крест') or (
            win_lst['position4'] == 'крест' and
            win_lst['position5'] == 'крест' and win_lst['position6'] == 'крест') or (
            win_lst['position7'] == 'крест' and win_lst[
        'position8'] == 'крест' and win_lst['position9'] == 'крест') or (
            win_lst['position1'] == 'крест' and win_lst['position4'] == 'крест' and win_lst[
        'position7'] == 'крест') or (
            win_lst['position2'] == 'крест' and win_lst['position5'] == 'крест' and win_lst[
        'position8'] == 'крест') or (
            win_lst['position3'] == 'крест' and win_lst['position6'] == 'крест' and win_lst['position9'] == 'крест') or \
            (win_lst['position1'] == 'крест' and win_lst['position5'] == 'крест' and win_lst[
                'position9'] == 'крест') or (
            win_lst[
                'position3'] == 'крест' and win_lst['position5'] == 'крест' and win_lst['position7'] == 'крест'):
        krestwin += 1
        showinfo('Победа', f'Выиграл крест - счет {krestwin}:{krugwin}')
        t.reset()
        draw_field()
        t_new.hideturtle()
        t_new.speed(-1)
        t_new.up()
        style = ('Courier', 50, 'bold')
        t_new.goto(-148, -207)
        t_new.write(f'{username} {krestwin}:{krugwin} {username2}', font=style)
        t_new.down()
        b = 0
        win_lst = {'position1': '', 'position2': '', 'position3': '', 'position4': '', 'position5': '', 'position6': '',
                   'position7': '', 'position8': '', 'position9': ''}
    elif (win_lst['position1'] == 'круг' and win_lst['position2'] == 'круг' and win_lst['position3'] == 'круг') or (
            win_lst['position4'] == 'круг' and
            win_lst['position5'] == 'круг' and win_lst['position6'] == 'круг') or (
            win_lst['position7'] == 'круг' and win_lst[
        'position8'] == 'круг' and win_lst['position9'] == 'круг') or (
            win_lst['position1'] == 'крест' and win_lst['position4'] == 'крест' and win_lst[
        'position7'] == 'крест') or (
            win_lst['position2'] == 'круг' and win_lst['position5'] == 'круг' and win_lst[
        'position8'] == 'круг') or (
            win_lst['position3'] == 'круг' and win_lst['position6'] == 'круг' and win_lst['position9'] == 'круг') or \
            (win_lst['position1'] == 'круг' and win_lst['position5'] == 'круг' and win_lst['position9'] == 'круг') or (
            win_lst[
                'position3'] == 'круг' and win_lst['position5'] == 'круг' and win_lst['position7'] == 'круг'):
        krugwin += 1
        showinfo('Победа', f'Выиграл круг - счет {krestwin}:{krugwin}')
        t.reset()
        draw_field()
        t_new.hideturtle()
        t_new.speed(-1)
        t_new.up()
        style = ('Courier', 50, 'bold')
        t_new.goto(-145, -205)
        t_new.write(f'{username} {krestwin}:{krugwin} {username2}', font=style)
        t_new.down()
        b = 0
        win_lst = {'position1': '', 'position2': '', 'position3': '', 'position4': '', 'position5': '', 'position6': '',
                   'position7': '', 'position8': '', 'position9': ''}


turtle.onscreenclick(func)

turtle.done()

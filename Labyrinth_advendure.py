from tkinter import filedialog
from tkinter import *
import random
import os

def position():
    global x, y
    pos = canvas.coords(user)
    x,y = int(pos[0]),int(pos[1])
    X,Y = (x-30)//50,(y-70)//50
    return x,y,X,Y

def click(event): # Function of mouse movement
    x,y,X,Y = position()
    difx = x - event.x
    dify = y - event.y
    check = check_point(x,y)
    if (check != "A" and ca < 2) and (check != "K" and ck < 2):
        if difx < 0 and abs(difx) > abs(dify):
            if check_move(X,Y,"Right") != 'W':
                x += mv
                if x >= 530: x -=mv
                else:
                    canvas.move(user, mv, 0)
                    text_update(' '.join(phrase[7].split('. ')))
                    check = check_point(x,y)
                    if check[0] == "E":
                        trap_exit(x,y,check[1])
            else: wall_e(x,y)
        if difx > 0 and abs(difx) > abs(dify):
            if check_move(X,Y,"Left") != 'W':
                x -= mv
                if x <= 10: x += mv
                else:
                    canvas.move(user, -mv, 0)
                    text_update(' '.join(phrase[5].split('. ')))
                    check = check_point(x,y)
                    if check[0] == "E":
                        trap_exit(x,y,check[1])
            else: wall_w(x,y)
        if dify < 0 and abs(difx) < abs(dify):
            if check_move(X,Y,"Down") != 'W':
                y += mv
                if y >= 550: y -= mv
                else:
                    canvas.move(user, 0, mv)
                    text_update(' '.join(phrase[8].split('. ')))
                    check = check_point(x,y)
                    if check[0] == "E":
                        trap_exit(x,y,check[1])
            else: wall_s(x,y)
        if dify > 0 and abs(difx) < abs(dify):
            if check_move(X,Y,"Up") != 'W':
                y -= mv
                if y <= 20: y += mv
                else:
                    canvas.move(user, 0, -mv)
                    text_update(' '.join(phrase[6].split('. ')))
                    check = check_point(x,y)
                    if check[0] == "E":
                        trap_exit(x,y,check[1])
            else: wall_n(x,y)
    else:
        if check == "A": trap_count("A")
        else: trap_count("K")
    if event.x >= 20 and event.x<=70 and  event.y >= 710 and event.y<=760:
    	gamehelp()
    if event.x >= 470 and event.x<=520 and event.y >= 710 and event.y<=760:
        end()
    return x,y

def key(event): # Function of keyboard movement
    global pot, ca, ck
    x,y,X,Y = position()
    check = check_point(x,y)
    if (check != "A" and ca < 2) and (check != "K" and ck < 2): 
        if event.keysym == "Up":
            if check_move(X,Y,event.keysym) != 'W':
                y -= mv
                if y <= 20: y += mv
                else:
                    canvas.move(user, 0, -mv)
                    text_update(' '.join(phrase[6].split('. ')))
                    check = check_point(x,y)
                    if check[0] == "E":
                        trap_exit(x,y,check[1])
            else: wall_n(x,y)
        if event.keysym == "Down":
            if check_move(X,Y,event.keysym) != 'W': 
                y += mv
                if y >= 550: y -= mv
                else:
                    canvas.move(user, 0, mv)
                    text_update(' '.join(phrase[8].split('. ')))
                    check = check_point(x,y)
                    if check[0] == "E":
                        trap_exit(x,y,check[1])
            else: wall_s(x,y)
        if event.keysym == "Left":
            if check_move(X,Y,event.keysym) != 'W':
                x -= mv
                if x <= 10: x += mv
                else:
                    canvas.move(user, -mv, 0)
                    text_update(' '.join(phrase[5].split('. ')))
                    check = check_point(x,y)
                    if check[0] == "E":
                        trap_exit(x,y,check[1])
            else: wall_w(x,y)
        if event.keysym == "Right":
            if check_move(X,Y,event.keysym) != 'W':
                x += mv
                if x >= 530: x -= mv
                else:
                    canvas.move(user, mv, 0)
                    text_update(' '.join(phrase[7].split('. ')))
                    check = check_point(x,y)
                    if check[0] == "E":
                        trap_exit(x,y,check[1])
            else: wall_e(x,y)
    else:
        if check == "A": trap_count("A")
        else: trap_count("K")
    return x,y

def wall_w(x,y): # West wall
    text_update(' '.join(phrase[9].split('. ')))
    x1 = x2 = x-11
    y1 = y-11
    y2 = y1+51
    canvas.create_line(x1,y1,x2,y2,fill=lines,width=3)

def wall_n(x,y): # North wall
    text_update(' '.join(phrase[9].split('. ')))
    x1 = x-11
    x2 = x1+51
    y1 = y2 = y-11
    canvas.create_line(x1,y1,x2,y2,fill=lines,width=3)

def wall_e(x,y): # Est wall
    text_update(' '.join(phrase[9].split('. ')))
    x1 = x2 = x+39
    y1 = y-11
    y2 = y1+51
    canvas.create_line(x1,y1,x2,y2,fill=lines,width=3)

def wall_s(x,y):# South wall
    text_update(' '.join(phrase[9].split('. ')))
    x1 = x-11
    x2 = x1+51
    y1 = y2 = y+39
    canvas.create_line(x1,y1,x2,y2,fill=lines,width=3)
    

def gamehelp(): # Help Field
	HF = Toplevel(GF) 
	HF.geometry('+{}+{}'.format(200, 100))
	HF.title('Labyrinth adventure help')
	text = Text(HF,width=40, height=25, bg=background, fg='midnightblue', wrap=WORD, font="Sans 12")
	text.pack()
	text.insert(1.0, 'Help for the Labyrinthe Aventure')
	text.config(state=DISABLED)
	HF.update()
	HF.mainloop()

def text_update(text="",size=11,style="italic"): # Function to change text
    global x, y, text_field, txt, lib_sz, lib_st
    for i in range (5,-1,-1):
        if i != 0:
            txt[i] = txt[i-1]
            lib_sz[i] = lib_sz[i-1]
            lib_st[i] = lib_st[i-1]
        else:
            txt[i] = text
            lib_sz[i] = size
            lib_st[i] = style
    for i in range (0,6):
        dify = 567+17*i
        canvas.delete(text_field[i])
        text_field[i] = canvas.create_text(20,dify,text=txt[i],anchor=NW, fill=text_fill,font = "Sans {} {}".format(lib_sz[i],lib_st[i]))


def listline(X,Y): # Function searching point in maze
    Z = X+10*Y
    point = maze[Z]
    return point

def check_move(X,Y,key="",check = 'P'): # Function Verifitation of Movements
    point = listline(X,Y)
    if X == point[0] and Y == point[1] and (key == "Left" and point[2] == 'W'):
        check = 'W'
    if X == point[0] and Y == point[1] and (key == "Up" and point[3] == 'W'):
        check = 'W'
    if X == point[0] and Y == point[1] and (key == "Right" and point[4] == 'W'):
        check = 'W'
    if X == point[0] and Y == point[1] and (key == "Down" and point[5] == 'W'):
        check = 'W'
    if X == point[0] and Y == point[1] and \
         (key == "Left" and point[6] == 'XW' or key == "Up" and point[6] == 'XN' or \
          key == "Right" and point[6] == 'XE' or key == "Down" and point[6] == 'XS'):
        text_update(' '.join(phrase[10].split('. ')),12,'bold italic')
        exitmz(pot[0])
    return check

def check_point(x,y,check = 'P'): # Function of Verifitation Actions
    x,y,X,Y = position()
    point = listline(X,Y)
    if point[6] == 'F' or point[6] == 'X':
        if pot[0] == '0':
            canvas.delete(tr)
            trap_draw(x,y,"X",treascol)
            text_update(' '.join(phrase[12].split('. ')),11,"bold italic")
            text_update(' '.join(phrase[11].split('. ')),11,"bold italic")
            pot[0] = point[6]
            point[6] = '0'
            z = X+10*Y
            maze[z] = point
        else:
            trap_draw(x,y,"X")
            text_update('. '.join(phrase[13].split('. ')),11,"bold italic")
    elif point[6] == 'A':
        text_update(' '.join(phrase[15].split('. ')),11,"bold")
        text_update(' '.join(phrase[14].split('. ')),11,"bold")
        check = 'A'
        trap(X,Y,check)
    elif point[6] == 'K':
        text_update(' '.join(phrase[16].split('. ')),11,"bold")
        check = 'K'
        trap(X,Y,check)
    elif point[6] == 'E1':
        check = point[6]
    elif point[6] == 'E2':
        check = point[6]
    elif point[6] == 'E3':
        check = point[6]
    elif point[6] == 'E4':
        check = point[6]
    elif point[6] == 'T1':
        check = 'T1'
        text_update(' '.join(phrase[17].split('. '))+"{}.".format(check[1]),12,"bold")
        trap(X,Y,check)
    elif point[6] == 'T2':
        check = 'T2'
        text_update(' '.join(phrase[17].split('. '))+"{}.".format(check[1]),12,"bold")
        trap(X,Y,check)
    elif point[6] == 'T3':
        check = 'T3'
        text_update(' '.join(phrase[17].split('. '))+"{}.".format(check[1]),12,"bold")
        trap(X,Y,check)
    elif point[6] == 'T4':
        check = 'T4'
        text_update(' '.join(phrase[17].split('. '))+"{}.".format(check[1]),12,"bold")
        trap(X,Y,check)
    return check

def trap(X,Y,check): # Function of traps
    pos = canvas.coords(user)
    x,y = int(pos[0]),int(pos[1])
    if len(check)>1: txt = check[1]
    else: txt = check
    canvas.create_text(x+15,y,text=txt,anchor=N,fill="darkgray",font = "Sans 20 bold")
    trap_count(check)
    if check == 'T1':
        for p in maze:
            if p[6] == 'E1':
                X,Y = p[0],p[1]
                check = 'I'
            else: continue
    elif check == 'T2':
        for p in maze:
            if p[6] == 'E2':
                X,Y = p[0],p[1]
                check = 'II'
            else: continue
    elif check == 'T3':
        for p in maze:
            if p[6] == 'E3':
                X,Y = p[0],p[1]
                check = 'III'
            else: continue
    elif check == 'T4':
        for p in maze:
            if p[6] == 'E4':
                X,Y = p[0],p[1]
                check = 'IV'
            else: continue
    x,y = X*50+30,Y*50+70
    trap_draw(x,y,check)

def trap_draw(x,y,check,color="darkgray"):  # Function of traps drawning
    global user,tr
    canvas.delete(user)
    tr = canvas.create_text(x+15,y,text=check,anchor=N,fill=color,font = "Sans 20 bold")
    user = canvas.create_oval(x, y, x+30, y+30, fill=text_fill)

def trap_count(check):  # Function of traps counters
    global ct, ca, ck, maze
    pos = canvas.coords(user)
    x,y = int(pos[0]),int(pos[1])
    X,Y = (x-30)//50,(y-70)//50
    z = X+10*Y
    point = listline(X,Y)
    if check == 'T1' or check == 'T2' or check == 'T3' or check == 'T4':
        n = int(check[1])-1
        ct[n] += 1
        if ct[n] >= 2: point[6] = '0'; maze[z] = point; ct[n] = 0
    if check == 'A':
        if ca < 2: x,y = int(pos[0]),int(pos[1]); ca += 1
        else: point[6] = '0'; z = X+10*Y; maze[z] = point; ca = 0
    if check == 'K':
        if ck < 2: x,y = int(pos[0]),int(pos[1]); ck += 1
        else: point[6] = '0'; z = X+10*Y; maze[z] = point; ck = 0

def trap_exit(x,y,n):  # Function of traps exits
    global user
    if int(n) < 4: txt = 'I'*int(n)
    else: txt = 'IV'
    text_update(" ".join(phrase[18].split('. '))+"{}.".format(n),10,"bold italic")
    canvas.delete(user)
    canvas.create_text(x+15,y,text=txt,anchor=N,fill="darkgray",font = "Sans 20 bold")
    user = canvas.create_oval(x, y, x+30, y+30, fill=text_fill)

def quit_restart(event):
    global x, y
    if event.x >= 70 and event.x <= 170 and event.y >= 400 and event.y<=450:
        restart()
    elif event.x >= WIDTH-171 and event.x <= WIDTH-73 and event.y >= 400 and event.y<=450: end()

def exitmz(treasure):
    global pot
    if treasure == 'X':
        pot[0] = '0'
        TEXT = f"! \n".join(phrase[19].split("! "))
        canvas.create_rectangle(22, HEIGHT//2-140, WIDTH-23, HEIGHT//2+70, fill=background, outline=backlines)
        canvas.create_text(WIDTH//2,HEIGHT//2-70,text=TEXT, justify=CENTER, fill=text_fill,font = "Sans 20 italic bold")
        canvas.create_line(70,400,172,400,fill=border,width=4)
        canvas.create_line(172,398,172,452,fill=border,width=4)
        canvas.create_line(174,450,70,450,fill=border,width=4)
        canvas.create_line(72,450,72,400,fill=border,width=4)
        canvas.create_text(122,400,text="R",anchor=N,fill=border,font = "Sans 18 bold")
        canvas.create_text(122,425,text="restart",anchor=N,fill=border,font = "Sans 16 bold")
        canvas.create_line(WIDTH-171,400,WIDTH-73,400,fill=border,width=4)
        canvas.create_line(WIDTH-73,398,WIDTH-73,452,fill=border,width=4)
        canvas.create_line(WIDTH-73,450,WIDTH-173,450,fill=border,width=4)
        canvas.create_line(WIDTH-171,450,WIDTH-171,400,fill=border,width=4)
        canvas.create_text(WIDTH-123,400,text="Q",anchor=N,fill=border,font = "Sans 18 bold")
        canvas.create_text(WIDTH-123,425,text="quit",anchor=N,fill=border,font = "Sans 16 bold")
        canvas.bind("<R>", lambda event: restart())
        canvas.bind("<r>", lambda event: restart())
        canvas.bind("<Button-1>", quit_restart)
    elif treasure == 'F':
        text_update("")
        text_update("")
        text_update(f".\n".join(phrase[20].split('. ')),15,"bold")
        pot[0] = '0'
    elif treasure == '0':
        text_update("")
        text_update("")
        text_update(f"! \n".join(phrase[21].split('! ')),15,"bold")

# GAME MODULE

runing = True
WIDTH = 540
HEIGHT = 800
mv = 50

def run():
    global canvas,user,GF,end,restart,maze,txt,ca,ck,lib_sz,lib_st,text_field,txt,pot,ct
    def restart():
        GF.destroy()
 
    def end():
        global runing
        runing = False
        GF.destroy()

#   LOADING FILES and INSTALLATION VARIABLES

    f = open('labyrinth.cfg')
    i = 0
    for line in f.read().splitlines():
        if i == 0: lng = line
        else: scheme = line
        i += 1

    def loadlang(lng):
        global phrase
        phrase = []
        file = lng+'.lng'
        f = open(file)
        for line in f.read().splitlines():
            phrase.append(line)
        return phrase

    def change_cfg(ln,cmd):
        with open('labyrinth.cfg', 'r') as f1:
            lines = f1.readlines()
        with open('labyrinth.cfg', 'w') as f2:
            for i in range(len(lines)):
                if i+1 == ln:
                    f2.write(cmd+'\n')
                else:
                    f2.write(lines[i])

    def english():
        loadlang('eng')
        change_cfg(1,'eng')
        restart()

    def french():
        loadlang('fr')
        change_cfg(1,'fr')
        restart()

    def russian():
        loadlang('rus')
        change_cfg(1,'rus')
        restart()

    def white():
        global background, border, lines, backlines, text_fill, treascol
        background = 'linen'
        border = 'darkgray'
        lines = 'midnightblue'
        backlines = 'skyblue'
        text_fill = 'midnightblue'
        treascol = 'lightgray'

    def black():
        global background, border, lines, backlines, text_fill, treascol
        background = 'black'
        border = 'darkgray'
        lines = 'white'
        backlines = 'darkslateblue'
        text_fill = 'mediumturquoise'
        treascol = 'lightslategray'

    def change_scheme(scheme):
        global lng
        if scheme == 'white':
            white()
            change_cfg(2,scheme)
        else:
            black()
            change_cfg(2,scheme)
        restart()

    j = 0
    for files in os.listdir("./"):
        if files.endswith(".mz"):
            j += 1
    f = random.randrange(0,j)
    if f < 10: file = '00'+str(f)+'.mz'
    elif f>9 and f < 100: file = '0'+str(f)+'.mz'
    else: file = str(f)+'.mz'

#   Load scheme
    if scheme == 'black':
        black()
    else: white()

    loadlang(lng)

    def loadmaze(file): # Load Maze + installation of actions
        maxx, maxy, a = [],[],[]
        f = open(file)
        for line in f.read().splitlines():
            maze.append(line.split(','))
            if maze[maze.index(line.split(','))][2] == maze[maze.index(line.split(','))][3] == maze[maze.index(line.split(','))][4] == 'W' or\
               maze[maze.index(line.split(','))][2] == maze[maze.index(line.split(','))][3] == maze[maze.index(line.split(','))][5] == 'W' or\
               maze[maze.index(line.split(','))][2] == maze[maze.index(line.split(','))][4] == maze[maze.index(line.split(','))][5] == 'W' or\
               maze[maze.index(line.split(','))][3] == maze[maze.index(line.split(','))][4] == maze[maze.index(line.split(','))][5] == 'W': a.append(line.split(','))
        for c in range(0,4):
            rnd = random.randrange(0,len(a))
            if c == 0: maze[maze.index(a[rnd])][6] = 'X'
            else: maze[maze.index(a[rnd])][6] = 'F'
            a.remove(a[rnd])
        acts = ['A','K','T1','T2','T3','T4','E1','E2','E3','E4','I','I','I']
        while len(acts) != 0:
            i = 0
            j = 0
            for p in maze:
                p[0] = int(p[0])
                p[1] = int(p[1])
                maxx.append(p[0])
                maxy.append(p[1])
                ln = len(maze)-j
                b = random.randrange(0,ln)
                if p[6] == '0' and len(acts) != 0:
                    i += 1
                    if i == b and p[6] == '0': p[6] = acts.pop(); j +=1;
        maxx,maxy = max(maxx)+1,max(maxy)+1
        return maze,maxx,maxy 

    maze,maxx,maxy,lib_sz,lib_st,text_field,txt,pot,ct = [],[],[],[],[],[],[],['0','0'],[0,0,0,0]
    ca,ck,cf = 0,0,3
    maze,maxx,maxy = loadmaze(file)
    X,Y = random.randrange(0,maxx),random.randrange(0,maxy)
    x,y = X*50+30,Y*50+70
        
#   Game Field        
    GF = Tk()
    GF.lift()
    GF.wm_iconbitmap("labyrinthe.ico")
    GF.title('Labyrinth adventure')
    GF.resizable(0, 0)
    
#   Menu
    mainmenu = Menu(GF)
    GF.config(menu=mainmenu)

    langmenu = Menu(mainmenu, tearoff=0)
    langmenu.add_command(label="".join(phrase[2].split(', ')[0]), command=english)
    langmenu.add_command(label="".join(phrase[2].split(', ')[1]), command=french)
    langmenu.add_command(label="".join(phrase[2].split(', ')[2]), command=russian)
     
    themmenu = Menu(mainmenu, tearoff=0)
    themmenu.add_command(label="".join(phrase[3].split(', ')[1]), command=lambda:change_scheme('white'))
    themmenu.add_command(label="".join(phrase[3].split(', ')[0]), command=lambda:change_scheme('black'))

    mainmenu.add_cascade(label="".join(phrase[1].split(', ')[0]), menu=langmenu)
    mainmenu.add_cascade(label="".join(phrase[1].split(', ')[1]), menu=themmenu)

    canvas = Canvas(GF, width=WIDTH, height=HEIGHT, highlightthickness=0, bg=background)
    canvas.focus_set()
    canvas.pack()

    for i in range (0,2000,50):
        canvas.create_line(0,10+i,WIDTH,10+i,fill=backlines,width=2)
        canvas.create_line(20+i,0,20+i,HEIGHT,fill=backlines,width=2)
#   Title
    canvas.create_text(270,30,text="LABYRINTHE AVENTURE",fill=text_fill,font = "Times 20 italic bold")
#   Pencil border
    canvas.create_line(18,60,520,60,fill=border,width=4)
    canvas.create_line(520,58,520,560,fill=border,width=4)
    canvas.create_line(522,560,18,560,fill=border,width=4)
    canvas.create_line(20,60,20,560,fill=border,width=4)
#   User start point
    user = canvas.create_oval(x, y, x+30, y+30, fill=text_fill)
#   Key binding
    canvas.bind('<Up>', key)
    canvas.bind('<Down>', key)
    canvas.bind('<Left>', key)
    canvas.bind('<Right>', key)
    canvas.bind('<q>',lambda event: end())
    canvas.bind('<Q>',lambda event: end())
    canvas.bind('<?>',lambda event: gamehelp())
    canvas.bind('<h>',lambda event: gamehelp())
    canvas.bind('<H>',lambda event: gamehelp())
    canvas.bind('<Button-1>', click)
#   Start text
    TEXT0 = ""
    TEXT1 = f'.\n'.join(phrase[0].split('. '))
    tr = trap_draw(x,y,"")
    for i in range (0,6):
        text_field.append('text_field'+str(i+1))
        txt.append('TEXT'+str(i+1))
        dify = 567+17*i
        size = 11
        style = 'italic'
        lib_sz.append(size)
        lib_st.append(style)
        if i == 0:
            txt[i] = TEXT1
            text_field[i] = canvas.create_text(20,dify,text=TEXT1,anchor=NW, fill=text_fill,font = "Sans {} {}".format(size,style))
        else:
            txt[i] = TEXT0
            text_field[i] = canvas.create_text(20,dify,text=TEXT0,anchor=NW, fill=text_fill,font = "Sans {} {}".format(size,style))

    GF.update()
#   Help button
    canvas.create_line(18,710,70,710,fill=border,width=4)
    canvas.create_line(70,708,70,760,fill=border,width=4)
    canvas.create_line(72,760,18,760,fill=border,width=4)
    canvas.create_line(20,760,20,710,fill=border,width=4)
    canvas.create_text(45,710,text="?",anchor=N,fill=border,font = "Sans 20 bold")
    canvas.create_text(45,740,text="help",anchor=N,fill=border,font = "Sans 11 bold")
#   Quit button
    canvas.create_line(520,710,468,710,fill=border,width=4)
    canvas.create_line(470,710,470,762,fill=border,width=4)
    canvas.create_line(470,760,522,760,fill=border,width=4)
    canvas.create_line(520,760,520,708,fill=border,width=4)
    canvas.create_text(495,710,text="Q",anchor=N,fill=border,font = "Sans 19 bold")
    canvas.create_text(495,740,text="quit",anchor=N,fill=border,font = "Sans 11 bold")


    GF.mainloop()
# GAME loop
while runing:
    run()

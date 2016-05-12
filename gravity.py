import curses
import time
from curses import wrapper

screen=curses.initscr()
y, x = 20, 20
gravity=[0,0]
def checkaround():
    global y, x, gravity
    rtnbool=1
    if not gravity[1]:
        if screen.inch(y+1,x)==ord(' ') and screen.inch(y-1,x)==ord(' '):
            rtnbool=0
    if gravity[1]:
        if screen.inch(y,x+1)==ord(' ') and screen.inch(y,x-1)==ord(' '):
            rtnbool=0
    return rtnbool

def game(scr):
    global y, x, gravity
    curses.start_color()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    screen.nodelay(1)
    screen.border()
    screen.addch(y,x, 'X')
    screen.refresh()
    while True:
        q="0"
        while q=="0":
            q=screen.getch()
            if not gravity[1]:
                if not gravity[0] and screen.inch(y+1,x)==ord(' '):
                    screen.addch(y,x, ' ')
                    y+=1
                    screen.addch(y,x, 'X')
                    screen.refresh()
                    time.sleep(0.1)
                if gravity[0] and screen.inch(y-1,x)==ord(' '):
                    screen.addch(y,x, ' ')
                    y-=1
                    screen.addch(y,x, 'X')
                    screen.refresh()
                    time.sleep(0.1)
            if gravity[1]:
                if gravity[0] and screen.inch(y,x-1)==ord(' '):
                    screen.addch(y,x, ' ')
                    x-=1
                    screen.addch(y,x, 'X')
                    screen.refresh()
                    time.sleep(0.1)
                if not gravity[0] and screen.inch(y,x+1)==ord(' '):
                    screen.addch(y,x, ' ')
                    x+=1
                    screen.addch(y,x, 'X')
                    screen.refresh()
                    time.sleep(0.1)
        if not gravity[1]:
            if q==ord('a') and screen.inch(y,x-1)==ord(' '):
                screen.addch(y,x, ' ')
                x-=1
                screen.addch(y,x, 'X')
                screen.refresh()
            if q==ord('d') and screen.inch(y,x+1)==ord(' '):
                screen.addch(y,x, ' ')
                x+=1
                screen.addch(y,x, 'X')
                screen.refresh()
        if gravity[1]:
            if q==ord('a') and screen.inch(y-1,x)==ord(' '):
                screen.addch(y,x, ' ')
                y-=1
                screen.addch(y,x, 'X')
                screen.refresh()
            if q==ord('d') and screen.inch(y+1,x)==ord(' '):
                screen.addch(y,x, ' ')
                y+=1
                screen.addch(y,x, 'X')
                screen.refresh()
        if q==ord('l') and checkaround():
            gravity[0]=1-gravity[0]
        if q==ord('k'):
            gravity[1]=1-gravity[1]
        if q==ord('x'):
            break
#wrapper(game)
game(screen)
screen.getch()
curses.endwin()

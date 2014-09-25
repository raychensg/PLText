import curses
import constants as cn

class curses_screen:
    def __enter__(self):
        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.keypad(1)
        SCREEN_HEIGHT, SCREEN_WIDTH = stdscr.getmaxyx()
        return stdscr
    def __exit__(self,a,b,c):
        curses.nocbreak()
        stdscr.keypad(0)
        curses.echo()
        curses.endwin()

def startup():
	stdscr.addstr('Welcome to Pilot Light\n')
	stdscr.refresh()

def act(command):
	cn.act(command, stdscr)

with curses_screen() as stdscr:
	stdscr.refresh()
	startup()
	while True:	
		stdscr.addstr('>>> ')
		stdscr.refresh()
		act(stdscr.getstr())
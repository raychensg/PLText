import curses
import re
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
	stdscr.addstr('----- Playing as ' + cn.active_character.name + ' -----\n')
	stdscr.refresh()

def act(command):
	command = re.sub(' ', '_', command)
	if command in cn.commands:
		stdscr.addstr(eval('cn.' + command + '(cn.active_character.name)'))
	else:
		stdscr.addstr(eval('cn.' + cn.commands[0] + '(cn.active_character.name)'))
	stdscr.refresh()

with curses_screen() as stdscr:
	stdscr.refresh()
	startup()
	while True:
		stdscr.addstr('>>> ')
		stdscr.refresh()
		act(stdscr.getstr())
		stdscr.addstr('\n')
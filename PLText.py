import curses

class Character:
    def __enter__(self):
        screen = curses.initscr()
        curses.cbreak()
        screen.keypad(1)
        SCREEN_HEIGHT, SCREEN_WIDTH = screen.getmaxyx()
        return screen

    def __exit__(self,a,b,c):
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()

    def __init__(self, data_file):
        self.data_file = data_file
        try:
    	    self.dat = __import__(data_file, globals(), locals(), ['*'])
        except ImportError:
            pass #Create a new randomly generated character file

    def act(self, cmd):
        pass

    def prompt(self):
        screen.addstr('>>> ')


characters = []

characters.append(Character('character_files.ray'))

with characters[0] as screen:
    characters[0].prompt()
    characters[0].act(screen.getstr)
    screen.refresh()
    screen.getch()
    exit()

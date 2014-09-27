import curses
import re

#Classes to be defined include Script, MissionCalc

#Define a scriptreader, which creates events based on a 
#scriptreader

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

    def act(self, cmd, args=[]):
        eval(repr(self.dat.commands[cmd](screen, args)))

    def interpret(self, first, rest=[]):
        if first in self.dat.commands:
            self.act(first, rest)
        else:
            if len(rest) == 0:
                if len(first) != 0:
                    self.act('error')
            if len(rest) >= 1:
                self.interpret(first + ' ' +  rest[0], rest[1::])

    def parse(self, in_cmd):
        cmd = []
        in_cmd = re.sub('[ ]', '\', \'', ''.join(map(chr, in_cmd)))
        in_cmd = '[\'%s\']' % in_cmd
        cmd = eval(in_cmd)

        if len(cmd) == 1:
            self.interpret(cmd[0])
        if len(cmd) > 1:
            self.interpret(cmd[0], cmd[1::])


    def prompt(self):
        screen.addstr('>>> ')
        screen.refresh()


class ClockTower:
    """The ClockTower serves as the satellite timekeeper,
    and all phones receive their time values through the
    value of time returned by ClockTower and the 
    zone_difference returned by Location.

    ClockTower only returns time.

    """

class Location:
    """Each notable location has a time zone shift, a map,
    and a description.

    Location has 3 basic functions:
    -   Map
    -   Zone

    Location stores these variables:
    -   description
    -   zone_difference
    """

class Phone:
    """Phone is one of the most useful and important 
    features in PL.
    Each PL Character has a Phone object. A phone defines
    a second terminal window, which displays time (pulled 
    from the global ClockTower class), and missed calls, 
    texts, and alarms.

    Phone has six important subfunctions:
    -   Call
    -   Messages
    -   Notes
    -   Maps
    -   Exit
    """

class Chatter:
    """Chatter is a mission chat-room for all characters on
    a given mission (and also can include hackers).

    Chatter stores:
    -   Characters (in the mission)
    """

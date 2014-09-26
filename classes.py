import curses
import constants as cn

#Classes to be defined include Script, MissionCalc

#Define a scriptreader, which creates events based on a 
#scriptreader


class ClockTower:
    """The ClockTower serves as the satellite timekeeper,
    and all phones receive their time values through the
    value of time returned by ClockTower and the 
    zone_difference returned by Location.

    ClockTower only returns time.

    """

class Command:
    def __init__(self, new_cmd, target_fn, docstr=''):
        self.new_cmd = new_cmd
        self.target_fn = target_fn

class CursesScreen:
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

class Character:
    """Every entity has a character class. Pilot Light
    characters spawn the main terminal window, where the
    player interacts with the world.

    Character has many variables:
    -   Name
    -   Stats
    -   Items
    -   Location

    Characters can:
    -   Listen (and remember)
    -   Act
    -   Die

    Pilot Light characters have a special item:
    -   Phone
    """
    def __init__(self, data_file): #Other shit comes later
        import_statement = 'import ' + data_file
        exec('import_statement')
        #print(eval(data_file + '.name'))
        #begin()

    def begin(self):
        with CursesScreen() as stdscr:
            stdscr.refresh()
            startup()
            while True: 
                stdscr.addstr('>>> ')
                stdscr.refresh()
                act(stdscr.getstr())

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
    def __init__(self, items): #other shit later
        self.items = items
    
    def survey(self):
        list_items = ''
        for i in range(0, len(self.items)):
            if i > 0:
                list_items += ", "
            list_items += self.items[i]
        return('Items: ' + list_items)

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

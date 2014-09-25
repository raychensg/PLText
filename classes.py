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
    def __init__(self, name, gender, location): #Other shit comes later
        self.name = name
        self.gender = gender
        if gender == 'male':
            self.ppronoun = 'his'
            self.pronoun = 'he'
        else:
            self.ppronoun = 'her'
            self.pronoun = 'she'
        self.location = location

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

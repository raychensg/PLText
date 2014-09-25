import datetime
import classes as cl

#Define a dictionary of commands

#Pilot Light begins on November 14, 2027, at 06:59:55 CST
#That translates to November 13, 2027, at 20:59:55 STD
t_zero = datetime.datetime(2027, 11, 13, 20, 59, 55, 0)

#Ray's day began on September 24, 2014, at 07:59:55 PST
#That translates to September 24, 2014, at 15:59:55 STD
t_ray_test = datetime.datetime(2014, 9, 24, 15, 59, 55, 0)

#Define characters!
Ray = cl.Character('Ray')
active_character = Ray


#Commands start here
commands = ['error', 'help','wake_up', 'quit']

def error(character):
	"""I'll make this more interesting later...
	For now, it'll just return stupid shit
	"""
	return('%s violently thrusted his hips, but to no avail' % character)

def help(character):
	"""Lists all the commands programmed and also shows how to
	get more information about them.
	"""
	return(commmands)

def wake_up(character):
	return('Ugghh\n...\n%s groggily sits up and gets out of bed' % character)

def quit(character):
	exit()
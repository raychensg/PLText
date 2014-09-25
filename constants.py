import datetime
import classes as cl
import re


#Define a dictionary of commands

#Pilot Light begins on November 14, 2027, at 06:59:55 CST
#That translates to November 13, 2027, at 20:59:55 STD
t_zero = datetime.datetime(2027, 11, 13, 20, 59, 55, 0)

#Ray's day began on September 24, 2014, at 07:59:55 PST
#That translates to September 24, 2014, at 15:59:55 STD
t_ray_test = datetime.datetime(2014, 9, 24, 15, 59, 55, 0)

#Define characters!
Slottman212 = cl.Location(['Phone', '3D Printer', 'Inkjet Printer', 'Bed', 'Desk Lamp'])
Ray = cl.Character('Ray', 'male', Slottman212)
active_character = Ray


def act(command, screen):
	if command != '':
		if command[0:5] == 'help ':
			target = command[5::]
			if target in commands:
				target = re.sub(' ', '_', target)
				screen.addstr(eval(target + '(0)'))
			else:
				screen.addstr('No such command')
			screen.addstr('\n')
		elif command[0:5] == 'bind ':
			new_command = ''
			binding = True
			i = 5
			while i < len(command) and binding:
				if command[i] == '-':
					binding = False
				else:
					new_command += command[i]
				i += 1
			target = command[i::]
			if target in commands:
				bound[commands.index(target)] = new_command
			else:
				screen.addstr('No such command')
				screen.addstr('\n')
		else:
			if command in commands:
				command = re.sub(' ', '_', command)
				screen.addstr(eval(command + '(active_character)'))
			elif command in bound:
				command = re.sub(' ', '_', commands[bound.index(command)])
				screen.addstr(eval(command + '(active_character)'))
			else:
				screen.addstr(eval(commands[0] + '(active_character)'))
			screen.addstr('\n')
	screen.refresh()

def act2(command, screen):
	#Parse things by space
	if command != '':
		input_commands = []
		temp = ''
		for i in range(0, len(command)):
			if command[i] == ' ' or i == len(command) - 1:
				input_commands += temp
			else:
				temp += command[i]

	if 'bind' in input_commands  and 'to' in input_commands:
		new_command  = ''
		for i in range(input_commands.index('bind'), input_commands.index('to')):
			new_command += input_commands[i] + ' '
		new_command = new_command[0:len(new_command) - 2]
		target = ''
		for i in range(input_commands.index('to'), len(input_commands)):
			target += input_commands[i] + ' '
		target = target[0:len(target) - 2]

		if target in commands:
			bound[commands.index(target)] =  
		else:
			screen.addstr('No such command')


	screen.refresh()

class Command:
    def __init__(self, new_cmd, target_fn):
        self.new_cmd = new_cmd
        self.target_fn = target_fn

commands = []#['error', 'help', 'bind', 'wake up', 'brush teeth', 'look around', 'quit']
bound = []

def error(character):
	"""I'll make this more interesting later...
	For now, it'll just return stupid shit
	"""
	#return('%s violently thrusted his hips, but to no avail' % character)
	if character == 0:
		return('Checks if the command entered is valid')
	return('%s thumps %s chest defiantly' % (character.name, character.ppronoun))
commands += Command('error', error)

def help(character):
	if character == 0:
		return('Lists all the commands programmed and also shows how toget more information about them.')
	str_commands = 'Specific instructions available by using help <command>\n'
	for s in commands:
		str_commands += '    ' + s + '\n'
	return(str_commands)
commands += Command('help', help)

def bind(character):
	if character == 0:
		return('binds a user-defined command to an existing one')
commands += Command('bind', bind)

def wake_up(character):
	if character == 0:
		return('Wakes the active character up')
	return('Ugghh\n...\n%s groggily sits up and gets out of bed' % character.name)

def look_around(character):
	if character == 0:
		return('Examines the area that the character is in')
	return(character.location.survey())

def brush_teeth(character):
	if character == 0:
		return('Hygeine matters')
	return('Bzzz Bzzz')

def quit(character):
	if character == 0:
		return('Closes PLText')
	exit()
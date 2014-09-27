def help():
	str_commands = 'Specific instructions available by using help <command>\n'
	for s in commands:
		str_commands += '    ' + s + '\n'
	stdscr.addstr(str_commands)
commands.append(Command('help', help, 'Lists all the commands programmed and also shows how toget more information about them.'))

def bind(args):
	pass
commands.append(Command('bind', bind, 'binds a user-defined command to an existing one'))

def quit():
	exit()
commands.append(Command('quit', quit, 'Closes PLText'))
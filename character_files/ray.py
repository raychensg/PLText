import time

name = 'Ray'
gender = 'Male'
location = 'Slottman 212'
alive = True

commands = {}

def make_cmd(fn):
	commands.update({fn('name'):fn})

def slow_show(entries, screen, t_delay=0.1):
	for i in range(0, len(entries)):
		for c in entries[i]:
			screen.addstr(c)
			screen.refresh()
			time.sleep(t_delay/len(entries))
		screen.addstr('\n')
		screen.refresh()

@make_cmd
def wake_up(screen, args=[]):
	if screen == 'name':
		return 'wake up'
	slow_show(['Ugh', '...', name + ' slowly sits up and rubs his eyes'], screen)

@make_cmd
def error(screen, args=[]):
	if screen == 'name':
		return 'error'
	slow_show(['%s cries pitifully' % name], screen, 0.05)

@make_cmd
def quit(screen, args=[]):
	if screen == 'name':
		return 'quit'
	screen.exit()
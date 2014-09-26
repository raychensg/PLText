commands = {}

name = 'Ray'
gender = 'Male'
location = 'Slottman 212'
alive = True

commands = {}

def make_cmd(fn):
	commands.update({fn('name'):fn})

@make_cmd
def wake_up(screen):
	if screen == 'name':
		return 'wake up'
	slow_show(['Ugh', '...', name + ' slowly sits up and rubs his eyes'], screen)

def slow_show(entries, screen, wait=0.5):
	time.sleep(wait)
	for e in entires:
		screen.addstr(e + '\n')
		screen.refresh()
		time.sleep(wait)
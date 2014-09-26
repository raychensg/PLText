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
Ray = cl.Character('ray')
Jake = cl.Character('jake')
Fang = cl.Character('fang')

active_character = Ray
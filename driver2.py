import sys
import os
import input.interactive as i
import exc_diff.single as s
import output.csv as c

system, start_time, end_time = i.interactive()

t_list, exc_list = s.single(system, start_time, end_time)

c.write_csv(t_list, exc_list, 'out')


def __init__():
    pass

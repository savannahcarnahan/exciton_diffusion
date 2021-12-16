import sys
import os
import input.interactive as i
import exc_diff.single as s
import output.graph as g

system, start_time, end_time = i.interactive()

t_list, exc_list = s.single(system, start_time, end_time)

g.graph(t_list, exc_list)


def __init__():
    pass

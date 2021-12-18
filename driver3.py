import sys
import input.com_line as i
import exc_diff.single as s
import output.csv as c

system, start_time, end_time = i.command_line(sys.argv[1:])

t_list, exc_list = s.single(system, start_time, end_time)

c.write_csv(t_list, exc_list, 'out')


def __init__():
    pass

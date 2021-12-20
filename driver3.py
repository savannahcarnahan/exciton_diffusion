import sys
import input.com_line as i
import exc_diff.run as s
import output.csv as c

system, start_time, end_time = i.command_line(sys.argv[1:])

t_list, exc_list = s.run(system, start_time, end_time, 5, 'average')

c.write_csv(t_list, exc_list, 'out')


def __init__():
    pass

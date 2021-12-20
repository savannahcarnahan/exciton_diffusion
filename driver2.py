import sys
import os
import input.com_line as i
import exc_diff.run as ex
import output.graph as g


def main():
    system, start_time, end_time = i.command_line(sys.argv[1:])

    t_list, exc_list = ex.run(system, start_time, end_time, 10)

    g.graph(t_list, exc_list, 'in_file')


if __name__ == "__main__":
    # cProfile.run('main()','profileout.txt')
    main()

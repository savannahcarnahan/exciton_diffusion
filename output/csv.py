import csv
import output.get_diffusion as d
def write_csv(t_list, exc_list, name = 'out'):

    list1 = t_list
    list2 = d.get_diffusion(exc_list)
    file_name = name + '.csv'

    f = open(file_name,'w')

    writer = csv.writer(f)

    for w in range(len(list2)):

        writer.writerow([list1[w], list2[w]])

    f.close()



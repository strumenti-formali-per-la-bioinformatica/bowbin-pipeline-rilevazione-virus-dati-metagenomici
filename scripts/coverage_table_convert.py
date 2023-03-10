import argparse
import os
import sys

def convert(infile, outfile, num_avg, num_stdev):
    with open(infile, 'r') as in_table, open(outfile, 'w') as out_table:
        first = in_table.readline().strip("\n").split("\t")[3:]
        total = len(first)+3
        out_table.write("scaffold")
        for item in first:
            if item[-4:] == '-var':
                out_table.write("\tstdev_" + str(item.rsplit("-",1)[0]))
            else:
                out_table.write("\tavg_" + str(item))
        for line in in_table:
            line = line.strip("\n").split("\t")
            out_table.write("\n" + line[0])
            for n in range(3,total,2):
                #out_table.write("\t" + line[n])
                out_table.write("\t" + str(float(line[n])*float(num_avg)))
                sd = float(line[n+1])**0.5
                sd = sd*float(num_stdev)
                out_table.write("\t" + str(sd))


if __name__ == '__main__':
 
    vRhyme = argparse.ArgumentParser(description="Convert a MetaBat2 'jgi_summarize_bam_contig_depths' generated coverage table into vRhyme format for -c input.")
    vRhyme.add_argument('-i', metavar='', type=str, nargs=1, required=True, help="input coverage table in MetaBat2 format")
    vRhyme.add_argument('-o', metavar='', type=str, nargs=1, required=True, help='output coverage table in vRhyme format')
    vRhyme.add_argument('-multiplyAvg', metavar='', type=str, nargs=1, required=True, help='-multiplyAvg = num, multiply avg MetaBat for num')
    vRhyme.add_argument('-multiplyStdev', metavar='', type=str, nargs=1, required=True, help='-multiplyStdev = num, multiply stdev MetaBat for num')
    #
    args = vRhyme.parse_args()
    #
    #
    if os.path.exists(str(args.o[0])):
        sys.stderr.write("\nError: output table (-o) already exists. Exiting.\n\n")
        exit()

    convert(args.i[0], args.o[0], args.multiplyAvg[0], args.multiplyStdev[0])

#
#
#

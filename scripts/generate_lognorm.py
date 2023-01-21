import sys

if __name__ == "__main__":
    file_out = open(sys.argv[1]+".lognorm", "w")
    with open(sys.argv[1]) as fasta_file:
        fasta_file.readline()
        for line in fasta_file:
            file_out.write(line)
    file_out.flush()
    file_out.close()

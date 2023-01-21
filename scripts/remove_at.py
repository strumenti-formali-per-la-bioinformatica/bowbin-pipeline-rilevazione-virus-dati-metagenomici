import sys

if __name__ == "__main__":
    file_out = open(sys.argv[2], "w")
    with open(sys.argv[1]) as fasta_file:
        for line in fasta_file:
            file_out.write(line.replace("@", ">"))
    file_out.flush()
    file_out.close()

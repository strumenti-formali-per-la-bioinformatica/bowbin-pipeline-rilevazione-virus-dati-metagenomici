import sys

if __name__ == "__main__":
    count = 0
    file_out = open(sys.argv[2], "w")
    with open(sys.argv[1]) as fasta_file:
        fasta_head = fasta_file.readline().replace(", complete genome", "")
        file_out.write(fasta_head.replace(">", ">" + str(int(count / int(sys.argv[3]))) + "_"))
        for line in fasta_file:
            count += 1
            file_out.write(line)
            if count % int(sys.argv[3]) == 0:
                file_out.write("\n" + fasta_head.replace(">", ">" + str(int(count / int(sys.argv[3]))) + "_"))

    file_out.flush()
    file_out.close()


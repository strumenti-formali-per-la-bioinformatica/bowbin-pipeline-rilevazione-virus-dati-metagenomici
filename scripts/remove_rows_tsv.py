import csv
import sys

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        data = [row for row in reader if row[1] != '0.0']

    with open(sys.argv[1], 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(data)

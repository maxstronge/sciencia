with open(r"Labs\final\output_5.txt", 'r') as infile, open('PHYS397/Labs/final/output_5.txt', 'w') as outfile:
    for line in infile:
        columns = line.split()
        if len(columns) >= 2 and columns[0].isdigit() and columns[1].isdigit():
            columns[0] = str(int(columns[0]) - 629)
            columns[1] = str(int(columns[1]) - 145770470)
            line = ' '.join(columns) + '\n'
        outfile.write(line)
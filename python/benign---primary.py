# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"62383.0","system":"readv2"},{"code":"45735.0","system":"readv2"},{"code":"66436.0","system":"readv2"},{"code":"66816.0","system":"readv2"},{"code":"2742.0","system":"readv2"},{"code":"1269.0","system":"readv2"},{"code":"33859.0","system":"readv2"},{"code":"70785.0","system":"readv2"},{"code":"29737.0","system":"readv2"},{"code":"7789.0","system":"readv2"},{"code":"22609.0","system":"readv2"},{"code":"56515.0","system":"readv2"},{"code":"14960.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benign-neoplasm-and-polyp-of-uterus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benign---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benign---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benign---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

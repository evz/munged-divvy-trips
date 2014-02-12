from csvkit.unicsv import UnicodeCSVReader, UnicodeCSVWriter

def clean(fname):
    f = open(fname, 'rb')
    reader = UnicodeCSVReader(f)
    outp = []
    header = reader.next()
    for row in reader:
        try:
            row[0] = int(row[0])
            row[3] = int(row[3])
            row[5] = int(row[5])
            row[7] = int(row[7])
            row[4] = row[4].replace(',', '')
            if len(row) == 12:
                outp.append(row)
        except (TypeError, ValueError):
           print row
    o = open('%s_cleaned.csv' % fname, 'wb')
    writer = UnicodeCSVWriter(o)
    writer.writerow(header)
    writer.writerows(outp)

if __name__ == "__main__":
    clean('trips.csv')

from csvkit.unicsv import UnicodeCSVReader, UnicodeCSVWriter

def clean(f):
    reader = UnicodeCSVReader(f)
    good = []
    bad = []
    header = reader.next()
    for row in reader:
        try:
            row[0] = int(row[0])
            row[3] = int(row[3])
            row[5] = int(row[5])
            row[7] = int(row[7])
            row[4] = row[4].replace(',', '')
            if len(row) == 12:
                good.append(row)
            else:
                bad.append(row)
        except (TypeError, ValueError):
           bad.append(row)
    goodf = open('data/trips_cleaned.csv', 'wb')
    badf = open('data/trips_dirty.csv', 'wb')
    goodwriter = UnicodeCSVWriter(goodf)
    goodwriter.writerow(header)
    goodwriter.writerows(good)
    badwriter = UnicodeCSVWriter(badf)
    badwriter.writerow(header)
    badwriter.writerows(bad)
    goodf.close()
    badf.close()

if __name__ == "__main__":
    import gzip
    from cStringIO import StringIO
    gz = open('data/trips_raw.csv.gz', 'rb')
    with gzip.GzipFile(fileobj=gz) as f:
        clean(f)

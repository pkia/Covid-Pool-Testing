import csv
def get_columns(csv_file):
    csv_reader = csv.reader(csv_file, delimiter = '')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print("Column names are {}".join(row))
    else:
        print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')


get_columns()

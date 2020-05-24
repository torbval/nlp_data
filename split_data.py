import os
import csv


def split(_file_handler, _file_name, delimiter=',', row_limit=10000, output_path='.', keep_headers=True):
    """
    Splits a CSV file into multiple pieces.

    A quick bastardization of the Python CSV library.
    Arguments:
        `row_limit`: The number of rows you want in each output file
        `output_name_template`: A %s-style template for the numbered output files.
        `output_path`: Where to stick the output files
        `keep_headers`: Whether or not to print the headers in each output file.
    Example usage:

        >> from toolbox import csv_splitter;
        >> csv_splitter.split(csv.splitter(open('/home/ben/Desktop/lasd/2009-01-02 [00.00.00].csv', 'r')));

    """
    reader = csv.reader(_file_handler, delimiter=delimiter)
    current_piece = 1
    output_name_template = 'data_parts/{}_part_%s.csv'.format(_file_name)
    current_out_path = os.path.join(
        output_name_template % current_piece
    )
    current_out_writer = csv.writer(open(current_out_path, 'w', encoding="utf-8"))
    current_limit = row_limit
    headers = None
    if keep_headers:
        headers = next(reader)
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w', encoding="utf-8"))
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)


file_name = "test_processed"
file_handler = open('{}.csv'.format(file_name), 'r', encoding="utf-8")
split(file_handler, file_name, row_limit=10000)

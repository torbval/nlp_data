import pandas as pd
import glob

file_name = "train_processed"
all_file_parts = glob.glob('data_parts/{}_part_*.csv'.format(file_name))

data_frame = pd.concat((pd.read_csv(file_part) for file_part in all_file_parts))
columns = list(filter(lambda x: x[:7] != 'Unnamed', data_frame.columns))
data_frame = data_frame[columns]
print(data_frame.head(5))
print(len(data_frame))

data_frame.to_csv("{}.csv".format(file_name))
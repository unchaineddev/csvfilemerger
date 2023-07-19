# Path Name Pattern Expansion
import glob
import pandas as pd


# list all csv files
csv_files = glob.glob('*.{}'.format('csv'))



new = []
# iterate through the csv file and concatenate it
for f in csv_files:
    new.append(pd.read_csv(f))

# Concatenate all files together 
merged_file = pd.concat(new, ignore_index=True)

# Saving the file back to csv
merged_file.to_csv("mergedfile.csv")



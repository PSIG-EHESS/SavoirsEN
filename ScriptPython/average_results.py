import pandas as pd
import glob

# path to all files precision and rappel by each algorythm 
path = r'/Users/alexsoares/Desktop/EHESS/dev/Savoirs_Spacy/db_results/SpaCy_precision_rappel/precision_rappel_BERT/' # use your path
# all files with format csv
all_files = glob.glob(path + "/*.csv")

#list empty
#li = []

# loop for concatenate them
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    #li.append(df)

    # concatenate it using pandas with a small loop
    #df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
    #df_merged = pd.concat(df_from_each_file, ignore_index=True)
    #df_merged.to_csv( "/Users/alexsoares/Desktop/EHESS/dev/Savoirs_Spacy/db_results/SpaCy_precision_rappel/all_merged_BERT.csv")

    # print it to verify
    #print(df_merged)

    # create the average from all files
    average = df.groupby(df.columns, axis=1).sum()
    print(average)
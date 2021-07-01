# operation system
import os
# regular expression
import re
# retrives file support
import glob
# make a table
import pandas as pd
# regular expression
import re

#function to compare columns NE-COARSE-LIT x GOLD
def compare(x):    
	return '1' if x['PREDICTION'] == x['GOLD'] else 'O'

path_hand = r'/Users/alexsoares/Desktop/EHESS/dev/Savoirs_Spacy/hand_pandas' # use your path
path_clean = r'/Users/alexsoares/Desktop/EHESS/dev/Savoirs_Spacy/SpaCy_BIO/SpaCy_sm_BIO' 

# inform the path
for file_path in glob.iglob(path_hand + "/*.txt"):
	#transform path into a readable file
	f_hand = file_path
	
	# open the variable to be read and split into words
	with open(f_hand, 'r', encoding='utf8') as f:
		t_hand = f.read()
		for f_path in glob.iglob(path_clean + "/*.txt"):
			
			#transform path into a readable file
			f_clean = f_path
			f_clean_part = os.path.basename(f_clean.replace("_text_SpaCy_sm_BIO.txt", ""))
			f_hand_part = os.path.basename(f_hand.replace("_text_beyond_hand_BIO.txt", ""))
			if (f_clean_part == f_hand_part):
				#print(f_clean_part)
				#print(f_hand_part)
				
				# open the variable to be read and split into words
				with open(f_clean, 'r', encoding='utf8') as f_BIO:
					# read and split into words to count word in file
					t_clean = f_BIO.read()
					#print(t_clean) 				
					#### PANDAS ####
					df_hand = pd.read_csv(f_hand, sep="\t", names=["TOK"])
					#print(df_hand)
					df_clean = pd.read_csv(f_clean, sep="\t", names=["TOKEN", "PREDICTION", "GOLD", "VALIDITY"])
					#print(df_clean)
					# convert the dictionary into DataFrame
					table_clean = pd.DataFrame(df_clean)
					#print(table_clean)
					table_hand = pd.DataFrame(df_hand)
					#print(table_hand)
					# split the column TOK in two GOLD with the IOB format and TOK_ with the tokenized text
					table_hand[['TOK_','GOLD_bio']] = table_hand.TOK.str.split(" ",expand=True,)
					#df['columnF'] = pd.Series(df1['columnF'])
					table_clean['GOLD']=pd.Series(table_hand['GOLD_bio'])
					# delete the index
					blankIndex=[''] * len(table_clean)
					table_clean.index=blankIndex
					
					# delete the column from TABLE_HAND previews columns
					del table_hand ['TOK']
					del table_hand ['TOK_']
					
					# it allows to display entire table
					pd.set_option("display.max_rows", None, "display.max_columns", None )
					table_clean['VALIDITY'] = table_clean.apply(compare, axis=1)

					#print(table_clean)
					
					# directory out
					output_dir = "/Users/alexsoares/Desktop/EHESS/dev/Savoirs_Spacy/db_results/SpaCy_prediction/prediction_sm/"
					# new files out with original's name plus _text and its new format .txt
					results_file = "%s%s_prediction.tsv"%(output_dir, os.path.splitext(os.path.basename(f_clean))[0])
					print(results_file)
					
					# write to files
					with open(results_file,'w') as write_csv:
						write_csv.write(table_clean.to_csv(sep='\t', index=False))
					#print(write_csv)
						

					

					

					

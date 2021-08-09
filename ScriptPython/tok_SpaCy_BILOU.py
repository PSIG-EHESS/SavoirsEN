# operation system
import os
# regular expression
import re
# retrives file support
import glob
# SpaCy NLP
import spacy
# conll03 format BIOLU
from spacy.training import offsets_to_biluo_tags
# NLP french language
from spacy.lang.fr import French
# applying spaCy to the file
from spacy.tokens import Doc

try:
    nlp = spacy.load('fr_dep_news_trf')
except OSError:
    #print("Do you have the spacy module fr_core_news_sm installed? If not run 'python -m spacy download fr_core_news_sm'")
    
    def custom_tokenize(text):
        words = text.split('|')
        return Doc(nlp.vocab, words=words)
    nlp.tokenizer = custom_tokenize

    # inform the path
    for file_path in glob.iglob('/Users/alexsoares/Desktop/EHESS/dev/Savoirs_env/tokenized_text/*.txt'): 
        #transform path into a readable file
        f_name = (file_path)
        #print(f_name)

        # open the variable to be read and split into words
        with open(f_name, 'r', encoding='utf8') as f:
            # read and split into words to count word in file
            #text = f.read()

            words = f.read().replace('\n', '|').replace('||','|').replace('||','|')
            words = words[:-1] #remove last pipe
            #print(words)

            # apply SpaCy
            doc = nlp(words)

            entities = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
            tags = offsets_to_biluo_tags(doc, entities)

            # directory out
            output_dir = "SpaCy_bert/"
            # new files out with original's name plus _SpaCY and its new format .txt
            results_file = "%s%s_SpaCy_bert.tsv"%(output_dir, os.path.splitext(os.path.basename(f_name))[0])
            print(results_file)

            # save it as blabla_.tsv
            count = 0
            with open(results_file, 'w', encoding='utf8') as fpout: 
                for tok in words.split("|"):
                    tag = str(tags[count])
                    fpout.write(str(tok)+"\t"+tag+"\n")
                    count = count + 1
                fpout.close()
            #print("fini")

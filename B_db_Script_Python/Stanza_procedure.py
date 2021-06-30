# -*- coding: UTF-8 -*-
#regex
import re
# NLP module
import stanza, os

#location directory 
location = '/Users/alexsoares/Desktop/EHESS/dev/Savoirs_Spacy/test_db/'

# import the model
nlp = stanza.Pipeline(lang='fr', processors='tokenize,ner', tokenize_pretokenized=True)

# apply the loop
for r, d, f in os.walk(location):
    for item in f:
        if item.endswith('conll.txt'):
            with open(os.path.join(r, item)) as fn:
                item2 = re.sub("_Stanza.txt", "", item)
                
                item2 = "prediction" + item2
                r2 = re.sub(".+(/.+?)$", "/Users/alexsoares/Desktop/EHESS/dev/Savoirs_Spacy/test_db/", r)
                
                pathtouse = str(os.path.join(r2, item2))+"_Stanza.tsv"
                print(pathtouse)
                fop = open(pathtouse, "w")
                print(pathtouse)
                words = [[line.strip() for line in fn]]
                #print(words)
                doc = nlp(words)
                for sent in doc.sentences:
                    for token in sent.tokens:
                        fop.write(token.text+"\t"+token.ner+"\n")
                fop.close()
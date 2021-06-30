# operation system
import os
# regular expression
import re
# retrives file support
import glob
# inform the path
for file_path in glob.iglob('SpaCy_tok/SpaCy_sm/*.tsv'):
    #transform path into a readable file
    f_name = (file_path)
    #print(f_name)
    
    # open the variable to be read and split into words
    with open(f_name, 'r', encoding='utf8') as f:
        # read and split into words to count word in file
        text = f.read()
        #print(text)
        
    _replacements = {
            'B-ORG': 'O',
            'U-ORG': 'O',
            'I-ORG': 'O',
            'L-ORG': 'O',
            
            'B-MISC': 'O',
            'U-MISC': 'O',
            'I-MISC': 'O',
            'L-MISC': 'O',
            
            'U-PER': 'B-PER',
            'U-LOC': 'B-LOC',
            'L-PER': 'I-PER',
            'L-LOC': 'I-LOC',
            }

    def _do_replace(text):
        return _replacements.get(text.group(0))

    def replace_tags(text, _re=re.compile('|'.join(re.escape(r) for r in _replacements))):
        return _re.sub(_do_replace, text)

    result = (replace_tags(text))
    #print(result)
    
    # directory out
    output_dir = "SpaCy_BIO/SpaCy_sm_BIO/"
    # new files out with original's name plus _BIO and its new format .txt
    results_file = "%s%s_BIO.txt"%(output_dir, os.path.splitext(os.path.basename(f_name))[0])
    print(results_file)
    # save it as blabla_BIO.txt
    with open(results_file, 'w', encoding='utf8') as fpout: 
        fpout.write(str(result))
        #print to verify the result
        #print(first)

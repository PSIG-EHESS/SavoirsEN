# operation system
import os
# regular expression
import re
# retrives file support
import glob
# inform the path
for file_path in glob.iglob('/Users/alexsoares/Desktop/EHESS/dev/Savoirs_env/4_db_OutputNerBeyond/*.conll'):
    #transform path into a readable file
    f_name = (file_path)
    #print(f_name)
    
    # open the variable to be read and split into words
    with open(f_name, 'r', encoding='utf8') as f:
        # read and split into words to count word in file
        text = f.read()
        #print(text)
        
    _replacements = {
            'B-TOP_GR': 'B-LOC',
            'B-PERSNAME_NAME': 'B-PER',
            'I-PERSNAME_NAME': 'I-PER',
            'I-TOP_GR': 'I-LOC',
            }

    def _do_replace(text):
        return _replacements.get(text.group(0))

    def replace_tags(text, _re=re.compile('|'.join(re.escape(r) for r in _replacements))):
        return _re.sub(_do_replace, text)

    result = (replace_tags(text))
    #print(result)
    
    # directory out
    output_dir = "/Users/alexsoares/Desktop/EHESS/dev/Savoirs_env/test_db/"
    # new files out with original's name plus _text and its new format .txt
    results_file = "%s%s_BIO.conll"%(output_dir, os.path.splitext(os.path.basename(f_name))[0])
    print(results_file)
    # save it as blabla_text.txt
    with open(results_file, 'w') as fpout: 
        fpout.write(str(result))
        #print to verify the result
        #print(first)


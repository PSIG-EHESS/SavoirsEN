# retrieve files
import glob
# operation system
import os
# library to work with html and xml files
from bs4 import BeautifulSoup as BeautifulSoup

# import a directory
input_dir = "/Users/alexsoares/Desktop/EHESS/dev/Savoirs_env/1_db_Savoirs/" #file root

# open all xml files in this directory 
for file_name in glob.glob(input_dir + "*.xml"):
    #named it as fp
    with open(file_name) as fp:
        #print(fp.read())
        
        # apply soap
        soup = BeautifulSoup(fp)
        # extract text part
        first = soup.find('text')
        # delete all titlepage tags    
        for tp in first.findAll('titlepage'):
            tp.decompose()
        # delete all listbibl tags
        for lb in first.findAll('listbibl'):
            lb.decompose()
        #delet all attributes    
        for tag in first.findAll(True): 
            del tag.attrs
                

        # directory out
        output_dir = "/Users/alexsoares/Desktop/EHESS/dev/Savoirs_env/test_db/" # output root
        # new files out with original's name plus _text and its new format .txt
        results_file = "%s%s_text.xml"%(output_dir, os.path.splitext(os.path.basename(file_name))[0]) # save filename with _text.xml
        print(results_file)
        # save it as blabla_text.txt
        with open(results_file, 'w') as fpout: 
            fpout.write(str(first))
            #print to verify the result
            print(first)
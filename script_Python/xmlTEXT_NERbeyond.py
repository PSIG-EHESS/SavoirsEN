# retrieve files
import glob
# os path
import os.path
# operation system
import os
# import regular expression module
import re

# import the directory with the files .txt
input_dir = "/Users/alexsoares/Desktop/EHESS/dev/Savoirs_env/test_db/" # Input folder

# open all xml files in this directory 
for file_name in glob.glob(input_dir + "*.xml"):
    #named it as fp
    with open(file_name) as fp:
        # print all files
        #print (fp.read())
        
        # imforn the tags which will be replaced and what will be located in their place 
        _replacements = {
            '<persname>': '[',
            '</persname>': ']',
            '<placename>': '{',
            '</placename>': '}',
            '<text xml:id="text">':'**',
            '</text>':'*',

                    }

        def _do_replace(fp):
            return _replacements.get(fp.group(0))

        def replace_tags(fp, _re=re.compile('|'.join(re.escape(r) for r in _replacements))):
            return _re.sub(_do_replace, fp)

        new_step = (replace_tags(str(fp.read())))
        
        #print(new_step) OK

        # as it says 
        TAG_REMOVE = re.compile(r'<[^>]+>')
        # as it says
        def remove_tags(new_step):
            return TAG_REMOVE.sub('', new_step)
            # end of process
        next_step = (remove_tags(str(new_step)))
        
        #print(next_step) OK
        new_replacements = {
            '[': '<persName.name>',
            ']': '</persName.name>',
            '{': '<top.gr>',
            '}': '</top.gr>',
            '**':'<text>',
            '*':'</text>'

                    }

        def _again_replace(next_step):
            return new_replacements.get(next_step.group(0))

        def place_tags(next_step, _re=re.compile('|'.join(re.escape(r) for r in new_replacements))):
            return _re.sub(_again_replace, next_step)

        last_step = (place_tags(str(next_step)))
        #print(last_step)
        finished = last_step

        # text without form
        new = (" ".join(finished.split()))
        #print(new_text)
        
                
        # directory out
        output_dir = "/Users/alexsoares/Desktop/EHESS/dev/Savoirs_env/test_db/" # output folder
        # new files out with original's name plus _text and its new format .txt
        results_file = "%s%s_beyond.xml"%(output_dir, os.path.splitext(os.path.basename(file_name))[0])
        print(results_file)
        # save it as (file name_text)_beyond.xml
        with open(results_file, 'w') as fp_out: 
            fp_out.write(str(new))
            # print it to verify the result
            print(new)
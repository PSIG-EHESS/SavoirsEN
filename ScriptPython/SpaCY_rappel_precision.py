import os
import glob
from nervaluate import Evaluator
import argparse
from tabulate import tabulate


'''
Ce script utilise nervaluate pour calculer la précision et le rappel
du marquage automatique des entités nommées par rapport à un étalon-or. 
Il recherche un dossier appelé "Predictions", qui doit contenir tous les fichiers à évaluer sous la forme suivante:
TOKEN   PREDICTION      GOLD   VALIDITY
Deux       O             O        1
mois       O             O        1
...
Les scores sont générés pour chaque fichier et enregistrés dans un dossier appelé "Scores".
'''

# Initialize the parser
parser = argparse.ArgumentParser(description="utilise nervaluate pour calculer la précision et le rappel" )

def pretty_print(result, outfile=None):
    """Affichage plus beau que par défaut"""
    x_name = ['Measure'] + [k for k in result]
    y_name = []
    rows = []
    for evaluation in result:
        # print(evaluation)
        metrics = result[evaluation]
        row = []
        for metric, score in metrics.items():
            if metric not in y_name:
                y_name.append(metric)
            row.append(round(score, 3)) # Arrondir
        rows.append(row)
    grid = [score for score in [column for column in zip(*rows)]]
    # print(*x_name, sep='\t', file=outfile)
    for i, row in enumerate(grid):
        # print(y_name[i], *map(str, row), sep='\t', file=outfile)
        
        
for input_file in glob.iglob("/Users/alexsoares/Desktop/EHESS/dev/Savoirs_env/8_db_SpaCy_results/SpaCy_prediction/prediction_BERT/*"):
    '''Loop throug the directory'''
    st_annotation = []
    gold_annotation = []
    
    # load the predictions and gold standard tags
    with open(input_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            try:
                #print(line)
                token, automatique, gold, validity = line.split('\t') 
                #print(token)
            except ValueError:
                # print(line)
            automatique = automatique.upper()
            # begin formatting the tags in the 'conll' format
            st_annotation.append(f"{token}\t{automatique}")
            gold_annotation.append(f"{token}\t{gold}")
    #finish 'conll' format
    true = '\n'.join(gold_annotation)
    pred_st = '\n'.join(st_annotation)
    #print(true)
    #print(pred_st)
   
    # generate precision and recall report
    evaluator = Evaluator(true, pred_st, tags=['LOC', 'PER'], loader="conll")
    results, results_by_tag = evaluator.evaluate()
    #print(results_by_tag)    
        
    # We can automatize it to do better
    # directory out
    output_dir = "/Users/alexsoares/Desktop/EHESS/dev/Savoirs_env/test_db/"
    
    # new files out with original's name plus _text and its new format .txt
    results_file = "%s%s_precision_rappel.csv"%(output_dir, os.path.splitext(os.path.basename(input_file))[0])
    # print(results_file)
    
    # save it as blabla_text.csv
    with open(results_file, 'w', encoding="utf-8") as fpout: 
        # pretty_print(results, outfile=fpout)
        
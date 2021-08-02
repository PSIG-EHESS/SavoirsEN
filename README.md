# PROJET Savoirs EN

Ce github concentre tous les scripts, les bases des données et les fichiers jupyter notebook qui comporte l'évolution du travail de stage d'Alex Soares 
sur la reconnaissance des entités nommées dans le cadre de projet Savoirs de l'Ehess, sous la direction de Carmen Brando.

# Les transformations et leurs bases de données

## 1 - step

### Objectif: 
recuperer le corps du text, tag (text) ainsi que remplacer les (persName) par (persName.name) et (placeName) par (top.gr) et enlever leurs attributs dans 
le but d'utiliser le transformateur NER & Beyond pour avoir un text tokenized.

### Input: 
db_1_savoirs_XMLtei
  #### example:
  
              <TEI lock="ndufournaud" time="2020-06-22T10:26:36.289+02:00" 
              xsi:schemaLocation="http://www.tei-c.org/ns/1.0 http://www.ehess.fr/crh/schemas/savoirs.xsd" xml:id="BNU_01_Didier">
              <teiHeader>
              <fileDesc>
              <titleStmt>
              <title type="main">
              Science et politique : le message de pierre de la Bibliothèque nationale et universitaire de Strasbourg
              </title>
              <title type="collection">
              La Revue de la BNU n
              <hi rend="sup">o</hi>
               1
              </title>
              <author role="aut">
              <forename>Christophe</forename>

### Output: 
db_2_NERbeyond
  #### example:
  
            <text>
            À la fin du XIXe siècle, le nouveau bâtiment de la Bibliothèque impériale de l’université et 
            de la régionespaces savantslieubibliothèque (Kaiserliche Universitäts- und Landesbibliothek, l’ancêtre de la BNU) 
            est construit dans le cœur symbolique du nouveau quartier édifié par les autorités allemandes, sur un côté de la place de 
            l’Empereur (Kaiserplatz, actuelle place de la République). Il avoisine le parlement régional, le palais où réside l’Empereur lorsqu’il se déplace à
            <top.gr>Strasbourg</top.gr>
            et deux bâtiments abritant, suivant le système politique allemand, des ministères régionaux. 
            Cette situation centrale donne évidemment à l’établissement culturel et éducatif qu’est la bibliothèque une 
            fonction politique qui prend sa place dans le programme de reconquête idéologique de l’
            <top.gr>Alsace</top.gr>

 #### fichier: 
 db_beyondNER.ipynb
 
## 2 - step

### Objectif: 
creation du fichier manuellement annoté (gold), remplacer les tags (B-TOP_GR) par (B-LOC),(I-TOP_GR) par (B-LOC), 
(B-PERSNAME_NAME) par (B-PER), (I-PERSNAME_NAME) par (I-PER) pour avoir le format IOB CONLL03

### Input: 
db_4_OutputNerBeyond 
#### obs : 
NER & Beyond output est fait en deux format .CONLL et .TXT
Cet outil n'accepte que 10 textes à la fois, je vous conseille de lire la doc.

#### http://nerbeyond.jerteh.rs/
  #### example: 
  
          facultés O
          de O
          l’université O
          de O
          Strasbourg B-TOP_GR
          : O
          au O
          sud O
          Hippocrate B-PERSNAME_NAME
          et O
          Grotius B-PERSNAME_NAME
          pour O
          la O
          médecine O
          et O
          le O
          droit, O
          au O
          nord O
          Erasme B-PERSNAME_NAME
          et O
          Scaliger B-PERSNAME_NAME
          pour O
          la O
          philosophie O
 
### Output: 
db_5_NERbeyond_BIO
  
  #### example:
  
          Martin B-PER
          Schongauer I-PER
          pour O
          la O
          Haute-Alsace B-LOC
          . O
          Le O
          dernier O
          médaillon O
          est O
          symboliquement O
          consacré O
          à O
          Herrade B-PER
          de I-PER
          Landsberg I-PER
          , O
          faisant O
          ainsi O
          écho, O
          par O
          le O
          biais O
          de O

## 3 - step

### Objectif:
 À partir de la sortie NER & Beyond CONLL, nous allons produire une tokenization pour pouvoir faire les annotations (prédiction)
 pour passer spaCy, autrement dit nous allons enlever la column IOB format CONLL pour avoir une tokenization syncronisée.
 
 ### Input: 
 db_5_NERbeyond_BIO
 
  #### example:
  
          Martin B-PER
          Schongauer I-PER
          pour O
          la O
          Haute-Alsace B-LOC
          . O
          Le O
          dernier O
          médaillon O
          est O
          symboliquement O
          consacré O
          à O
          Herrade B-PER
          de I-PER
          Landsberg I-PER
          , O
          faisant O
          ainsi O
          écho, O
          par O
          le O
          biais O
          de O

### Output: 
db_6_TOKenized_text
  
  #### example:
  
          À
          la
          fin
          du
          XIXe
          siècle,
          le
          nouveau
          bâtiment
          de
          la
          Bibliothèque
          impériale
          de
          l’université
          et
          de
          la
          régionespaces
          savantslieubibliothèque
          (Kaiserliche
          Universitäts-
          und

#### fichier: 
 faite avec regex sublime text
 
## 4 - step

### Objectif: 
Lorsque nous avons les output tokenized, nous allons creer les fichiers predictions pour pouvoir comparer avec le gold. 
SpaCy dans sa version v3 offre 4 pipelines trained dont une transformer 

    fr_core_news_sm size 16mb
    fr_core_news_md size 43mb
    fr_core_news_lg size 545mb
    fr_dep_news_trf French transformer pipeline (camembert-base) 

### Input: 
db_6_TOKenized_text
  
  #### example:
  
          À
          la
          fin
          du
          XIXe
          siècle,
          le
          nouveau
          bâtiment
          de
          la
          Bibliothèque
          impériale
          de
          l’université
          et
          de
          la
          régionespaces
          savantslieubibliothèque
          (Kaiserliche
          Universitäts-
          und

### Output:
db_7_SpaCy
#### obs:
Dans cette base de données il y a la sortie des 4 pipelines en format BIOLU car dans sa version 3 spaCy a choisi le format plus riche c'est BIOLU
B - Begin
I - Interior
O - Other
L - Last
U - Unique
  
  #### example:
  
          parlement),	O
          mêmes	O
          architectes	O
          (Hartel	O
          et	O
          Neckelmann	U-PER
          ),	O
          mêmes	O
          matériaux	O
          employés	O
          (grès	O
          vosgien	O
          pour	O
          l’extérieur,	O
          grès	O
          de	O
          la	O
          Forêt-Noire	U-LOC
          pour	O
          les	O
          escaliers	O

#### fichier: 
tok_SpaCy_BILOU.py

## 5 - step

### Objectif:
Nous avons les output prediction cependant leur étiquetage a été faite en BIOLU format et notre GOLD est en BIO format
allons devoir faire une transformation pour revenir vers un output prediction laballed BIO tout en savant que nous allons perdre une richesse descriptive dans
cette régression vers BIO format
Dans cette transformation nous faisons également le replacement de les étiquettes pour avoir une similarité dans notre prochaine étape 
    
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


 ### Input: 
 db_7_SpaCy/SpaCy_BIOLU
 
#### example:
  
          parlement),	O
          mêmes	O
          architectes	O
          (Hartel	O
          et	O
          Neckelmann	U-PER
          ),	O
          mêmes	O
          matériaux	O
          employés	O
          (grès	O
          vosgien	O
          pour	O
          l’extérieur,	O
          grès	O
          de	O
          la	O
          Forêt-Noire	U-LOC
          pour	O
          les	O
          escaliers	O          

### Output: 
db_7_SpaCy/SpaCy_BIO
#### obs:
dans la base de données db_7_SpaCy/ il y a les versions BIOLU et BIO output
  #### example:
  
          1892	O
          pour	O
          le	O
          parlement),	O
          mêmes	O
          architectes	O
          (Hartel	O
          et	O
          Neckelmann	B-PER
          ),	O
          mêmes	O
          matériaux	O
          employés	O
          (grès	O
          vosgien	O
          pour	O
          l’extérieur,	O
          grès	O
          de	O
          la	O
          Forêt-Noire	B-LOC
          pour	O
          les	O
          escaliers	O
          intérieurs),	O
          enfin	O

#### fichier: 
 SpaCyBILOU_toBIO.py
 
## 6 - step

### Objectif: 
Créer un fichier validity ou comparaison
L'objectif de cette comparaison est de savoir si les spaCy's pipelines trained ont su identifier les entités nommées annotées par les taggeurs.

### Input: 
 - db_7_SpaCy/SpaCy_BIO
 - db_5_NERbeyond_BIO

  #### example:
  
  regardez les exemples correspondant à chaque input

### Output: 
db_8_SpaCy_results/SpaCy_prediction
#### obs:
0 = ERROR
1 = VALIDITY
  #### example:
  
  |TOKEN |	PREDICTION	| GOLD	| VALIDITY
  | :--: | :----------: | :----:|  :----:
  |  À	 |      O	      |  O	  |    1
  |  la	 |     O	      |  O	  |    1
  |  fin |	   O	      |  O	  |    1
  |  ... |              |       |
  |  Bibl|	B-LOC	      |    O	|    O
  | impériale	| I-LOC	  |  O	  |     O
  | de	 | I-LOC	      | O	    |  O
  | l’université |I-LOC |	O	    |  O
 
 #### fichier: 
prediction_automatized.ipynb

## 7 - step

### Objectif: 
Alors que nous avons le fichier de prediction organisé, nous pouvons faire le rappel et precision pour calculer ces deux derniers.
Nous allons utiliser NERevaluate pour cet étape.
### Input: 
 db_8_SpaCy_results/SpaCy_prediction/
#### obs:
data cet input existent plusieurs résultats precisions et rappels
par pipelines / par fichiers / par tags /

  #### example:
  
  -  voir l'exemple avant
  
### Output: 
db_8_SpaCy_results/SpaCy_prediction
#### obs:

- pour comprendre les résultalts lire la documentation 
- https://pypi.org/project/nervaluate/

- plusieurs résultats sont disponibles

  #### example:
  
  Measure	  | ent_type 	| partial	 | strict |	exact |
  :-------: |  :------: | :-----:  | :-----:| :----:|
   correct	|      10	  |      0   |    0	  |    0  |
   incorrect|	    0	    |      0	 |    10	|    10 |
   partial	|    0	    |      10	 |     0	|     0 |
   missed	  |    26	    |    26	   |     26	|    26 |
   spurious	|    62	    |  62	     |     62	|    62 |
   possible	|    36	    |  36	     |   36	  |    36 |
   actual	  |    72	    |  72	     |   72	  |    72 |
   precision|	 0.139	  |  0.069   |	0.0   | 	0.0 |
   recall	  |  0.278	  |   0.139	 |   0.0	|   0.0 |
   f1	      |  0.185	  |    0.093 |    0	  |    0  |
   
   #### fichier :
   precision_rappel.ipynb

## 8 - step

### Objectif: 
Concatenate les résultats pour avoir une moyenne

### Input: 
8_db_SpaCy_results/SpaCy_precision_rappel/
  #### example:
  
  voir exemple anterieur
  
### output:
8_db_SpaCy_results/SpaCy_precision_rappel/
#### obs:
On a mis le résultat de la moyenne par tag dans input directory
   
  #### example:
  
 "Measure	 |  ent_type |	partial |	strict |	exact"
 :-------: |  :------: | :-----:  | :-----:| :----:|
  "correct | 	204	     |	222	    |190	   |222"
 "incorrect|	35		   |0	        |49	     |17"
"partial	 | 0		     |   0      |17		   |0"
"missed		 | 36		     |36	      |36	     |36"
"spurious	 |167		     |167	      |167	   |167"
"possible	 | 275		   |275	      |275	   |275"
"actual		 | 406		   |406	      |406	   |406"
"precision |	0.502		 |0.568	    |0.468	 |0.547"
"recall		 |0.742		   |0.838	    |0.691	 |0.807"
"f1		     |0.599		   |0.677	    |0.558	 |0.652"
  
#### fichier :
  Result_average.ipynb

## 9 - step

### Objectif: 
  - les dernières reglages avant d'entrainer notre pipeline pour creer notre best model
  - D'abord nous allons concatener les fichiers puis les diviser selon notre metrique pour l'entrainement 
  * 70% train
  * 20% evaluation
  * 10% test
  
### Input: 
db_10_tokenIOB
  #### example:
          
          de	O
          deux	O
          personnages	O
          symbolisent	O
          les	O
          facultés	O
          de	O
          l’université	O
          de	O
          Strasbourg	B-LOC
          :	O
          au	O
          sud	O
          Hippocrate	B-PER
          et	O
          Grotius	B-PER
          pour	O
          la	O
          médecine	O
          et	O
          le	O
          droit,	O
          au	O
          nord	O
          Erasme	B-PER
          et	O
          Scaliger	B-PER

### output:
13_db_spaCY_trainning

  #### example:
  
  tokenization de tous les textes
    
#### fichier :
  concatenate_eval_train_test.ipynb

## 10 - step

### Objectif: 
  - Après avoir reglagé quelques problèmes de concatenation pour avoir un fichier json  bien formé, nous allons transformer notre fichier manuellement annoté (GOLD) en format .tsv et le diviser selon la percentage choisie par Carmen Brando et moi.
  
  * 70% train
  * 20% evaluation et developement
  * 10% test
  
### Input:
  
13_db_spaCY_trainning
  
  #### example:
  
  tokenization 
  
### output:

13_db_spaCY_trainning/
  
  #### example:
  
  tokenization 
    
#### fichier :
  division_train_eval_test.ipynb

## 11 - step

### Objectif: 
  - transformer les fichiers divisés en json selon les percentage détérminée
  
  * 70% train
  * 20% evaluation et developement
  * 10% test
 
  - maintenant ces fichiers doivent être en json
  -  command line for a terminal (for d in *; do echo $d ; python -m spacy convert $d /Users/alexsoares/Desktop/EHESS/dev/Savoirs_env/13_db_spaCY_trainning/ -t json -s -c iob ; done
  - cette division est validate pour chaque pipeline
### Input: 
13_db_spaCY_trainning/
  #### example:
  
  voir la db
  
### output:
13_db_spaCY_trainning/

#### fichier :
  command line for a terminal (for d in *; do echo $d ; python -m spacy convert $d /Users/alexsoares/Desktop/EHESS/dev/Savoirs_env/13_db_spaCY_trainning/ -t json -s -c iob ; done

## 12 - step

### Objectif: 
  - transformer les fichiers .json en spacy binary pour lancer l'entrainement
  
### Input: 
13_db_spaCY_trainning/
  #### example:
  
  [
  {
    "id":0,
    "paragraphs":[
      {
        "raw":null,
        "sentences":[
          {
            "tokens":[
              {
                "id":0,
                "orth":"appara\u00eet",
                "space":" ",
                "tag":"-",
                "ner":"O"
              },
              {
                "id":1,
                "orth":"plus",
                "space":" ",
                "tag":"-",
                "ner":"O"
              },
              {
                "id":2,
                "orth":"complexe",
                "space":" ",
                "tag":"-",
                "ner":"O"
              },
              {

### output:
13_db_spaCY_trainning/
  ### example:
  fichier binary. spacy

#### fichier :
  command line for a terminal (for d in *; do echo $d ; python -m spacy convert $d /Users/alexsoares/Desktop/EHESS/dev/Savoirs_env/13_db_spaCY_trainning/ -t spacy; done
  
 




    











 






 





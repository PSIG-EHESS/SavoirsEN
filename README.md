# PROJET Savoirs EN

Ce github concentre tous les scripts, les bases des données et les fichiers jupyter notebook qui comporte l'évolution du travail de stage d'Alex Soares 
sur la reconnaissance des entités nommées dans le cadre de projet Savoirs de l'Ehess, sous la direction de Carmen Brando.

# Les transformations et leurs bases de données

## 1 - step

### Objectif: 
recuperer le corps du text, tag (text) ainsi que remplacer les (persName) par (persName.name) et (placeName) par (top.gr) et enlever leurs attributs dans 
le but d'utiliser le transformateur NER & Beyond pour avoir un text tokenized.

### Input: db_1_savoirs_XMLtei
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

### Output: db_2_NERbeyond
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

 - fichier: db_beyondNER.ipynb
 
## 2 - step

### Objectif: 
creation du fichier manuellement annoté (gold), remplacer les tags (B-TOP_GR) par (B-LOC),(I-TOP_GR) par (B-LOC), 
(B-PERSNAME_NAME) par (B-PER), (I-PERSNAME_NAME) par (I-PER) pour avoir le format IOB CONLL03

### Input: db_4_OutputNerBeyond 
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
 
### Output: db_5_NERbeyond_BIO
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





 
BILOU_to_BIO_ transformation.ipynb

BIO_ transformation_HAND.ipynb

BIO_to_BIOLU_automatized.ipynb

BIO_to_BIOLU_hand.ipynb

Evaluation des textes_handly.ipynb

Result_average.ipynb

Stanza_procedure.ipynb

TEST_SpaCY.ipynb

Token_BIO.ipynb

Token_BIO_SpaCy.ipynb

average_LOC_PER.ipynb

columns_TOKEN_IOB.ipynb

concatenate_eval_train_test.ipynb

database_procedure.ipynb

db_beyondNER.ipynb

division_train_eval_test.ipynb

precision_rappel.ipynb

precision_rappel_dic.ipynb

precision_rappel_handly.ipynb

precision_rappel_tag.ipynb

prediction_automatized.ipynb

prediction_handly.ipynb

presentation.ipynb

stanza.ipynb

tab_BILOU.ipynb

table_creation.ipynb

table_savoirs.xlsx

test_evaluation_tag.ipynb













<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 SAVOIRS Project: 
## Detecting placeName and persName (Named Entity Recognition) 

This project uses around 100 texts about History of sciences, History of knowlegdes, Anthropology of sciences and Culture Studies. It is directed by Christian Jacob - EHESS, piloted by Carmen Brando EHESS - Geomatique lab and executed by Carmen Brando and Alex Soares. 

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `train` | Train a named entity recognition model |
| `devuate` | devuate the model and export metrics |
| `package` | Package the trained model so it can be installed |
| `visualize-model` | Visualize the model's output interactively using Streamlit |
| `visualize-data` | Explore the annotated data in an interactive Streamlit app |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `train` &rarr; `devuate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/train.json`](assets/train.json) | Local | JSON-formatted training data |
| [`assets/dev.json`](assets/dev.json) | Local | JSON-formatted development data 
| [`assets/test.json`](assets/test.jsonl) | Local | JSON- formatted test file 

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->

---

## 📚 Data

[Labelling the data](https://explosion.ai/blog/sense2vec-reloaded#annotation-bootstrap)
took about 5 months and was done manually for gold files and prediction was done by spaCy. 

| File                                                                    | Count | Description                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------- | ----: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`test.json`](assets/test.json) | ?   | Match patterns created with [`sense2vec.teach`](https://github.com/explosion/sense2vec/tree/master#recipe-sense2vecteach) and [`sense2vec.to-patterns`](https://github.com/explosion/sense2vec/tree/master#recipe-sense2vecto-patterns). Can be used with spaCy's [`EntityRuler`](https://spacy.io/usage/rule-based-matching#entityruler) for a rule-based baseline and faster NER annotation. |
| [`train.json`](assets/train.json) |  ?| Training data annotated with `PER` and `LOC` entities.                                                                                                                                                                                                                                                                                                                                         |
| [`dev.json`](assets/dev.json)         |   ?| devuation data annotated with `PER` and `LOC` entities.                                                                                                                                                                                                                                                                                                                                       |

### Visualize the data and model

The [`visualize_data.py`](scripts/visualize_data.py) script lets you visualize
the training and devuation datasets with
[displaCy](https://spacy.io/usage/visualizers).

```bash
python -m spacy project run visualize-data
```

The [`visualize_model.py`](scripts/visualize_model.py) script is powered by
[`spacy-streamlit`](https://github.com/explosion/spacy-streamlit) and lets you
explore the trained model interactively.

```bash
python -m spacy project run visualize-model
```

### Training and devuation data format

The training and devuation datasets are distributed in 70% and 20%, both are JSON format. Each entry contains a `"text"` and a list of
`"id"` with the `"paragraphs"`, `"raw"`, `"sentences"` and `"tokens"`. For the annotated entities, `"id"`, `"orth"`, `"space"`, `"tag"` and `"ner"` . The data is tokenizated. 
Here's a simplified example entry:

```json
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
                "id":3,
                "orth":"que",
                "space":" ",
                "tag":"-",
                "ner":"O"
    
}
```

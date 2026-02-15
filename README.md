# GARLIC: Graph Attention-based Relational Learning of Multivariate Time Series in Intensive Care

This repository contains the implementation of **GARLIC**.
## Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

The code is tested with Python 3.11.

## Datasets

### PhysioNet Challenge 2012 & 2019

Download from:

- https://www.physionet.org/content/challenge-2012/1.0.0/
- https://physionet.org/content/challenge-2019/1.0.0/

### MIMIC-III

Request access from:

- https://physionet.org/content/mimiciii/1.4/

### Preparation

To reproduce results, place the corresponding raw datasets in the following directories:

```
./data/rawdata/P12/
./data/rawdata/P19/
./data/rawdata/MIMICIII/
```

Preprocessed data will be automatically generated in `./data/processed_data/` upon the first run.

## Run the Model

To train and evaluate the model on each dataset, run the corresponding shell scripts:

```bash
bash run.sh
bash interpretability_evaluation.sh
```

Each script initializes the model, preprocesses data if needed, trains the model, and reports AUROC and AUPRC.


# 🧄 GARLIC: Graph Attention-Based Relational Learning of Multivariate Time Series in Intensive Care

[![Paper](https://img.shields.io/badge/ICLR%202026-Paper-blue)](https://openreview.net/forum?id=4ZAwmIaA9y)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the official PyTorch implementation of **[GARLIC](https://openreview.net/pdf?id=4ZAwmIaA9y)**, accepted at **ICLR 2026**. 

GARLIC is a novel neural framework designed for accurate and interpretable clinical outcome prediction (e.g., mortality, sepsis) from irregularly sampled, multivariate Intensive Care Unit (ICU) time series. It achieves state-of-the-art performance on major benchmarks (PhysioNet-12, PhysioNet-19, and MIMIC-III) while providing transparent, built-in explanations at the observation, signal, and inter-signal relational levels.

## 🌟 Overview

Clinical data is often messy, irregular, and riddled with missing values. GARLIC tackles these challenges without sacrificing interpretability through a three-stage architecture:
1. **Latent Feature Modeling:** Handles irregular missingness using a learnable exponential-decay encoder.
2. **Time-Lagged Graph Message Passing:** Captures dynamic inter-sensor dependencies through learned summary graphs.
3. **Cross-Dimensional Sequential Attention:** Fuses global patterns across time and signals for robust prediction.

<p align="center">
  <img src="images/structure.pdf" alt="GARLIC Architecture overview" width="850">
  <br>
  <em>Figure: The GARLIC framework.</em>
</p>

## ⚙️ Requirements

The code is tested with **Python 3.11**. We recommend setting up a virtual environment (e.g., conda or venv) before installing dependencies.

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## 📊 Datasets & Preparation
We evaluate GARLIC on three standard public ICU datasets. You will need to download the raw data and place them in the correct directories.

### Download Links
- PhysioNet Challenge 2012 (P12): Download [here](https://physionet.org/content/challenge-2012/1.0.0/)
- PhysioNet Challenge 2019 (P19): Download [here](https://physionet.org/content/challenge-2019/1.0.0/)
- MIMIC-III: Request access [here](https://physionet.org/content/mimiciii/1.4/) (Credentialed access required)

### Directory Structure
Place the downloaded raw datasets into the following structure:

```
├── data/
│   ├── rawdata/
│   │   ├── P12/           # Place P12 raw files here
│   │   ├── P19/           # Place P19 raw files here
│   │   └── MIMICIII/      # Place MIMIC-III raw files here
│   └── processed_data/    # Auto-generated during the first run
├── run.sh
├── interpretability_evaluation.sh
└── ...
```
Note: Preprocessing will automatically trigger during the first run and save the cleaned data to ./data/processed_data/.

## 🚀 Running the Model
1. Training & Evaluation
To run the full pipeline (data preprocessing, model initialization, training, and evaluation), execute the main shell script. This will output the AUROC and AUPRC metrics for the tasks.

```bash
bash run.sh
```
2. Interpretability Evaluation
To reproduce the quantitative interpretability experiments (e.g., the perturbation-based masking using Top 50%, Bottom 50%, Random 50%), run:

```bash
bash interpretability_evaluation.sh
```

## 🧪 Reproducibility notes

- Fix random seeds (if exposed via flags/configs) for comparable results.
- Small numerical differences may occur across hardware and CUDA versions.
- The first run may take longer due to preprocessing and caching under ```./data/processed_data/.```


## 🙏 Acknowledgments
This research project was partially supported by the Schweizer Paraplegiker Stiftung and the ETH Zürich Foundation (2021-HS-348) and the JST Moonshot R\&D Program, Grant Number JPMJMS2034-18.

## 📖 Citation
If you find this code or our paper useful for your research, please consider citing:

```
@inproceedings{wang2026garlic,
  title={{GARLIC}: Graph Attention-Based Relational Learning of Multivariate Time Series in Intensive Care},
  author={Wang, Ruirui*, Li, Yanke*, G{\"u}nther, Manuel and Paez-Granados, Diego},
  booktitle={The Fourteenth International Conference on Learning Representations (ICLR)},
  year={2026},
  url={[https://openreview.net/forum?id=4ZAwmIaA9y](https://openreview.net/forum?id=4ZAwmIaA9y)}
}
```

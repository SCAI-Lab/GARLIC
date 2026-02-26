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
  <img src="assets/garlic_architecture.png" alt="GARLIC Architecture overview" width="850">
  <br>
  <em>Figure: The GARLIC framework.</em>
</p>

## ⚙️ Requirements

The code is tested with **Python 3.11**. We recommend setting up a virtual environment (e.g., conda or venv) before installing dependencies.

Install the required packages using pip:

```bash
pip install -r requirements.txt

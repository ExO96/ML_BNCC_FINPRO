<<<<<<< HEAD
# 🩺 Sistem Peringatan Dini Resiko Obesitas Terintegrasi (Early Warning System for Obesity Risk)

> **LnT Final Project — Kementerian Kesehatan Republik Indonesia x BNCC**

## 📌 Deskripsi Proyek
Proyek ini dikembangkan untuk mendukung program Kementerian Kesehatan Republik Indonesia dalam pencegahan obesitas dan peningkatan kesadaran gaya hidup sehat di masyarakat. 

Sistem ini merupakan model Machine Learning klasifikasi end-to-end yang dapat memprediksi tingkat resiko obesitas seseorang berdasarkan karakteristik fisik, kebiasaan makan, dan pola gaya hidup. Model telah di-deploy secara interaktif agar dapat diakses secara langsung oleh tenaga kesehatan di seluruh Puskesmas di Indonesia.

---

## 🚀 Fitur Utama & Alur Kerja
- **Exploratory Data Analysis (EDA):** Analisis komprehensif terhadap distribusi fitur, korelasi variabel gaya hidup terhadap tingkat obesitas, serta penanganan *class imbalance*.
- **Data Preprocessing & Scikit-Learn Pipeline:** Otomatisasi pembersihan data meliputi imputasi *missing values*, *encoding* variabel kategorikal, dan *feature scaling*.
- **Model Engineering & Hyperparameter Tuning:** Perbandingan performa model *baseline* (K-Nearest Neighbors) dengan model *advanced* (Random Forest & Gradient Boosting) menggunakan *K-Fold Cross Validation* dan *GridSearchCV*.
- **Model Evaluation:** Evaluasi mendalam berbasis metrik klasifikasi (*Accuracy, Precision, Recall, F1-Score*) dan analisis *Confusion Matrix*.
- **Interactive Web App Deployment:** Aplikasi web interaktif berbasis Streamlit yang di-deploy di platform Hugging Face Spaces.

---

## 🛠️ Teknologi & Library Utama
- **Bahasa Pemrograman:** Python 3.10+
- **Data Processing & ML:** Pandas, NumPy, Scikit-Learn, Imbalanced-Learn
- **Visualisasi Data:** Matplotlib, Seaborn
- **Web Framework & Deployment:** Streamlit, Hugging Face Spaces
- **Version Control & Pipeline:** Git, Joblib / Pickle
=======
---
title: ObesityLvl
emoji: 📊
colorFrom: red
colorTo: yellow
sdk: gradio
sdk_version: 6.26.0
python_version: '3.12'
app_file: app.py
pinned: false
short_description: Check your obesity level based your habits here!!
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
>>>>>>> 6a6386d191944a5a4e3feeccca9168f5c60f3f5c

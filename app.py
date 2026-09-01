import streamlit as st
import pandas as pd
import joblib

# Konfigurasi Halaman
st.set_page_config(page_title="Prediksi Obesitas", layout="wide")

st.title("🏥 Sistem Prediksi Tingkat Obesitas Puskesmas")
st.write("Aplikasi ini menggunakan model Machine Learning (Random Forest) untuk mendiagnosis tingkat obesitas pasien berdasarkan gaya hidup dan kondisi fisik.")
st.markdown("---")

# Buka Kapsul Model
model = joblib.load('model_obesitas.pkl')

# Merancang Komponen Input (Dibagi jadi 3 kolom layaknya Grid di Figma)
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Fisik & Riwayat")
    gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    age = st.number_input("Umur", min_value=10.0, max_value=100.0, value=20.0)
    height = st.number_input("Tinggi Badan (m)", min_value=1.0, max_value=2.5, value=1.70)
    weight = st.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0, value=70.0)
    family = st.selectbox("Riwayat Keluarga Obesitas", ["yes", "no"])
    mtrans = st.selectbox("Kendaraan Utama", ["Automobile", "Motorbike", "Bike", "Public_Transportation", "Walking"])

with col2:
    st.subheader("Pola Makan")
    favc = st.selectbox("Sering Makan Tinggi Kalori (FAVC)", ["yes", "no"])
    fcvc = st.slider("Konsumsi Sayur (FCVC)", 1.0, 3.0, 2.0)
    ncp = st.slider("Jumlah Makan Utama (NCP)", 1.0, 4.0, 3.0)
    caec = st.selectbox("Sering Makan Camilan (CAEC)", ["no", "Sometimes", "Frequently", "Always"])
    ch2o = st.slider("Minum Air/Hari (CH2O)", 1.0, 3.0, 2.0)
    calc = st.selectbox("Konsumsi Alkohol (CALC)", ["no", "Sometimes", "Frequently", "Always"])

with col3:
    st.subheader("Gaya Hidup")
    smoke = st.selectbox("Perokok (SMOKE)", ["yes", "no"])
    scc = st.selectbox("Pantau Kalori Harian (SCC)", ["yes", "no"])
    faf = st.slider("Aktivitas Fisik (FAF)", 0.0, 3.0, 1.0)
    tue = st.slider("Lama Main Gadget (TUE)", 0.0, 2.0, 1.0)

st.markdown("---")

# 5. Tombol Eksekusi
# use_container_width=True membuat tombolnya penuh/responsif
if st.button("🔍 Prediksi Sekarang", use_container_width=True):
    
    # Bungkus input jadi Dictionary agar nama kolom otomatis sama dengan X_train
    data_pasien = {
        'Gender': [gender],
        'Age': [age],
        'Height': [height],
        'Weight': [weight],
        'family_history_with_overweight': [family],
        'FAVC': [favc],
        'FCVC': [fcvc],
        'NCP': [ncp],
        'CAEC': [caec],
        'SMOKE': [smoke],
        'CH2O': [ch2o],
        'SCC': [scc],
        'FAF': [faf],
        'TUE': [tue],
        'CALC': [calc],
        'MTRANS': [mtrans]
    }
    
    # Ubah ke DataFrame
    df_pasien = pd.DataFrame(data_pasien)
    
    # Inference
    hasil = model.predict(df_pasien)
    
    st.success(f"### Hasil Diagnosis: {hasil[0]}")
    st.balloons() # Animasi balon saat berhasil (biar aplikasinya terasa hidup!)
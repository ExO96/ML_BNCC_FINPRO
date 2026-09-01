import streamlit as st
import pandas as pd
import joblib
import time

# Konfigurasi Halaman (Lebih Segar)
st.set_page_config(page_title="Prediksi Obesitas", page_icon="🩺", layout="wide")

# Header Interaktif
st.title("🏥 Sistem Prediksi Tingkat Obesitas Puskesmas")
st.caption("✨ Dibekali oleh kecerdasan buatan (Random Forest) untuk menganalisis gaya hidup dan metrik fisikmu secara instan.")
st.markdown("---")

# Buka Kapsul Model 
@st.cache_resource
def load_model():
    return joblib.load('model_obesitas.pkl')

model = load_model()

# Merancang Komponen Input (Grid 3 Kolom)
col1, col2, col3 = st.columns(3)

with col1:
    st.success("🧬 **Fisik & Riwayat**")
    gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    age = st.number_input("Umur", min_value=10.0, max_value=100.0, value=20.0, step=1.0)
    height = st.number_input("Tinggi Badan (m)", min_value=1.0, max_value=2.5, value=1.70, step=0.01)
    weight = st.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0, value=70.0, step=1.0)
    family = st.radio("Riwayat Keluarga Obesitas?", ["yes", "no"], horizontal=True)
    mtrans = st.selectbox("Kendaraan Utama", ["Automobile", "Motorbike", "Bike", "Public_Transportation", "Walking"])

with col2:
    st.warning("🍔 **Pola Makan**")
    favc = st.radio("Sering Makan Kalori Tinggi (FAVC)?", ["yes", "no"], horizontal=True)
    fcvc = st.slider("Konsumsi Sayur (FCVC)", 1.0, 3.0, 2.0, help="1 = Jarang, 3 = Selalu")
    ncp = st.slider("Jumlah Makan Utama (NCP)", 1.0, 4.0, 3.0)
    caec = st.selectbox("Sering Ngemil (CAEC)?", ["no", "Sometimes", "Frequently", "Always"])
    ch2o = st.slider("Minum Air/Hari (CH2O)", 1.0, 3.0, 2.0, help="Dalam hitungan liter")
    calc = st.selectbox("Konsumsi Alkohol (CALC)", ["no", "Sometimes", "Frequently", "Always"])

with col3:
    st.info("🏃‍♂️ **Gaya Hidup**")
    smoke = st.radio("Perokok (SMOKE)?", ["yes", "no"], horizontal=True)
    scc = st.radio("Pantau Kalori (SCC)?", ["yes", "no"], horizontal=True)
    faf = st.slider("Aktivitas Fisik (FAF)", 0.0, 3.0, 1.0, help="0 = Tidak Pernah, 3 = Rutin")
    tue = st.slider("Lama Main Gadget (TUE)", 0.0, 2.0, 1.0, help="0 = Sebentar, 2 = Sangat Lama")

st.markdown("---")

# Eksekusi Prediksi dengan Animasi
if st.button("🔍 Mulai Analisis Diagnosis", use_container_width=True):
    
    # Pesan loading sementara
    with st.spinner('Menganalisis profil gaya hidup pasien...'):
        time.sleep(1.5)
        
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
        
        df_pasien = pd.DataFrame(data_pasien)
        
        try:
            hasil = model.predict(df_pasien)[0]
            
            # 5. Output Dinamis Berdasarkan Hasil
            st.toast('Analisis Selesai!', icon='✅')
            
            if "Normal" in hasil or "Insufficient" in hasil:
                st.success(f"### 🎉 Hasil Diagnosis: {hasil}")
                st.write("Pasien berada di rentang berat badan yang aman. Pertahankan gaya hidup sehat!")
                st.balloons()
            elif "Overweight" in hasil:
                st.warning(f"### ⚠️ Hasil Diagnosis: {hasil}")
                st.write("Pasien mulai memasuki fase kelebihan berat badan. Kurangi camilan dan perbanyak air putih.")
            else:
                st.error(f"### 🚨 Hasil Diagnosis: {hasil}")
                st.write("Perhatian medis disarankan. Pasien perlu segera mengatur ulang aktivitas fisik dan pola makan.")
                st.snow() # Efek salju dramatis untuk peringatan obesitas
                
        except Exception as e:
            st.error(f"Terjadi kesalahan data (ValueError): {e}")
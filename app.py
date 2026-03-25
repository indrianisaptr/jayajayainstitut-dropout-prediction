import streamlit as st
import pandas as pd
import pickle

# =========================
# LOAD MODEL
# =========================
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# =========================
# TITLE
# =========================
st.title("Prediksi Risiko Dropout Mahasiswa")
st.write("Masukkan data mahasiswa untuk memprediksi apakah berisiko dropout atau tidak.")

# =========================
# INPUT USER
# =========================
st.subheader("Input Data Mahasiswa")

age = st.number_input("Usia saat masuk", 15, 60, 20)

grade1 = st.number_input("Nilai Semester 1", 0.0, 20.0, 10.0)
grade2 = st.number_input("Nilai Semester 2", 0.0, 20.0, 10.0)

approved1 = st.number_input("Jumlah MK Lulus Semester 1", 0, 20, 5)
approved2 = st.number_input("Jumlah MK Lulus Semester 2", 0, 20, 5)

tuition = st.selectbox(
    "Status Pembayaran Biaya",
    ["Lunas", "Belum Lunas"]
)

debtor = st.selectbox(
    "Status Tunggakan",
    ["Tidak Ada", "Ada"]
)

# mapping ke angka
tuition = 1 if tuition == "Lunas" else 0
debtor = 1 if debtor == "Ada" else 0

# =========================
# DATAFRAME INPUT
# =========================
input_data = pd.DataFrame({
    'Age_at_enrollment': [age],
    'Curricular_units_1st_sem_grade': [grade1],
    'Curricular_units_2nd_sem_grade': [grade2],
    'Curricular_units_1st_sem_approved': [approved1],
    'Curricular_units_2nd_sem_approved': [approved2],
    'Tuition_fees_up_to_date': [tuition],
    'Debtor': [debtor]
})

# =========================
# PREDICTION
# =========================
if st.button("Prediksi"):
    proba = model.predict_proba(input_data)[0][1]

    if proba > 0.7:
        st.error(f"⚠️ Risiko Dropout Tinggi ({proba:.2%})")
    elif proba > 0.4:
        st.warning(f"⚠️ Risiko Sedang ({proba:.2%})")
    else:
        st.success(f"✅ Risiko Rendah ({proba:.2%})")
    
st.markdown("""
Faktor yang mempengaruhi prediksi:
- Performa akademik (nilai semester)
- Jumlah mata kuliah yang lulus
- Status pembayaran
- Kondisi finansial (tunggakan)
""")
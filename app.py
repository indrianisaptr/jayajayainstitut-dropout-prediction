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

tuition = st.selectbox("Status Pembayaran Biaya (1 = Lunas, 0 = Tidak)", [0, 1])
debtor = st.selectbox("Memiliki Tunggakan (1 = Ya, 0 = Tidak)", [0, 1])

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
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Mahasiswa Berisiko Dropout")
    else:
        st.success("Mahasiswa Tidak Berisiko Dropout")
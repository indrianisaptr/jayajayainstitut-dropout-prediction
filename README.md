# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Institusi pendidikan menghadapi tantangan dalam mempertahankan mahasiswa hingga lulus. Tingginya angka dropout dapat berdampak pada reputasi institusi, efisiensi operasional, serta potensi kehilangan pendapatan.

Oleh karena itu, diperlukan pendekatan berbasis data untuk mengidentifikasi faktor-faktor yang mempengaruhi risiko dropout mahasiswa. Dengan memahami pola tersebut, institusi dapat mengambil langkah preventif melalui sistem deteksi dini dan intervensi yang tepat.

### Permasalahan Bisnis
Beberapa permasalahan bisnis yang dihadapi antara lain:

- Tingginya jumlah mahasiswa yang mengalami dropout
- Kesulitan dalam mengidentifikasi mahasiswa yang berisiko sejak dini
- Kurangnya pemahaman terhadap faktor utama yang mempengaruhi dropout
- Belum adanya sistem prediksi yang dapat membantu pengambilan keputusan berbasis data

### Cakupan Proyek
Cakupan proyek ini meliputi:

- Analisis data mahasiswa untuk memahami faktor-faktor yang mempengaruhi dropout
- Melakukan eksplorasi data (EDA) untuk menemukan pola dan insight
- Membangun model machine learning untuk memprediksi risiko dropout mahasiswa
- Membuat dashboard interaktif untuk visualisasi insight bisnis
- Mengembangkan prototype sistem prediksi berbasis Streamlit

### Persiapan

Sumber data:
Dataset performa mahasiswa yang mencakup aspek akademik, ekonomi, dan demografi, digunakan sebagai dasar analisis dan pemodelan prediksi dropout. (data.csv)

Link data:
https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv

Setup environment:
```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

## Business Dashboard
Dashboard dibuat menggunakan Google Looker Studio untuk memvisualisasikan faktor-faktor yang mempengaruhi dropout mahasiswa.

Dashboard menampilkan:

- Distribusi mahasiswa berdasarkan status (dropout vs non-dropout)
- Perbandingan performa akademik (nilai semester 1 dan 2)
- Pengaruh faktor ekonomi seperti status pembayaran dan tunggakan
- Analisis demografi seperti usia saat pendaftaran

Dashboard ini membantu institusi dalam memahami pola dropout serta mendukung pengambilan keputusan berbasis data.

Link dashboard:
https://lookerstudio.google.com/reporting/e85e6cdb-b1a7-45a0-afab-dc47fea294e0

## Menjalankan Sistem Machine Learning

Prototype sistem machine learning dapat diakses secara online melalui Streamlit.

Akses aplikasi melalui link berikut:
https://jayajayainstitut-dropout-prediction-mdmpsfzpsxewfismqrqwmb.streamlit.app/

Aplikasi ini memungkinkan pengguna memasukkan data mahasiswa dan mendapatkan prediksi apakah berisiko dropout atau tidak.

### Alternatif Menjalankan Secara Lokal

Prototype sistem machine learning dijalankan menggunakan Streamlit secara lokal.

Langkah menjalankan:

1. Pastikan file model.pkl tersedia
2. Jalankan perintah berikut:

```
streamlit run app.py
```
   
3. Buka browser di:
   http://localhost:8501

Aplikasi ini memungkinkan pengguna memasukkan data mahasiswa dan mendapatkan prediksi apakah berisiko dropout atau tidak.

## Conclusion
Berdasarkan hasil analisis data, permasalahan utama yang dihadapi institusi adalah kesulitan dalam mengidentifikasi mahasiswa yang berisiko dropout sejak dini. Hasil analisis menunjukkan bahwa risiko dropout dipengaruhi oleh beberapa faktor utama, yaitu performa akademik, kondisi ekonomi, dan faktor demografi. Mahasiswa dengan nilai akademik rendah, jumlah mata kuliah yang sedikit diselesaikan, serta memiliki kendala finansial seperti keterlambatan pembayaran atau tunggakan, cenderung memiliki risiko dropout yang lebih tinggi. Selain itu, usia saat pendaftaran juga turut berkontribusi terhadap kemungkinan mahasiswa menyelesaikan studi.

Untuk menjawab permasalahan tersebut, dibangun model machine learning menggunakan Random Forest yang mampu memprediksi risiko dropout dengan akurasi sebesar 88%. Model ini dapat membantu institusi dalam mengidentifikasi mahasiswa berisiko secara lebih cepat dan berbasis data, meskipun masih terdapat sejumlah kesalahan prediksi yang perlu diperhatikan dalam implementasi.

Selain itu, proyek ini juga mencakup dashboard interaktif yang digunakan untuk memvisualisasikan faktor-faktor utama yang mempengaruhi dropout, sehingga memudahkan pihak institusi dalam memahami pola dan tren yang terjadi. Prototype sistem berbasis Streamlit memungkinkan pengguna melakukan prediksi secara langsung terhadap data mahasiswa, sehingga dapat digunakan sebagai alat bantu operasional dalam proses monitoring.

Secara keseluruhan, solusi yang dibangun dapat diimplementasikan sebagai sistem deteksi dini (early warning system) dalam konteks nyata. Institusi dapat memanfaatkan sistem ini untuk melakukan identifikasi mahasiswa berisiko sejak semester awal, sehingga intervensi seperti pendampingan akademik, pemberian bantuan finansial, dan monitoring berkala dapat dilakukan lebih cepat dan tepat sasaran. Dengan demikian, solusi ini berkontribusi langsung dalam menurunkan angka dropout dan meningkatkan tingkat kelulusan mahasiswa.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- Mengembangkan sistem early warning untuk mendeteksi mahasiswa berisiko sejak semester awal
- Memberikan program pendampingan akademik bagi mahasiswa dengan performa rendah
- Menyediakan bantuan finansial atau skema pembayaran fleksibel bagi mahasiswa dengan kendala ekonomi
- Melakukan monitoring berkala terhadap mahasiswa dengan indikator risiko tinggi
- Mengintegrasikan model prediksi ke dalam sistem akademik institusi untuk pengambilan keputusan yang lebih cepat dan akurat

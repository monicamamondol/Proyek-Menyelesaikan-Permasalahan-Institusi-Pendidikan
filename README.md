# Proyek Akhir: Menyelesaikan Permasalahan Institut Pendidikan

## Business Understanding

### Latar Belakang Bisnis
Jaya Jaya Institut adalah lembaga pendidikan tinggi yang telah berdiri sejak tahun 2000 dan berhasil mencetak banyak lulusan berkualitas. Meskipun demikian, institusi ini menghadapi tantangan besar terkait tingginya angka mahasiswa yang tidak menyelesaikan studi atau dropout.
Masalah dropout ini merupakan masalah yang serius bagi institusi pendidikan, karena dropout yang tinggi dapat mempengaruhi citra institusi, mengurangi tingkat kelulusan, dan pada akhirnya berdampak pada daya tarik institusi bagi calon siswa di masa mendatang. Tingkat dropout yang tinggi juga bisa menjadi indikasi bahwa ada masalah mendasar dalam proses penerimaan siswa, pembelajaran, atau dukungan akademik yang disediakan oleh institusi.

### Permasalahan Bisnis
Permasalahan bisnis yang akan diselesaikan melalui proyek ini adalah:
1. Mengidentifikasi faktor-faktor utama yang memengaruhi angka dropout siswa, baik dari segi `latar belakang demografis`, `performa akademik`, maupun kondisi `sosial ekonomi`.

2. Menentukan pola atau karakteristik siswa yang cenderung mengalami dropout, seperti pengaruh status pekerjaan, jumlah penghasilan orang tua, dan beban studi.

3. Menyediakan alat bantu berupa dashboard interaktif yang memudahkan manajemen akademik dalam memantau data siswa dan mengambil tindakan preventif terhadap risiko dropout.

Dengan menyelesaikan permasalahan ini, institusi diharapkan dapat:

- Menurunkan angka dropout melalui intervensi berbasis data.

- Merancang program bimbingan dan dukungan yang lebih efektif untuk siswa berisiko tinggi.

- Meningkatkan tingkat kelulusan dan reputasi institusi pendidikan secara keseluruhan.

### Cakupan Proyek
Proyek ini mencakup:
1. **Eksplorasi dan Pemahaman Data**: Analisis dataset `data.csv` untuk memahami karakteristik siswa, distribusi status kelulusan, dan fitur-fitur yang relevan terhadap kemungkinan dropout.
2. **Data Preparation**: Membersihkan dan mempersiapkan data, termasuk penanganan nilai kosong, encoding variabel kategori, normalisasi data numerik, serta penyeimbangan kelas untuk memastikan kualitas model prediksi.
3. **Analisis Faktor Penyebab Dropout**:
   - Menganalisis korelasi antara variabel seperti nilai akademik, status sosial ekonomi, kehadiran, dan status beasiswa terhadap kemungkinan dropout.
   - Visualisasi tren dan pola dropout berdasarkan program studi, usia saat pendaftaran, dan riwayat akademik.
4. **Pembuatan Business Dashboard**: Visualisasi data dalam bentuk dashboard yang mudah dipahami untuk memantau faktor penyebab dropout.
5. **Kesimpulan dan Rekomendasi**: Menyusun ringkasan hasil analisis beserta rekomendasi tindakan konkret yang dapat diambil oleh institusi untuk menurunkan angka dropout dan meningkatkan keberhasilan akademik siswa.

### Persiapan
**Sumber data**:

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.
Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan.

Dataset yang digunakan dalam proyek ini adalah [Dataset Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance) sesuai dengan instruksi dari submission proyek ini.

**Setup environment**:

Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt`
```

Setup Environment - Shell/Terminal
```
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

Proyek ini membutuhkan lingkungan sederhana untuk menjalankan analisis data dan dashboard. Berikut langkah-langkah untuk mempersiapkan environment:
1. **Menjalankan `notebook.ipynb`**
   - Pastikan dependensi, packages, library yang dibutuhkan sudah tersedia (lihat file `requirements.txt` untuk melihat dependensi yang dibutuhkan).
   - Jalankan seluruh isi file `notebook.ipynb` menggunakan Google Colab/Jupyter Notebook untuk melihat hasil analisis data, temuan, dan insight yang diperoleh.
2. **Menjalankan Dashboard**:
   Untuk melihat isi dashboard secara langsung klik link ini https://lookerstudio.google.com/reporting/e73ef9a9-c6aa-4270-a5af-cd9a3265e080


## Business Dashboard
Dashboard ini dirancang untuk memberikan wawasan komprehensif kepada institut terhadap faktor-faktor yang berkontribusi dengan `Status` baik dropout, enrolled, ataupun graduated. Dengan dashboard ini tim institut dapat :
1. Memantau Tingkat Dropout Secara Proaktif:
    - Melalui visualisasi persentase siswa yang dropout, enrolled, dan graduate, tim dapat memantau tren dropout secara real-time. Ini memungkinkan institusi untuk segera mengambil tindakan jika terlihat ada peningkatan signifikan dalam tingkat dropout.
2. Menganalisis Faktor-Faktor yang Mempengaruhi Dropout:
    - Dengan analisis mendalam tentang bagaimana faktor-faktor seperti nilai akademik, beasiswa, biaya pendidikan, dan kualifikasi orang tua mempengaruhi status siswa, tim dapat mengidentifikasi elemen-elemen yang paling berisiko bagi siswa. Ini memungkinkan penyesuaian kebijakan dan intervensi yang lebih tepat sasaran.


## Menjalankan Prototype 
Pada proyek ini telah disediakan sebuah prototype untuk melakukan prediksi terhadap model yang sudah dibuat. Untuk menjalankan protoype secara lokal jalankan perintah berikut di terminal: 
```
streamlit run app.py

```
Atau buka [tautan](https://proyek-menyelesaikan-permasalahan-institusi-pendidikan-9zz4ysa.streamlit.app/) untuk membuka prototype yang sudah dijalankan pada streamlit community.

## Conclusion
Proyek ini dirancang untuk menjawab beberapa permasalahan utama yang dihadapi oleh Jaya Jaya Institut terkait dengan tingkat dropout siswa. 
Berikut adalah kesimpulan dari proyek ini:

1. **Membangun model prediktif yang akurat**:
    - Model Random Forest memberikan performa terbaik dengan **accuracy 90.77%** dan metrik lainnya yang tinggi. Dengan membangun model prediktif menggunakan algoritma seperti Random Forest, Jaya Jaya Institut dapat mengidentifikasi siswa-siswa yang berpotensi mengalami dropout sejak dini. Model ini mampu mendeteksi siswa berisiko dengan tingkat akurasi yang memadai berdasarkan data historis dan faktor-faktor demografis, akademik, serta ekonomi.

2. **Mengidentifikasi faktor utama penyebab dropout**:
    - Analisis korelasi dan pentingnya fitur dalam model prediktif menunjukkan bahwa beberapa faktor yang paling berpengaruh terhadap keputusan siswa untuk dropout antara lain latar belakang akademik (seperti nilai dan jumlah unit yang diambil) dan kondisi ekonomi (scholarship ataupun displaced) . Misalnya, siswa yang menghadapi kesulitan akademik dalam semester pertama atau kedua cenderung memiliki risiko lebih tinggi untuk dropout.
  
3. **Memberikan rekomendasi yang actionable**:

   Jaya Jaya Institut dapat segera menerapkan sistem pemantauan berbasis data untuk:
   - Menyediakan program remedial bagi siswa dengan nilai rendah.
   - Memberikan dukungan finansial bagi siswa yang kesulitan membayar.
   - Memberikan bimbingan akademik di awal semester untuk meningkatkan retensi.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
1. Implementasi Sistem Pemantauan Siswa Berbasis Data
    - Menerapkan model prediktif yang telah dibangun untuk memantau siswa secara berkala. Institusi dapat menggunakan sistem ini untuk mendeteksi siswa yang berisiko tinggi untuk dropout dan memberikan intervensi dini berupa bimbingan akademik atau dukungan lainnya.
2. Pengembangan Program Dukungan Akademik dan Psikologis
    - Berdasarkan faktor-faktor risiko yang diidentifikasi, institusi harus memperkuat program dukungan akademik dan psikologis. Ini bisa mencakup peningkatan akses ke bimbingan belajar, sesi konseling, dan dukungan kesehatan mental bagi siswa yang rentan.
3. Optimalisasi Kurikulum dan Program Studi
    - Lakukan evaluasi terhadap program studi yang memiliki tingkat dropout tinggi dan lakukan penyesuaian kurikulum atau metode pengajaran. Misalnya, meningkatkan fleksibilitas dalam penjadwalan kursus atau menyediakan materi pendukung tambahan dapat membantu mengurangi tekanan akademik pada siswa.

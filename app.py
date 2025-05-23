import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("random_forest_pipeline.joblib")

# Preprocessing function (if needed, else just return the input)
def preprocess_data(df):
    # Jika model sudah termasuk preprocessing pipeline, ini bisa dilewati
    return df

# Prediction function
def prediction(data):
    return model.predict(data)

# Streamlit UI
st.title("Prediksi Dropout Mahasiswa")

# Input form
with st.form(key='prediction_form'):
    marital_status = st.selectbox("Status Pernikahan", ['Single', 'Married', 'Widower', 'Divorced', 'Facto Union', 'Legally Separated'])
    application_mode = st.selectbox("Mode Aplikasi", list(range(1, 19)))
    application_order = st.number_input("Urutan Aplikasi", min_value=1, max_value=20, value=1)
    course = st.selectbox("Program Studi", list(range(33)))  # Sesuaikan dengan data asli
    daytime_evening_attendance = st.selectbox("Waktu Kuliah", ['Daytime', 'Evening'])
    previous_qualification = st.selectbox("Kualifikasi Sebelumnya", list(range(1, 19)))
    previous_qualification_grade = st.number_input("Nilai Kualifikasi Sebelumnya", min_value=0.0, max_value=200.0)
    nationality = st.selectbox("Kebangsaan", list(range(1, 22)))
    mothers_qualification = st.selectbox("Kualifikasi Ibu", list(range(1, 19)))
    fathers_qualification = st.selectbox("Kualifikasi Ayah", list(range(1, 19)))
    mothers_occupation = st.selectbox("Pekerjaan Ibu", list(range(1, 11)))
    fathers_occupation = st.selectbox("Pekerjaan Ayah", list(range(1, 11)))
    admission_grade = st.number_input("Nilai Masuk", min_value=0.0, max_value=200.0)
    age_at_enrollment = st.number_input("Usia Saat Masuk", min_value=15, max_value=100)
    displaced = st.selectbox("Pengungsi", ['Yes', 'No'])
    educational_special_needs = st.selectbox("Kebutuhan Khusus", ['Yes', 'No'])
    debtor = st.selectbox("Penunggak Biaya", ['Yes', 'No'])
    tuition_fees_up_to_date = st.selectbox("Biaya Kuliah Terkini", ['Yes', 'No'])
    gender = st.selectbox("Jenis Kelamin", ['Male', 'Female'])
    scholarship_holder = st.selectbox("Penerima Beasiswa", ['Yes', 'No'])
    international = st.selectbox("Mahasiswa Internasional", ['Yes', 'No'])
    
    curricular_units_1st_sem_enrolled = st.number_input("Mata Kuliah Semester 1 Diambil", 0)
    curricular_units_1st_sem_evaluations = st.number_input("Evaluasi Semester 1", 0)
    curricular_units_1st_sem_approved = st.number_input("Mata Kuliah Lulus Semester 1", 0)
    curricular_units_1st_sem_grade = st.number_input("Rata-rata Nilai Semester 1", 0.0)
    curricular_units_1st_sem_without_evaluations = st.number_input("Tanpa Evaluasi Semester 1", 0)
    
    curricular_units_2nd_sem_enrolled = st.number_input("Mata Kuliah Semester 2 Diambil", 0)
    curricular_units_2nd_sem_evaluations = st.number_input("Evaluasi Semester 2", 0)
    curricular_units_2nd_sem_approved = st.number_input("Mata Kuliah Lulus Semester 2", 0)
    curricular_units_2nd_sem_grade = st.number_input("Rata-rata Nilai Semester 2", 0.0)
    curricular_units_2nd_sem_without_evaluations = st.number_input("Tanpa Evaluasi Semester 2", 0)
    
    unemployment_rate = st.number_input("Tingkat Pengangguran", 0.0)
    inflation_rate = st.number_input("Tingkat Inflasi", 0.0)
    gdp = st.number_input("Produk Domestik Bruto", 0.0)
    
    submit_button = st.form_submit_button(label='Prediksi')

if submit_button:
    input_data = pd.DataFrame({
        'Marital_status': [marital_status],
        'Application_mode': [application_mode],
        'Application_order': [application_order],
        'Course': [course],
        'Daytime_evening_attendance': [daytime_evening_attendance],
        'Previous_qualification': [previous_qualification],
        'Previous_qualification_grade': [previous_qualification_grade],
        'Nacionality': [nationality],
        'Mothers_qualification': [mothers_qualification],
        'Fathers_qualification': [fathers_qualification],
        'Mothers_occupation': [mothers_occupation],
        'Fathers_occupation': [fathers_occupation],
        'Admission_grade': [admission_grade],
        'Age_at_enrollment': [age_at_enrollment],
        'Displaced': [displaced],
        'Educational_special_needs': [educational_special_needs],
        'Debtor': [debtor],
        'Tuition_fees_up_to_date': [tuition_fees_up_to_date],
        'Gender': [gender],
        'Scholarship_holder': [scholarship_holder],
        'International': [international],
        'Curricular_units_1st_sem_enrolled': [curricular_units_1st_sem_enrolled],
        'Curricular_units_1st_sem_evaluations': [curricular_units_1st_sem_evaluations],
        'Curricular_units_1st_sem_approved': [curricular_units_1st_sem_approved],
        'Curricular_units_1st_sem_grade': [curricular_units_1st_sem_grade],
        'Curricular_units_1st_sem_without_evaluations': [curricular_units_1st_sem_without_evaluations],
        'Curricular_units_2nd_sem_enrolled': [curricular_units_2nd_sem_enrolled],
        'Curricular_units_2nd_sem_evaluations': [curricular_units_2nd_sem_evaluations],
        'Curricular_units_2nd_sem_approved': [curricular_units_2nd_sem_approved],
        'Curricular_units_2nd_sem_grade': [curricular_units_2nd_sem_grade],
        'Curricular_units_2nd_sem_without_evaluations': [curricular_units_2nd_sem_without_evaluations],
        'Unemployment_rate': [unemployment_rate],
        'Inflation_rate': [inflation_rate],
        'GDP': [gdp]
    })

    # Preprocessing and prediction
    preprocessed_data = preprocess_data(input_data)
    result = prediction(preprocessed_data)

    # Display result
    if result[0] == 0:
        st.error("🔴 Prediksi: Mahasiswa Dropout")
    else:
        st.success("🟢 Prediksi: Mahasiswa Graduate")

import pandas as pd
import joblib
import numpy as np
import streamlit as st


# Muat model dan encoder saat aplikasi dimulai
pipeline = joblib.load("random_forest_pipeline.joblib")
encoders = joblib.load('encoder.joblib')

def preprocess_data(form_input):
    # Create a DataFrame directly from the input dictionary
    data_df = pd.DataFrame(form_input, index=[0])  # Ensure it is 2D with a single row

    # Kolom kategori
    category_cols = data_df.select_dtypes(include=['category', 'object']).columns.tolist()

    # Lakukan encoding untuk kolom kategori
    for col in category_cols:
        encoder = encoders[col]  # Mengambil encoder yang sesuai dengan kolom
        data_df[col] = encoder.transform(data_df[col])  # Lakukan transformasi
        encoders[col] = encoder  # Simpan encoder untuk kolom tersebut

    # Return the processed data
    return data_df

# Fungsi untuk melakukan prediksi
def prediction(data):
    # Memuat model prediksi yang telah dilatih
    model = joblib.load('random_forest_pipeline.joblib')
    
    # Memproses data input menggunakan preprocessing
    data_processed = preprocess_data(data)
    
    # Melakukan prediksi menggunakan model
    prediction = model.predict(data_processed)
    
    # Mengembalikan hasil prediksi (0: Tidak Dropout, 1: Dropout)
    return prediction

# Streamlit: Judul aplikasi
st.title("Prediksi Dropout Mahasiswa")

with st.form(key='input_form'):
    # Default values
    default_marital_status = 'single'
    default_application_mode = 'International student (bachelor)'
    default_application_order = 1
    default_course = 'Tourism'
    default_daytime_evening_attendance = 'daytime'
    default_previous_qualification = 'Secondary education'
    default_previous_qualification_grade = 160
    default_nationality = 'Portuguese'
    default_mothers_qualification = 'Secondary Education - 12th Year of Schooling or Eq.'
    default_fathers_qualification = 'Higher Education - Degree'
    default_mothers_occupation = 'Intermediate Level Technicians and Professions'
    default_fathers_occupation = 'Intermediate Level Technicians and Professions'
    default_admission_grade = 142.5  # Default as float
    default_displaced = 'yes'
    default_educational_special_needs = 'no'
    default_debtor = 'no'
    default_tuition_fees_up_to_date = 'no'
    default_gender = 'male'
    default_scholarship_holder = 'no'
    default_age_at_enrollment = 19
    default_international = 'no'
    default_curricular_units_1st_sem_enrolled = 6
    default_curricular_units_1st_sem_evaluations = 6
    default_curricular_units_1st_sem_approved = 6
    default_curricular_units_1st_sem_grade = 14
    default_curricular_units_1st_sem_without_evaluations = 6
    default_curricular_units_2nd_sem_enrolled = 6
    default_curricular_units_2nd_sem_evaluations = 6
    default_curricular_units_2nd_sem_approved = 6
    default_curricular_units_2nd_sem_grade = 13.66666667
    default_curricular_units_2nd_sem_without_evaluations = 6
    default_unemployment_rate = 13.9
    default_inflation_rate = -0.3
    default_gdp = 0.79

    marital_status = st.selectbox("Marital Status", options=['single', 'married'], index=0)
    application_mode = st.selectbox("Application Mode", options=['International student (bachelor)', 'Another mode'], index=0)
    application_order = st.number_input("Application Order", min_value=1, value=default_application_order)
    course = st.selectbox("Course", options=['Tourism', 'Other'], index=0)
    daytime_evening_attendance = st.selectbox("Attendance", options=['daytime', 'evening'], index=0)
    previous_qualification = st.selectbox("Previous Qualification", options=['Secondary education', 'Higher education'], index=0)
    previous_qualification_grade = st.number_input("Previous Qualification Grade", value=default_previous_qualification_grade)
    nationality = st.selectbox("Nationality", options=['Portuguese', 'Other'], index=0)
    mothers_qualification = st.selectbox("Mother's Qualification", options=['Secondary Education - 12th Year of Schooling or Eq.', 'Other'], index=0)
    fathers_qualification = st.selectbox("Father's Qualification", options=['Higher Education - Degree', 'Other'], index=0)
    mothers_occupation = st.selectbox("Mother's Occupation", options=['Intermediate Level Technicians and Professions', 'Other'], index=0)
    fathers_occupation = st.selectbox("Father's Occupation", options=['Intermediate Level Technicians and Professions', 'Other'], index=0)
    admission_grade = st.number_input("Admission Grade", value=default_admission_grade)
    displaced = st.selectbox("Displaced", options=['yes', 'no'], index=0)
    educational_special_needs = st.selectbox("Educational Special Needs", options=['no', 'yes'], index=0)
    debtor = st.selectbox("Debtor", options=['no', 'yes'], index=0)
    tuition_fees_up_to_date = st.selectbox("Tuition Fees Up to Date", options=['no', 'yes'], index=0)
    gender = st.selectbox("Gender", options=['male', 'female'], index=0)
    scholarship_holder = st.selectbox("Scholarship Holder", options=['no', 'yes'], index=0)
    age_at_enrollment = st.number_input("Age at Enrollment", value=default_age_at_enrollment)
    international = st.selectbox("International Student", options=['no', 'yes'], index=0)
    curricular_units_1st_sem_enrolled = st.number_input("Curricular Units 1st Sem Enrolled", value=default_curricular_units_1st_sem_enrolled)
    curricular_units_1st_sem_evaluations = st.number_input("Curricular Units 1st Sem Evaluations", value=default_curricular_units_1st_sem_evaluations)
    curricular_units_1st_sem_approved = st.number_input("Curricular Units 1st Sem Approved", value=default_curricular_units_1st_sem_approved)
    curricular_units_1st_sem_grade = st.number_input("Curricular Units 1st Sem Grade", value=default_curricular_units_1st_sem_grade)
    curricular_units_1st_sem_without_evaluations = st.number_input("Curricular Units 1st Sem Without Evaluations", value=default_curricular_units_1st_sem_without_evaluations)
    curricular_units_2nd_sem_enrolled = st.number_input("Curricular Units 2nd Sem Enrolled", value=default_curricular_units_2nd_sem_enrolled)
    curricular_units_2nd_sem_evaluations = st.number_input("Curricular Units 2nd Sem Evaluations", value=default_curricular_units_2nd_sem_evaluations)
    curricular_units_2nd_sem_approved = st.number_input("Curricular Units 2nd Sem Approved", value=default_curricular_units_2nd_sem_approved)
    curricular_units_2nd_sem_grade = st.number_input("Curricular Units 2nd Sem Grade", value=default_curricular_units_2nd_sem_grade)
    curricular_units_2nd_sem_without_evaluations = st.number_input("Curricular Units 2nd Sem Without Evaluations", value=default_curricular_units_2nd_sem_without_evaluations)
    unemployment_rate = st.number_input("Unemployment Rate", value=default_unemployment_rate)
    inflation_rate = st.number_input("Inflation Rate", value=default_inflation_rate)
    gdp = st.number_input("GDP", value=default_gdp)

    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    form_data = {
        'Marital_status': marital_status,
        'Application_mode': application_mode,
        'Application_order': application_order,
        'Course': course,
        'Daytime_evening_attendance': daytime_evening_attendance,
        'Previous_qualification': previous_qualification,
        'Previous_qualification_grade': previous_qualification_grade,
        'Nationality': nationality,
        'Mothers_qualification': mothers_qualification,
        'Fathers_qualification': fathers_qualification,
        'Mothers_occupation': mothers_occupation,
        'Fathers_occupation': fathers_occupation,
        'Admission_grade': admission_grade,
        'Displaced': displaced,
        'Educational_special_needs': educational_special_needs,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_fees_up_to_date,
        'Gender': gender,
        'Scholarship_holder': scholarship_holder,
        'Age_at_enrollment': age_at_enrollment,
        'International': international,
        'Curricular_units_1st_sem_enrolled': curricular_units_1st_sem_enrolled,
        'Curricular_units_1st_sem_evaluations': curricular_units_1st_sem_evaluations,
        'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
        'Curricular_units_1st_sem_without_evaluations': curricular_units_1st_sem_without_evaluations,
        'Curricular_units_2nd_sem_enrolled': curricular_units_2nd_sem_enrolled,
        'Curricular_units_2nd_sem_evaluations': curricular_units_2nd_sem_evaluations,
        'Curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': curricular_units_2nd_sem_grade,
        'Curricular_units_2nd_sem_without_evaluations': curricular_units_2nd_sem_without_evaluations,
        'Unemployment_rate': unemployment_rate,
        'Inflation_rate': inflation_rate,
        'GDP': gdp
    }

    result = prediction(form_data)
    st.subheader("Hasil Prediksi")
    if result[0] == 1:
        st.error("🚨 Mahasiswa diprediksi akan DROP OUT")
    else:
        st.success("✅ Mahasiswa diprediksi akan LULUS")

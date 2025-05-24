import pandas as pd
import joblib
import streamlit as st

# Muat model dan encoder saat aplikasi dimulai
model = joblib.load("random_forest_pipeline.joblib")
encoders = joblib.load('encoder.joblib')

# Fungsi untuk preprocessing

def preprocess_data(form_input):
    df = pd.DataFrame(form_input, index=[0])
    category_cols = df.select_dtypes(include=['object']).columns.tolist()
    for col in category_cols:
        encoder = encoders.get(col)
        if encoder:
            df[col] = encoder.transform(df[col])
    return df

# Fungsi prediksi
def prediction(data):
    processed = preprocess_data(data)
    return model.predict(processed)

# Tampilan UI Streamlit
st.set_page_config(page_title="Prediksi Dropout Mahasiswa", layout="wide")
st.markdown("""
    <style>
        .main { background-color: #f5f7fa; }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 24px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 Prediksi Dropout Mahasiswa")

col1, col2 = st.columns(2)

with st.form(key='input_form'):
    with col1:
        marital_status = st.selectbox("Marital Status", ['single', 'married'])
        application_mode = st.selectbox("Application Mode", ['International student (bachelor)', 'Another mode'])
        application_order = st.number_input("Application Order", min_value=1, value=1)
        course = st.selectbox("Course", ['Tourism', 'Other'])
        daytime_evening_attendance = st.selectbox("Attendance", ['daytime', 'evening'])
        previous_qualification = st.selectbox("Previous Qualification", ['Secondary education', 'Higher education'])
        previous_qualification_grade = st.number_input("Previous Qualification Grade", value=160)
        nationality = st.selectbox("Nationality", ['Portuguese', 'Other'])
        mothers_qualification = st.selectbox("Mother's Qualification", ['Secondary Education - 12th Year of Schooling or Eq.', 'Other'])
        fathers_qualification = st.selectbox("Father's Qualification", ['Higher Education - Degree', 'Other'])

    with col2:
        mothers_occupation = st.selectbox("Mother's Occupation", ['Intermediate Level Technicians and Professions', 'Other'])
        fathers_occupation = st.selectbox("Father's Occupation", ['Intermediate Level Technicians and Professions', 'Other'])
        admission_grade = st.number_input("Admission Grade", value=142.5)
        displaced = st.selectbox("Displaced", ['yes', 'no'])
        educational_special_needs = st.selectbox("Educational Special Needs", ['no', 'yes'])
        debtor = st.selectbox("Debtor", ['no', 'yes'])
        tuition_fees_up_to_date = st.selectbox("Tuition Fees Up to Date", ['no', 'yes'])
        gender = st.selectbox("Gender", ['male', 'female'])
        scholarship_holder = st.selectbox("Scholarship Holder", ['no', 'yes'])
        age_at_enrollment = st.number_input("Age at Enrollment", value=19)

    st.markdown("---")
    st.subheader("📘 Informasi Akademik Semester")
    col3, col4 = st.columns(2)

    with col3:
        cu1_enrolled = st.number_input("1st Sem Enrolled", value=6)
        cu1_eval = st.number_input("1st Sem Evaluations", value=6)
        cu1_approved = st.number_input("1st Sem Approved", value=6)
        cu1_grade = st.number_input("1st Sem Grade", value=14.0)
        cu1_wo_eval = st.number_input("1st Sem Without Evaluations", value=0)

    with col4:
        cu2_enrolled = st.number_input("2nd Sem Enrolled", value=6)
        cu2_eval = st.number_input("2nd Sem Evaluations", value=6)
        cu2_approved = st.number_input("2nd Sem Approved", value=6)
        cu2_grade = st.number_input("2nd Sem Grade", value=13.67)
        cu2_wo_eval = st.number_input("2nd Sem Without Evaluations", value=0)

    st.markdown("---")
    st.subheader("📉 Faktor Ekonomi")
    col5, col6 = st.columns(2)
    with col5:
        unemployment_rate = st.number_input("Unemployment Rate", value=13.9)
    with col6:
        inflation_rate = st.number_input("Inflation Rate", value=-0.3)
    gdp = st.number_input("GDP", value=0.79)

    submit_button = st.form_submit_button(label='🔍 Prediksi Dropout')

if submit_button:
    form_data = {
        'Marital_status': marital_status,
        'Application_mode': application_mode,
        'Application_order': application_order,
        'Course': course,
        'Daytime_evening_attendance': daytime_evening_attendance,
        'Previous_qualification': previous_qualification,
        'Previous_qualification_grade': previous_qualification_grade,
        'Nacionality': nationality,
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
        'International': 'no',
        'Curricular_units_1st_sem_enrolled': cu1_enrolled,
        'Curricular_units_1st_sem_evaluations': cu1_eval,
        'Curricular_units_1st_sem_approved': cu1_approved,
        'Curricular_units_1st_sem_grade': cu1_grade,
        'Curricular_units_1st_sem_without_evaluations': cu1_wo_eval,
        'Curricular_units_2nd_sem_enrolled': cu2_enrolled,
        'Curricular_units_2nd_sem_evaluations': cu2_eval,
        'Curricular_units_2nd_sem_approved': cu2_approved,
        'Curricular_units_2nd_sem_grade': cu2_grade,
        'Curricular_units_2nd_sem_without_evaluations': cu2_wo_eval,
        'Unemployment_rate': unemployment_rate,
        'Inflation_rate': inflation_rate,
        'GDP': gdp
    }

    with st.spinner("🔄 Memproses prediksi..."):
        result = prediction(form_data)

    st.markdown("---")
    st.subheader("📊 Hasil Prediksi:")
    if result[0] == 1:
        st.error("🚨 Mahasiswa diprediksi akan **DROP OUT**")
    else:
        st.success("✅ Mahasiswa diprediksi akan **LULUS**")
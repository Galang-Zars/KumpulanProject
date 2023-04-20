import streamlit as st
import pandas as pd
import pickle

st.title("Deteksi Kesehatan Jantung Anda")

# import model
model = pickle.load(open('final_pipeline.pkl' , 'rb'))


st.write('Isi kelengkapan data dibawah')

# user input
Age = st.slider(label='Age', min_value=10, max_value=100)
Sex = st.selectbox(label='Gender', options=['M', 'F', 'Non-Binary'])
ChestPainType = st.selectbox(label='ChestPainType', options=['TA', 'ASY', 'NAP', 'ATA'])
RestingBP = st.slider(label='RestingBP', min_value=100, max_value=200, step=1)
Cholesterol = st.slider(label='Cholesterol', min_value=0, max_value=409)
FastingBS = st.selectbox(label='FastingBS', options=[0, 1])
RestingECG = st.slider(label='RestingECG', min_value=0, max_value=300)
MaxHR = st.slider(label='MaxHR', min_value=0, max_value=300)
ExerciseAngina = st.selectbox(label='ExerciseAngina',options=['Y', 'N'])
Oldpeak = st.slider(label='Oldpeak', min_value=0.0, max_value=3.0, step=0.1)
ST_Slope = st.selectbox(label='ST_Slope', options=['Flat', 'Up', 'Down'])

# convert into dataframe
data = pd.DataFrame({'Age': [Age],
                'Sex': [Sex],
                'ChestPainType': [ChestPainType],
                'RestingBP':[RestingBP],
                'FastingBS': [FastingBS],
                'RestingECG': [RestingECG],
                'MaxHR': [MaxHR],
                'ExerciseAngina': [ExerciseAngina],
                'Oldpeak': [Oldpeak],
                'ST_Slope': [ST_Slope]
                })

# data = data.rename(columns={
#     'Age': 'age',
#     'Sex': 'sex',
#     'ChestPainType': 'CPT',
#     'RestingBP': 'RestBP',
#     'FastingBS': 'FastBP',
#     'RestingECG': 'RestECG',
#     'MaxHR': 'MaxHr',
#     'ExerciseAngina': 'EA',
#     'Oldpeak': 'OldPeak',
#     'ST_Slope': 'ST_slope',
# })
# interpretation
if st.button('Predict'):
    classifications = model.predict(data).tolist()[0]
    st.write('Prediction Result : ')
    if classifications == 0:
        st.subheader('Sehat')
    elif classifications == 1:
        st.subheader('Terindikasi jantung')
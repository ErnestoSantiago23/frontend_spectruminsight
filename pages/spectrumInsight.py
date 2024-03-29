import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import requests


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Aplicar el CSS
local_css("style.css")

st.title("SpectrumInsight")

preguntas = ["Question 1: Choose the child's age range in months",
             "Question 2: Choose the child's sex",
             "Question 3: Choose the child's ethnicity",
             "Question 4: Does the child have a family member with ASD?",
             "Question 5: Does your child look at you when you call his/her name?",
             "Question 6: How easy is it for you to get eye contact with your child?",
             "Question 7: Does your child point to indicate that s/he wants something? (e.g. a toy that is out of reach)",
             "Question 8: Does your child point to share interest with you? (e.g. pointing at an interesting sight)",
             "Question 9: Does your child pretend? (e.g. care for dolls, talk on a toy phone)",
             "Question 10: Does your child follow where you're looking?",
             "Question 11: If you or someone else in the family is visibly upset, does your child show signs of wanting to comfort them? (e.g. stroking hair, hugging them)",
             "Question 12: Would you describe your child's first words as:",
             "Question 13: Does your child use simple gestures? (e.g. wave goodbye)",
             "Question 14: Does your child stare at nothing with no apparent purpose?"]


answer_5_and_11 = ["--","Always", "Usually", "Sometimes", "Rarely", "Never"]
answer_7_questions = ["--","Many times a day", "A few times a day", "A few times a week", "Less than once a week", "Never"]
answer_6 = ["--","Very easy", "Quite easy", "Quite difficult", "Very difficult", "Impossible"]
answer_12 = ["--","Very typical", "Quite typical", "Slightly unusual", "Very unusual", "My child doesn't speak"]
answer_1 = ["--","12-18", "18-24", "24-30", "30 or more"]
answer_2 = ["--","Male", "Female"]
answer_3 = ["--",'Middle eastern', 'White european', 'Hispanic', 'Black', 'Asian', 'South asian', 'Native indian', 'Pacifica', 'Latino', 'Mixed', 'Others']
answer_4 = ["--","Yes", "No"]


mapeo_respuestas = {"Always": 0, "Sometimes": 1, "Never": 1, "Rarely": 1, "Usually": 0,
                    "Many times a day": 0, "A few times a day": 0, "A few times a week": 1, "Less than once a week": 1,
                    "Very easy": 0, "Quite easy": 0, "Quite difficult": 1, "Very difficult": 1, "Impossible": 1,
                    "Very typical": 0, "Quite typical": 0, "Slightly unusual": 1, "Very unusual": 1,
                    "My child doesn't speak": 0, "12-18": 0, "18-24": 1, "24-30": 2, "30 or more": 3,
                    "Male": 1, "Female": 0, "Yes": 1, "No": 0, "Hispanic": 0,
                    "White european": 5, "Middle eastern": 8, "Black": 7, "Asian": 6, "South asian": 10,
                    "Native indian": 2, "Mixed": 9, "Latino": 1, "Pacifica": 4, "Others": 3}

# Lista para almacenar las respuestas del usuario
respuestas_usuario = []

# Iterar a través de las preguntas y obtener las respuestas del usuario
for i, pregunta in enumerate(preguntas):
    if "Question 1:" in pregunta:
        st.write(f"**{pregunta}**")
        respuesta = st.selectbox(f"Select an option for question {i+1}", answer_1)
        st.write(f"*Selected Option for Question {i+1}:* {respuesta}")
        respuestas_usuario.append(mapeo_respuestas.get(respuesta, respuesta))
    elif "Question 2" in pregunta:
        st.write(f"**{pregunta}**")
        respuesta = st.selectbox(f"Select an option for question {i+1}", answer_2)
        st.write(f"*Selected Option for Question {i+1}:* {respuesta}")
        respuestas_usuario.append(mapeo_respuestas.get(respuesta, respuesta))
    elif "Question 3" in pregunta:
        st.write(f"**{pregunta}**")
        respuesta = st.selectbox(f"Select an option for question {i+1}", answer_3)
        st.write(f"*Selected Option for Question {i+1}:* {respuesta}")
        respuestas_usuario.append(mapeo_respuestas.get(respuesta, respuesta))
    elif "Question 4" in pregunta:
        st.write(f"**{pregunta}**")
        respuesta = st.selectbox(f"Select an option for question {i+1}", answer_4)
        st.write(f"*Selected Option for Question {i+1}:* {respuesta}")
        respuestas_usuario.append(mapeo_respuestas.get(respuesta, respuesta))
    elif "Question 5" in pregunta:
        st.write(f"**{pregunta}**")
        respuesta = st.selectbox(f"Select an option for question {i+1}", answer_5_and_11)
        st.write(f"*Selected Option for Question {i+1}:* {respuesta}")
        respuestas_usuario.append(mapeo_respuestas.get(respuesta, respuesta))
    elif "Question 6" in pregunta:
        st.write(f"**{pregunta}**")
        respuesta = st.selectbox(f"Select an option for question {i+1}", answer_6)
        st.write(f"*Selected Option for Question {i+1}:* {respuesta}")
        respuestas_usuario.append(mapeo_respuestas.get(respuesta, respuesta))
    elif "Question 11" in pregunta:
        st.write(f"**{pregunta}**")
        respuesta = st.selectbox(f"Select an option for question {i+1}", answer_5_and_11)
        st.write(f"*Selected Option for Question {i+1}:* {respuesta}")
        respuestas_usuario.append(mapeo_respuestas.get(respuesta, respuesta))
    elif "Question 12" in pregunta:
        st.write(f"**{pregunta}**")
        respuesta = st.selectbox(f"Select an option for question {i+1}", answer_12)
        st.write(f"*Selected Option for Question {i+1}:* {respuesta}")
        respuestas_usuario.append(mapeo_respuestas.get(respuesta, respuesta))
    elif "Question 14" in pregunta:
        st.write(f"**{pregunta}**")
        respuesta = st.selectbox(f"Select an option for question {i+1}", answer_7_questions)
        st.write(f"*Selected Option for Question {i+1}:* {respuesta}")
        if mapeo_respuestas.get(respuesta, respuesta) == 0:
            respuestas_usuario.append(1)
        else:
            respuestas_usuario.append(0)
    else:
        st.write(f"**{pregunta}**")
        respuesta = st.selectbox(f"Select an option for question {i+1}", answer_7_questions)
        st.write(f"*Selected Option for Question {i+1}:* {respuesta}")
        respuestas_usuario.append(mapeo_respuestas.get(respuesta, respuesta))

if st.button("Predict"):
    if "--" in respuestas_usuario:
        st.error("Please answer all the questions before proceeding.")
    else:
        # Preparar los datos para enviar a la API
        data = {
            "months_encoder": respuestas_usuario[0],
            "sex": respuestas_usuario[1],
            "ethnicity_encoder": respuestas_usuario[2],
            "family_mem_with_ASD": respuestas_usuario[3],
            "a1": respuestas_usuario[4],
            "a2": respuestas_usuario[5],
            "a3": respuestas_usuario[6],
            "a4": respuestas_usuario[7],
            "a5": respuestas_usuario[8],
            "a6": respuestas_usuario[9],
            "a7": respuestas_usuario[10],
            "a8": respuestas_usuario[11],
            "a9": respuestas_usuario[12],
            "a10": respuestas_usuario[13]
        }

        # Enviar los datos a la API y recibir la respuesta
        url = 'https://spectruminsight-e5rx7utlva-ue.a.run.app'
        response = requests.get(url+'/predict', params=data)

        if response.status_code == 200:
            result = response.json()
            prediction = result['prediccion']
            proba = result['probability']

            # Mostrar el resultado
            if prediction == 1:
                st.write(f"The answers give a {proba[1]:.2%} probability that the child is on the spectrum")
            else:
                st.write(f"The answers give a {proba[0]:.2%} probability that the child is not on the spectrum")

            st.write("**Please do not take these results as infallible. Go to the doctor, if you have not already done so, and verify these results with a professional. In the graph below you can see the possibilities for each case.**")

        # Visualización de la probabilidad (opcional)
            fig, ax = plt.subplots()
            bars = ax.bar(['No ASC', 'ASC'], proba, color=['lightcoral', 'lightgreen'])
            ax.set_ylabel('Probability')
            ax.set_title('Prediction Probability')

            for bar in bars:
                yval = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2.0, yval, f"{yval:.2%}", ha='center', va='bottom')
            st.pyplot(fig)

        else:
            st.error(f"Error in API call: {response.status_code}")

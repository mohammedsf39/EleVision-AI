import random
import time

import streamlit as st


class Doctor:
    def __init__(self, name, associated_hospital):
        self.remaining_tries = 20
        self.name = name
        self.associated_hospital = associated_hospital


class Model:
    def __init__(self, model_path, disease_info: dict) -> None:
        self.model_path = model_path
        self.disease_info = disease_info
        self.model = None

    def predict(self, image) -> str:
        time.sleep(3)
        random_disease = random.choice(list(self.disease_info.keys()))
        return random_disease, self.disease_info[random_disease]


def main():
    app_config()
    render_side_bar()

    diseases_info = {
        'Normal eye': 'No abnormalities detected in the eye.',
        'Age - related Macular Degeneration(AMD)': 'A common eye condition and a leading cause of vision loss among people age 50 and older.',
        'Central Serous Chorioretinopathy(CSCR)': 'Buildup of fluid under the retina, causing vision distortion.',
        'Retinal Vein Occlusion(RVO)': 'Blockage of the veins that carry blood away from the retina, leading to vision loss.',
        'Epiretinal Membrane(ERM)': 'Formation of a thin layer of scar tissue on the surface of the retina, causing vision distortion.',
        'Retinitis Pigmentosa(RP)': 'A group of inherited diseases causing degeneration of the retina, leading to vision loss.',
        'Macular Hole(MH)': 'A small break in the macula, causing blurred or distorted central vision.',
        'Retinal Detachment': 'Separation of the retina from the underlying tissue, causing sudden vision loss.'
    }

    model = Model("model", diseases_info)

    input_form_column, prediction_result_column = st.columns(2)

    with input_form_column:
        uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            with st.container(height=350, border=None):
                st.image(uploaded_file, caption="Uploaded Image", width=600)

            predict_button = st.button("Predict")
            if predict_button:
                prediction_result = model.predict(uploaded_file)

    with prediction_result_column:
        if uploaded_file and predict_button:
            st.write("## Prediction Results")
            with st.spinner('Wait for it...'):
                st.markdown(f"""
                    <p style='
                        padding:10px 20px;
                        font-size:24px; 
                        font-weight:bold; 
                        color:#1434A4;
                        background-color: rgb(240, 242, 246); 
                        border-radius: 0.5rem;'>
                        {prediction_result[0]}
                    </p>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                    <p style='padding:5px 20px;'>
                        {prediction_result[1]}
                    </p>
                """, unsafe_allow_html=True)


def app_config():
    st.set_page_config(layout="wide")
    st.title("OCT Ailments Detector")


def render_side_bar():
    st.sidebar.image('logo.png', width=200)
    doctor = Doctor(name="John Doe", associated_hospital="ElOued hospital")
    st.sidebar.title("Doctor Profile")
    st.sidebar.write(f"Dr. {doctor.name}")
    st.sidebar.write(f"{doctor.associated_hospital}")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.markdown(f"""
        <p style='
            font-weight:bold; 
            border:1px solid rgb(255, 75, 75); 
            color:rgb(255, 75, 75); 
            text-align:center; 
            border-radius: 0.5rem;'>
            Remaining Tries: {doctor.remaining_tries} try
        </p>
    """, unsafe_allow_html=True)
    st.sidebar.markdown(f"[Subscribe from here]({0})")


if __name__ == "__main__":
    main()

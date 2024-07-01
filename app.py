import streamlit as st
import preprocessor
import pandas as pd
from datetime import datetime


st.set_page_config(layout="wide")
st.title('Poly Pulleys Faults Detection')


col1, col2 = st.columns(2)

manual_data=st.sidebar.button(label="Manual Enter Values")
image_data=st.sidebar.button(label='upload a image')

if manual_data:
    with col1:
        pulley_location = st.selectbox(label='Pulley Location',options=['Head Pulley', 'Bend Pulley', 'Tail Pulley'])
        belt_tension = st.slider(label="Belt Tension",min_value=200,max_value=600,step=1)
        Speed = st.number_input(label="Speed",min_value=1.5000000, max_value=5.5000000,step=0.0000001, format="%.7f")
        Material = st.selectbox(label="Material",options=['Limestone', 'Coal', 'Iron Ore', 'Steel', 'Sand'])
        Vibration = st.number_input(label="Vibration",min_value=0.1, max_value=1.5,step=0.0000001, format="%.7f")
        Temprerature = st.number_input(label="Temerature",min_value=30, max_value=60,step=1)
        Acoustic = st.number_input(label="Acoutic",min_value=50, max_value=80,step=1)


        df = pd.DataFrame([[datetime.now().date(),pulley_location,belt_tension,Speed,Material,Vibration,Temprerature,Acoustic,'Groove Damage'
        ]],columns=['Timestamp', 'Pulley Location', 'Belt Tension', 'Speed', 'Material',
            'Vibration', 'Temperature', 'Acoustic', 'Problem Label'])

    with col2:

        if st.button('Predict'):
            prediction = str(preprocessor.preprocess(df)[0])
            if prediction == "Misalignment":
                st.header("Misalignment")
                st.write("What cause the belt misalignment? Belt misalignment is the off-centre travel of the conveyor belt along the conveyor system. Belt misalignment can be caused by a number of factors including: damaged conveyor structure or ill-fitting components, poor belt splices, environmental conditions or material loading effects.")
                st.image('./images/misalignment.png',width=500)
            elif prediction ==  "Excessive Wear":
                st.header("Excessive Wear")
                st.write("One key cause of wear and tear on conveyor belts: not keeping up on regular maintenance. Components, bearings, rollors, and motors can quickly wear down over time. Without proper care and maintenance, one (or more!) of these essential parts can break without a moment's notice.")
                st.image('./images/excessive wear.jpeg',width=500)
            elif prediction ==  "Bearing Failure":
                st.header("Bearing Failure")
                st.write("Conveyor Pulley bearing failure is a common maintenance challenge encountered on most mine sites on a daily basis. When a bearing fails, eventually it means the conveyor will need to stop in order to repair or change out the entire pulley. This is a costly exercise and interrupts production.")
                st.image('./images/bearing design.png',width=500)
            elif prediction ==  "Groove Damage":
                st.header("Groove Damage")
                st.write("Grooves in the belt generally stem from entrapped materials. Often belts will develop signs of wear at a fixed distance from their edge that appear to be caused by overly-abrasive or poorly adjusted belt seals. But generally this wear is actually the result of fines or other materials trapped underneath the seal.")
                st.image('./images/groove.jpeg',width=500)
            elif prediction ==  "Loose Belt":
                st.header("Loose Belt")
                st.write('Conveyor belts require an exact balance of tension to operate correctly. Having too little or too much tension can cause belt slippage. Besides slippage, improper tension and insufficient traction also can create a strain or stretch on the belts, along with loud squealing and grating noises.')
                st.image('./images/looseblet.webp',width=500)
            else:
                st.write("Pata nhi")

elif image_data:
    with col1:
        file = st.file_uploader(label="upload imaeg of the pulley")
    with col2:
        st.write('you result')
        
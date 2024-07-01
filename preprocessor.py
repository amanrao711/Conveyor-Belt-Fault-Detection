import pickle as pk
import pandas as pd

scaler =  pk.load(open('./model/scaler.pkl', 'rb'))
OHE = pk.load(open('./model/OHE.pkl', 'rb'))
classifier = pk.load(open('./model/classifier.pkl', 'rb'))

    # pully_location
    # belt_tension
    # Speed
    # Material
    # Vibration
    # Temerature
    # Acoutic

def preprocess(df):
    df = df.drop(['Timestamp'],axis=1)
    df[['Pulley Location_Bend Pulley', 'Pulley Location_Head Pulley',
       'Pulley Location_Tail Pulley', 'Material_Coal',
       'Material_Iron Ore', 'Material_Limestone', 'Material_Sand',
       'Material_Steel']] = OHE.transform(df[['Pulley Location','Material']]).toarray()
    df = df.drop(["Pulley Location","Material"],axis=1)
    df[['Belt Tension','Vibration','Temperature','Acoustic','Speed']] = scaler.transform(df[['Belt Tension','Vibration','Temperature','Acoustic','Speed']])
    df = df.drop(['Problem Label'],axis=1)

    return classifier.predict(df) 
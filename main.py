import pickle


scaler = pickle.load(open('./model/scaler.pkl', 'rb'))

scaler.transform()
import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_rumah.sav', 'rb'))

st.title('Estimasi Harga Rumah/Apartment')

Area_in_sq_ft = st.number_input('Input Luas Meter Persegi')
Bedrooms = st.number_input('Input Jumlah Kamar Tidur')
Bathrooms = st.number_input('Input Jumlah Kamar Mandi')


predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[Area_in_sq_ft, Bedrooms, Bathrooms]]
    )
    st.write ('Estimasi harga rumah/apartment dalam Pound Sterling : ', predict)
    st.write ('Estimasi harga rumah/apartment dalam Rupiah : ', predict*19000)

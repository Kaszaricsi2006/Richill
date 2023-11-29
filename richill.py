import streamlit as st

def szamologep(a, b):
    osszeg = a + b
    kulonbseg = a - b
    szorzat = a * b
    osztas = a / b if b != 0 else "Nem osztható 0-val"
    return osszeg, kulonbseg, szorzat, osztas

st.title('Egyszerű Számológép')

szam1 = st.number_input("Kérem az első számot:")
szam2 = st.number_input("Kérem a második számot:")

if st.button('Számol'):
    eredmeny = szamologep(szam1, szam2)
    st.write(f'Összeg: {eredmeny[0]}')
    st.write(f'Különbség: {eredmeny[1]}')
    st.write(f'Szorzat: {eredmeny[2]}')
    st.write(f'Osztás: {eredmeny[3]}')

import streamlit as st
import pandas as pd
from PIL import Image

def main():
    st.title("Kép és Excel táblázat megjelenítése a Streamlitben")

    # Kép beolvasása
    image = Image.open('https://th.bing.com/th/id/R.c8c6dda0a605d7dd6d0daa943ea3c691?rik=%2bg9eponkh4YkRA&riu=http%3a%2f%2fwww.pgiengineering.com%2fmedia%2fcitys%2fmexido-df.jpg&ehk=6QmdBwVK2y%2fl6x8z18lh4igOKtQ50VOc6muEUTroCI4%3d&risl=&pid=ImgRaw&r=0')  # Itt cseréld le a 'sample_image.jpg'-t a saját képed nevére

    # Kép megjelenítése
    st.image(image, caption='Ez egy példa kép', use_column_width=True)

    # Excel fájl beolvasása
    excel_data = pd.read_excel('weblap.xlsx')  # Itt cseréld le a 'sample_excel.xlsx'-t a saját Excel fájlod nevére

    # Excel táblázat megjelenítése
    st.write("Excel táblázat:")
    st.dataframe(excel_data)

if _name_ == "_main_":
    main()

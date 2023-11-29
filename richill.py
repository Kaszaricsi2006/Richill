import streamlit as st
import pandas as pd
from PIL import Image

def main():
    st.title("Kép és Excel táblázat megjelenítése a Streamlitben")

    # Kép beolvasása
    image = Image.open('sample_image.jpg')  # Itt cseréld le a 'sample_image.jpg'-t a saját képed nevére

    # Kép megjelenítése
    st.image(image, caption='Ez egy példa kép', use_column_width=True)

    # Excel fájl beolvasása
    excel_data = pd.read_excel('sample_excel.xlsx')  # Itt cseréld le a 'sample_excel.xlsx'-t a saját Excel fájlod nevére

    # Excel táblázat megjelenítése
    st.write("Excel táblázat:")
    st.dataframe(excel_data)

if _name_ == "_main_":
    main()

import streamlit as st
import sqlite3

# Streamlit alkalmazás létrehozása
def main():
    st.title('SQL Adatbázis Streamlit Alkalmazás')

    # Adatbázis inicializálása vagy megnyitása
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # Tábla létrehozása, ha még nem létezik
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                 )''')

    # Felhasználók beszúrása
    try:
        c.execute("INSERT INTO users (id, name) VALUES (1, 'John')")
        c.execute("INSERT INTO users (id, name) VALUES (2, 'Alice')")
        c.execute("INSERT INTO users (id, name) VALUES (3, 'Bob')")
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Hiba történt az adatbázisban: {e}")
    finally:
        # Adatbázis kapcsolat lezárása
        conn.close()

    # Streamlit kódok az adatok megjelenítéséhez, módosításához, törléséhez, stb.
    # Például:
    menu = ['Create', 'Read', 'Update', 'Delete']
    choice = st.sidebar.selectbox('Válassz műveletet:', menu)

    if choice == 'Create':
        # Felhasználók létrehozása űrlap segítségével st.text_input, st.number_input, st.button stb. használatával
        pass
    elif choice == 'Read':
        # Adatok megjelenítése
        pass
    elif choice == 'Update':
        # Adatok frissítése űrlap segítségével st.text_input, st.number_input, st.button stb. használatával
        pass
    elif choice == 'Delete':
        # Adatok törlése
        pass

if __name__ == '__main__':
    main()

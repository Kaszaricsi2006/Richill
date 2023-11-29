import streamlit as st
import sqlite3

# Adatbázis kapcsolat létrehozása
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Tábla létrehozása, ha még nem létezik
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Streamlit alkalmazás létrehozása
def main():
    st.title('SQL Adatbázis Streamlit Alkalmazás')

    menu = ['Create', 'Read', 'Update', 'Delete']
    choice = st.sidebar.selectbox('Válassz műveletet:', menu)

    if choice == 'Create':
        st.subheader('Hozzáadás új felhasználóhoz')
        name = st.text_input('Név', value='', max_chars=50, help='Írd be a nevet', key='name_input')
        age = st.number_input('Kor', 0)
        if st.button('Felhasználó hozzáadása'):
            # Kézi karakterkódolás az ékezetes karakterek kezelésére
            encoded_name = name.encode('utf-8')
            decoded_name = encoded_name.decode('utf-8')
            c.execute('INSERT INTO users (name, age) VALUES (?, ?)', (decoded_name, age))
            conn.commit()
            st.success('Felhasználó hozzáadva: {} - {}'.format(decoded_name, age))

    elif choice == 'Read':
        st.subheader('Felhasználók listázása')
        result = c.execute('SELECT * FROM users')
        for row in result:
            st.write(f"Név: {row[1]}, Kor: {row[2]}")

    elif choice == 'Update':
        st.subheader('Felhasználó frissítése')
        users = c.execute('SELECT * FROM users')
        user_list = [row[1] for row in users]
        selected_user = st.selectbox('Válassz felhasználót', user_list)
        new_name = st.text_input('Új név', value='', max_chars=50, help='Írd be az új nevet', key='new_name_input')
        new_age = st.number_input('Új kor', 0)
        if st.button('Felhasználó frissítése'):
            # Kézi karakterkódolás az ékezetes karakterek kezelésére
            encoded_new_name = new_name.encode('utf-8')
            decoded_new_name = encoded_new_name.decode('utf-8')
            c.execute('UPDATE users SET name=?, age=? WHERE name=?', (decoded_new_name, new_age, selected_user))
            conn.commit()
            st.success('Felhasználó frissítve: {} - {}'.format(decoded_new_name, new_age))

    elif choice == 'Delete':
        st.subheader('Felhasználó törlése')
        users = c.execute('SELECT * FROM users')
        user_list = [row[1] for row in users]
        user_to_delete = st.selectbox('Válassz felhasználót törléshez', user_list)
        if st.button('Felhasználó törlése'):
            c.execute('DELETE FROM users WHERE name=?', (user_to_delete,))
            conn.commit()
            st.warning('Felhasználó törölve: {}'.format(user_to_delete))

if __name__ == '__main__':
    main()

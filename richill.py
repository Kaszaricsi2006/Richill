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
        name = st.text_input('Név', '')
        age = st.number_input('Kor', 0)
        if st.button('Felhasználó hozzáadása'):
            c.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
            conn.commit()
            st.success('Felhasználó hozzáadva: {} - {}'.format(name, age))

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
        new_name = st.text_input('Új név', '')
        new_age = st.number_input('Új kor', 0)
        if st.button('Felhasználó frissítése'):
            c.execute('UPDATE users SET name=?, age=? WHERE name=?', (new_name, new_age, selected_user))
            conn.commit()
            st.success('Felhasználó frissítve: {} - {}'.format(new_name, new_age))

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

import streamlit as st

i1= st.button("button 1")
st.write("value:", i1)

i2 = st.checkbox("reset button")


import streamlit as st

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')


# image example
import streamlit as st
from PIL import Image

# Title
st.title("Display Image Example")

# Load image
image = Image.open("images.jpg")

# Display image
st.image(image, caption='Example Image', use_column_width=True)    
import  streamlit as st
import sqlite3

# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        st.error(e)
    return conn

# Function to create a table in the database
def create_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS records (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
                     )''')
    except sqlite3.Error as e:
        st.error(e)

# Function to insert a record into the database
def insert_record(conn, name):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO records (name) VALUES (?)", (name,))
        conn.commit()
        st.success(f"Record '{name}' added successfully!")
    except sqlite3.Error as e:
        st.error(e)

# Function to remove a record from the database
def remove_record(conn, id):
    try:
        c = conn.cursor()
        c.execute("DELETE FROM records WHERE id=?", (id,))
        conn.commit()
        st.success("Record removed successfully!")
    except sqlite3.Error as e:
        st.error(e)

# Main function to run the app
def main():
    st.title("Database Operations with Streamlit")

    # Create a database connection
    conn = create_connection("example.db")

    if conn is not None:
        create_table(conn)

        # Add record section
        st.header("Add Record")
        new_name = st.text_input("Enter name to add:")
        if st.button("Add"):
            if new_name:
                insert_record(conn, new_name)
            else:
                st.warning("Please enter a name.")

        # Remove record section
        st.header("Remove Record")
        record_id = st.text_input("Enter ID of record to remove:")
        if st.button("Remove"):
            if record_id:
                remove_record(conn, record_id)
            else:
                st.warning("Please enter the ID of the record.")

        # Display existing records
        st.header("Existing Records")
        c = conn.cursor()
        c.execute("SELECT * FROM records")
        records = c.fetchall()
        for record in records:
            st.write(f"ID: {record[0]}, Name: {record[1]}")

        conn.close()
    else:
        st.error("Error: Unable to create database connection.")

if __name__ == "__main__":
    main()


import streamlit as st

# Define functions for each page
def page_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

def page_about():
    st.title("About Page")
    st.write("Welcome to the About Page!")

def page_contact():
    st.title("Contact Page")
    st.write("Welcome to the Contact Page!")

# Define a function to display navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", options=["Home", "About", "Contact"])

    if page == "Home":
        page_home()
    elif page == "About":
        page_about()
    elif page == "Contact":
        page_contact()

# Run the main function to start the app
if __name__ == "__main__":
    main()

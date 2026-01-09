import streamlit as st
import pandas as pd
import psycopg2

st.title("Data Engineering Dashboard")

st.write("Welcome to your local data engineering project!")

# Example connection (will fail until DB is ready and configured)
st.sidebar.header("Database Connection")
try:
    # This expects the DATABASE_URL env var to be set or defaults to standard airflow db
    # In a real app, you'd probably have a separate analytics DB
    conn = psycopg2.connect(
        host="postgres",
        user="airflow",
        password="airflow",
        database="airflow"
    )
    st.sidebar.success("Connected to Postgres!")
    
    # Simple query to show it works (listing tables)
    cur = conn.cursor()
    cur.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
    """)
    tables = cur.fetchall()
    st.write("### Available Tables in 'public' schema:")
    st.dataframe(pd.DataFrame(tables, columns=["Table Name"]))
    
except Exception as e:
    st.sidebar.error(f"Connection failed: {e}")

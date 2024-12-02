import psycopg2
import random
from datetime import datetime
from db_config import db_config

def connect_db():
    conn = psycopg2.connect(**db_config)
    return conn

def generate_random_data(num_records):
    data = []
    for _ in range(num_records):
        name = f"Name{random.randint(1, 100000)}"
        age = random.randint(18, 99)
        email = f"{name.lower()}@example.com"
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data.append((name, age, email, created_at))
    return data

def insert_data(num_records):
    conn = connect_db()
    cursor = conn.cursor()
    data = generate_random_data(num_records)
    
    query = """INSERT INTO your_table (name, age, email, created_at) 
               VALUES (%s, %s, %s, %s)"""
    cursor.executemany(query, data)
    conn.commit()
    cursor.close()
    conn.close()

insert_data(1000)
